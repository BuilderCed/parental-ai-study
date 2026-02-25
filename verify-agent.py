"""
RESPIRE Discovery Agent — Live Verification
=============================================
Fetches actual agent config from ElevenLabs API and validates
every setting against expected values.

Usage:
  python verify-agent.py
"""

import os
import json
import sys

# Unset proxy vars that cause SOCKS errors
for var in ["ALL_PROXY", "all_proxy", "HTTPS_PROXY", "HTTP_PROXY",
            "https_proxy", "http_proxy"]:
    os.environ.pop(var, None)

from elevenlabs.client import ElevenLabs

AGENT_ID = "agent_4301kj6mtc0debes0xew21d3yyhw"

client = ElevenLabs()

# ============================================================
# 1. Fetch live agent config
# ============================================================
print("=" * 60)
print("RESPIRE Discovery Agent — Live Verification")
print("=" * 60)

print("\n1/5 — Fetching agent config from API...")
try:
    agent = client.conversational_ai.agents.get(agent_id=AGENT_ID)
    print(f"   Agent found: {agent.name}")
except Exception as e:
    print(f"   FATAL: Cannot fetch agent: {e}")
    sys.exit(1)

# ============================================================
# 2. Validate conversation_config
# ============================================================
print("\n2/5 — Validating conversation config...")

errors = []
warnings = []

conv = agent.conversation_config

# Language
if hasattr(conv, "agent") and conv.agent:
    lang = getattr(conv.agent, "language", None)
    if lang == "fr":
        print("   [OK] Language: fr")
    else:
        errors.append(f"Language is '{lang}', expected 'fr'")

    # First message
    fm = getattr(conv.agent, "first_message", "")
    if fm and "Camille" in fm:
        print(f"   [OK] First message contains 'Camille' ({len(fm)} chars)")
    else:
        errors.append(f"First message missing or doesn't mention Camille")

    # Prompt
    prompt_cfg = getattr(conv.agent, "prompt", None)
    if prompt_cfg:
        prompt_text = getattr(prompt_cfg, "prompt", "")
        llm = getattr(prompt_cfg, "llm", "")
        temp = getattr(prompt_cfg, "temperature", None)

        if "interview" in prompt_text.lower() or "camille" in prompt_text.lower():
            print(f"   [OK] System prompt loaded ({len(prompt_text)} chars)")
        else:
            warnings.append("System prompt may not contain interview instructions")

        if "claude" in str(llm).lower() and "sonnet" in str(llm).lower():
            print(f"   [OK] LLM: {llm}")
        else:
            errors.append(f"LLM is '{llm}', expected Claude Sonnet")

        if temp is not None and 0.4 <= temp <= 0.6:
            print(f"   [OK] Temperature: {temp}")
        else:
            warnings.append(f"Temperature is {temp}, recommended 0.5")

        # Knowledge base
        kb = getattr(prompt_cfg, "knowledge_base", [])
        if kb and len(kb) > 0:
            print(f"   [OK] Knowledge base: {len(kb)} document(s)")
        else:
            errors.append("No knowledge base attached")
    else:
        errors.append("No prompt configuration found")

# TTS
if hasattr(conv, "tts") and conv.tts:
    voice = getattr(conv.tts, "voice_id", "")
    model = getattr(conv.tts, "model_id", "")
    speed = getattr(conv.tts, "speed", None)

    if voice == "EXAVITQu4vr4xnSDxMaL":
        print("   [OK] Voice: Sarah (EXAVITQu4vr4xnSDxMaL)")
    else:
        errors.append(f"Voice is '{voice}', expected Sarah")

    if "v2_5" in str(model) or "v2.5" in str(model):
        print(f"   [OK] TTS model: {model}")
    else:
        errors.append(f"TTS model '{model}' must be turbo/flash v2.5 for French")

    if speed is not None:
        print(f"   [OK] TTS speed: {speed}")
    else:
        warnings.append("TTS speed not set (default 1.0)")

# Turn-taking
if hasattr(conv, "turn") and conv.turn:
    mode = getattr(conv.turn, "mode", "")
    timeout = getattr(conv.turn, "turn_timeout", None)
    eagerness = getattr(conv.turn, "turn_eagerness", None)

    if mode in ("turn", "turn_based"):
        print(f"   [OK] Turn mode: {mode}")
    else:
        errors.append(f"Turn mode is '{mode}', expected 'turn'")

    if timeout and timeout >= 15:
        print(f"   [OK] Turn timeout: {timeout}s")
    else:
        warnings.append(f"Turn timeout is {timeout}s, recommended 20s for interviews")

    if eagerness:
        print(f"   [OK] Turn eagerness: {eagerness}")
    else:
        warnings.append("Turn eagerness not set via API (check dashboard)")

