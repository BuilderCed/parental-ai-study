"""
RESPIRE Discovery Agent — Configuration dashboard
==================================================
Applique tous les settings recommandes via API.
Inclut: turn-taking, ASR, TTS, privacy, dynamic variables.
Pre-requis: agent deja cree (create-agent.py)

Usage:
  python configure-agent.py
"""

import os
from elevenlabs.client import ElevenLabs

AGENT_ID = "agent_4301kj6mtc0debes0xew21d3yyhw"

client = ElevenLabs()

# --- 1. Update conversation_config (turn-taking, TTS, ASR) ---
print("1/5 — Configuring turn-taking & ASR...")

client.conversational_ai.agents.update(
    agent_id=AGENT_ID,
    conversation_config={
        "turn": {
            "mode": "turn",
            "turn_timeout": 20,
            "turn_eagerness": "patient",
            "speculative_turn": False,
            "soft_timeout_config": {
                "timeout_seconds": 3.0,
                "message": "Hmm... je vois.",
                "use_llm_generated_message": False,
            },
        },
        "tts": {
            "model_id": "eleven_turbo_v2_5",
            "voice_id": "d3AXX0BlgJHYFCuH9X88",  # Emilie - French (France) podcast host
            "stability": 0.5,
            "similarity_boost": 0.8,
            "optimize_streaming_latency": 3,
            "speed": 0.95,
        },
        "asr": {
            "quality": "high",
            "language": "fr",
            "keywords": [
                "charge mentale",
                "anticipation",
                "fallait demander",
                "la charge",
                "en charge",
                "mental charge",
                "WhatsApp",
                "Cozi",
                "FamilyWall",
                "Google Agenda",
                "babysitter",
                "periscolaire",
                "cantine",
                "pediatre",
                "batch cooking",
                "ChatGPT",
                "burnout",
                "epuisement",
            ],
        },
        "conversation": {
            "max_duration_seconds": 1500,  # 25 min hard cap
            "client_events": [
                "audio",
                "interruption",
                "agent_response",
                "user_transcript",
                "agent_response_correction",
            ],
        },
    },
)
print("   Turn eagerness: PATIENT")
print("   Soft timeout: 3.0s 'Hmm... je vois.'")
print("   ASR keywords: 18 termes cles (+ variantes charge mentale)")
print("   ASR language: fr")
print("   Max duration: 25 min")
print("   TTS speed: 0.95x (legere lenteur naturelle)")

# --- 2. Platform settings (privacy, security, call limits) ---
print("\n2/5 — Configuring platform settings (privacy & security)...")

client.conversational_ai.agents.update(
    agent_id=AGENT_ID,
    platform_settings={
        "privacy": {
            "record_conversation": True,
            "retention_days": 30,
        },
        "call_limits": {
            "max_call_duration_secs": 1500,
            "max_concurrent_calls": 5,
        },
    },
)
print("   Recording: ON (transcripts pour analyse)")
print("   Retention: 30 jours (RGPD)")
print("   Max duration: 25 min")
print("   Max concurrent: 5 calls")

# --- 3. Dynamic variables for participant tracking ---
print("\n3/5 — Configuring dynamic variables...")

client.conversational_ai.agents.update(
    agent_id=AGENT_ID,
    conversation_config={
        "agent": {
            "dynamic_variables": {
                "dynamic_variable_config": [
                    {
                        "name": "prenom",
                        "label": "Prenom du participant",
                        "default_value": "",
                        "type": "string",
                    },
                    {
                        "name": "user_id",
                        "label": "ID unique du participant",
                        "default_value": "",
                        "type": "string",
                    },
                ],
            },
        },
    },
)
print("   Dynamic vars: prenom, user_id")
print("   Usage: passe via widget dynamic-variables ou signed URL")

# --- 4. Data collection fields ---
print("\n4/5 — Note: Data Collection fields must be configured in dashboard:")
print("   Go to: https://elevenlabs.io/app/conversational-ai")
print(f"   Agent: Camille — RESPIRE Discovery ({AGENT_ID})")
print("   Section: Agent Analysis > Data Collection")
print("   Add these fields:")

DATA_FIELDS = [
    ("nombre_enfants", "number", "Nombre d'enfants du parent"),
    ("ages_enfants", "string", "Ages des enfants (ex: '3 ans et 6 ans')"),
    ("situation_couple", "string", "couple / solo / recompose"),
    ("charge_mentale_score", "number", "Score charge mentale 1-10 (infere)"),
    ("top_irritant", "string", "Principal irritant cite"),
    ("apps_essayees", "string", "Apps famille essayees (Cozi, etc.)"),
    ("raison_abandon_app", "string", "Pourquoi abandonne (LA question cle)"),
    ("usage_ia_famille", "boolean", "Utilise ChatGPT/IA pour famille"),
    ("whatsapp_actif", "boolean", "Utilise WhatsApp activement"),
    ("groupes_whatsapp_count", "number", "Nombre de groupes WhatsApp famille"),
    ("depense_temps_mensuelle", "number", "EUR/mois pour gagner du temps"),
    ("willingness_to_pay", "number", "EUR/mois acceptable pour service"),
    ("referrals", "string", "Noms/contacts suggeres"),
    ("opt_in_beta", "boolean", "Accepte de tester le MVP"),
    ("h1_validated", "boolean", "H1 anticipation = pain #1"),
    ("h2_validated", "boolean", "H2 asymetrie couple"),
    ("h3_validated", "boolean", "H3 apps ne resolvent pas"),
    ("h4_validated", "boolean", "H4 WhatsApp canal pertinent"),
    ("h5_validated", "boolean", "H5 willingness to pay"),
]

for name, dtype, desc in DATA_FIELDS:
    print(f"   - {name} ({dtype}) — {desc}")

# --- 5. Summary ---
print(f"\n5/5 — Configuration complete!")
print(f"\n{'='*60}")
print(f"AGENT ID          : {AGENT_ID}")
print(f"TURN EAGERNESS    : PATIENT (attendre reflexion)")
print(f"SOFT TIMEOUT      : 3.0s → 'Hmm... je vois.'")
print(f"ASR KEYWORDS      : 18 termes FR (charge mentale + variantes)")
print(f"TTS SPEED         : 0.95x (naturel)")
print(f"PRIVACY           : Record ON, 30 jours retention")
print(f"MAX DURATION      : 25 min (hard cap)")
print(f"MAX CONCURRENT    : 5 calls")
print(f"DYNAMIC VARS      : prenom, user_id")
print(f"DATA COLLECTION   : 19 fields (5 hypotheses tracking)")
print(f"{'='*60}")
print(f"\nWidget embed code (avec dynamic variables):")
print(f'  <elevenlabs-convai agent-id="{AGENT_ID}"')
print(f"    dynamic-variables='{{\"user_id\":\"P001\",\"prenom\":\"Marie\"}}'")
print(f"  ></elevenlabs-convai>")
print(f'  <script src="https://unpkg.com/@elevenlabs/convai-widget-embed" async></script>')
print(f"\nTest URL:")
print(f"  https://elevenlabs.io/app/conversational-ai/agents/{AGENT_ID}")
print(f"\nGenerate participant links:")
print(f"  python generate-link.py P001 Marie")