# ASR
if hasattr(conv, "asr") and conv.asr:
    quality = getattr(conv.asr, "quality", None)
    keywords = getattr(conv.asr, "keywords", [])
    if not keywords:
        keywords = getattr(conv.asr, "keyterms", [])

    if keywords and len(keywords) > 0:
        print(f"   [OK] ASR keywords: {len(keywords)} terms")
    else:
        warnings.append("ASR keywords not set (may not be readable via API)")

    if quality:
        print(f"   [OK] ASR quality: {quality}")

# Conversation limits
if hasattr(conv, "conversation") and conv.conversation:
    max_dur = getattr(conv.conversation, "max_duration_seconds", None)
    if max_dur and max_dur >= 1200:
        print(f"   [OK] Max duration: {max_dur}s ({max_dur // 60} min)")
    else:
        warnings.append(f"Max duration is {max_dur}s, recommended 1500s")

# ============================================================
# 3. Validate platform settings
# ============================================================
print("\n3/5 — Validating platform settings...")

ps = agent.platform_settings
if ps:
    # Privacy
    privacy = getattr(ps, "privacy", None)
    if privacy:
        record = getattr(privacy, "record_voice", getattr(privacy, "record_conversation", None))
        retention = getattr(privacy, "retention_days", None)
        if record:
            print(f"   [OK] Recording: ON")
        else:
            errors.append("Recording is OFF — transcripts needed for analysis")
        if retention and retention <= 90:
            print(f"   [OK] Retention: {retention} days (RGPD OK)")
        elif retention:
            warnings.append(f"Retention {retention} days may exceed RGPD minimization")

    # Call limits
    limits = getattr(ps, "call_limits", None)
    if limits:
        max_dur = getattr(limits, "max_call_duration_secs", None)
        max_conc = getattr(limits, "max_concurrent_calls", None)
        if max_dur:
            print(f"   [OK] Max call duration: {max_dur}s")
        if max_conc:
            print(f"   [OK] Max concurrent: {max_conc}")
else:
    warnings.append("Platform settings not readable via API")

# ============================================================
# 4. Validate security (prompt content)
# ============================================================
print("\n4/5 — Validating security guardrails in prompt...")

prompt_text = ""
if hasattr(conv, "agent") and conv.agent:
    prompt_cfg = getattr(conv.agent, "prompt", None)
    if prompt_cfg:
        prompt_text = getattr(prompt_cfg, "prompt", "")

security_checks = [
    ("JAMAIS mentionner une app", "no app/product mention"),
    ("JAMAIS poser de question hypothetique", "no hypothetical questions"),
    ("JAMAIS dire", "no opinion giving"),
    ("JAMAIS mentionner RESPIRE", "no project name leak"),
    ("prompt injection", "anti-injection defense"),
    ("3114", "crisis hotline reference"),
    ("Donnees personnelles", "PII protection"),
    ("Depassement duree", "duration overflow handling"),
]

for keyword, label in security_checks:
    if keyword.lower() in prompt_text.lower():
        print(f"   [OK] {label}")
    else:
        errors.append(f"Missing guardrail: {label} (keyword: '{keyword}')")

# ============================================================
# 5. Check conversation history
# ============================================================
print("\n5/5 — Checking conversation history...")

try:
    conversations = client.conversational_ai.conversations.list(
        agent_id=AGENT_ID
    )
    conv_list = getattr(conversations, "conversations", [])
    if not conv_list:
        conv_list = conversations if isinstance(conversations, list) else []

    if hasattr(conv_list, "__len__"):
        count = len(conv_list)
    else:
        count = 0
        for _ in conv_list:
            count += 1

    print(f"   Total conversations: {count}")
    if count > 0:
        print("   Recent conversations:")
        for i, c in enumerate(list(conv_list)[:5]):
            cid = getattr(c, "conversation_id", getattr(c, "id", "?"))
            status = getattr(c, "status", "?")
            print(f"     {i+1}. {cid} — {status}")
except Exception as e:
    warnings.append(f"Cannot list conversations: {e}")

# ============================================================
# Summary
# ============================================================
print(f"\n{'=' * 60}")
print("VERIFICATION SUMMARY")
print(f"{'=' * 60}")
print(f"Errors:   {len(errors)}")
print(f"Warnings: {len(warnings)}")

if errors:
    print(f"\n{'!'*40}")
    print("ERRORS (must fix):")
    for e in errors:
        print(f"  [!] {e}")

if warnings:
    print(f"\n{'~'*40}")
    print("WARNINGS (review):")
    for w in warnings:
        print(f"  [~] {w}")

if not errors:
    print(f"\n{'*'*40}")
    print("AGENT IS READY FOR TESTING")
    print(f"{'*'*40}")
    print(f"\nTest URL:")
    print(f"  https://elevenlabs.io/app/conversational-ai/agents/{AGENT_ID}")
    print(f"\nWidget embed:")
    print(f'  <elevenlabs-convai agent-id="{AGENT_ID}"></elevenlabs-convai>')
    print(f'  <script src="https://unpkg.com/@elevenlabs/convai-widget-embed" async></script>')

print(f"\n{'=' * 60}")

sys.exit(1 if errors else 0)
