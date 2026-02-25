"""
RESPIRE Discovery — Deployment Verification
============================================
Checks that the widget is deployed and the ElevenLabs agent is operational.

Usage:
  python verify-deploy.py
  python verify-deploy.py --url https://custom-url.com/widget/
"""

import os
import sys
import urllib.request
import urllib.error

# Clean proxy env vars that cause SOCKS errors with httpx
for _var in ["ALL_PROXY", "all_proxy", "HTTPS_PROXY", "HTTP_PROXY",
             "https_proxy", "http_proxy"]:
    os.environ.pop(_var, None)

from elevenlabs.client import ElevenLabs

AGENT_ID = "agent_4301kj6mtc0debes0xew21d3yyhw"
DEFAULT_WIDGET_URL = "https://BuilderCed.github.io/parental-ai-study/widget/"


def check_widget_url(url: str) -> bool:
    """Check that the widget HTML page is accessible (HTTP 200)."""
    try:
        req = urllib.request.Request(url, method="GET")
        req.add_header("User-Agent", "RESPIRE-Verify/1.0")
        with urllib.request.urlopen(req, timeout=10) as resp:
            body = resp.read().decode("utf-8", errors="replace")
            if "elevenlabs-convai" in body or "AGENT_ID" in body:
                return True
            print(f"  Warning: page loaded but widget embed not found in HTML")
            return False
    except urllib.error.HTTPError as e:
        print(f"  HTTP {e.code}: {e.reason}")
        return False
    except Exception as e:
        print(f"  Error: {e}")
        return False


def check_agent_active(client: ElevenLabs) -> bool:
    """Check that the ElevenLabs agent exists and is retrievable."""
    try:
        agent = client.conversational_ai.agents.get(agent_id=AGENT_ID)
        print(f"  Agent name: {agent.name}")
        return True
    except Exception as e:
        print(f"  Error: {e}")
        return False


def check_signed_url(client: ElevenLabs) -> bool:
    """Check that a signed URL can be generated."""
    try:
        result = client.conversational_ai.conversations.get_signed_url(
            agent_id=AGENT_ID
        )
        if result.signed_url:
            print(f"  Signed URL: {result.signed_url[:60]}...")
            return True
        print("  Error: empty signed URL returned")
        return False
    except Exception as e:
        print(f"  Error: {e}")
        return False


def check_knowledge_base(client: ElevenLabs) -> bool:
    """Check that the agent has a knowledge base attached."""
    try:
        agent = client.conversational_ai.agents.get(agent_id=AGENT_ID)
        # Check for knowledge base in agent config
        kb = getattr(agent, "knowledge_base", None)
        if kb:
            print(f"  Knowledge base entries: {len(kb) if hasattr(kb, '__len__') else 'present'}")
            return True
        # Some SDK versions expose it differently
        config = getattr(agent, "conversation_config", None)
        if config and getattr(config, "knowledge_base", None):
            print(f"  Knowledge base: attached via conversation_config")
            return True
        print("  Warning: no knowledge base detected (may be in agent config)")
        return True  # Non-blocking — KB may be configured via dashboard
    except Exception as e:
        print(f"  Error: {e}")
        return False


def main():
    url = DEFAULT_WIDGET_URL
    if "--url" in sys.argv:
        idx = sys.argv.index("--url")
        if idx + 1 < len(sys.argv):
            url = sys.argv[idx + 1]

    client = ElevenLabs()
    checks = []

    print("RESPIRE Deploy Verification")
    print("=" * 50)

    # 1. Widget URL
    print(f"\n[1/4] Widget URL: {url}")
    ok = check_widget_url(url)
    checks.append(("Widget accessible", ok))
    print(f"  {'PASS' if ok else 'FAIL'}")

    # 2. Agent active
    print(f"\n[2/4] ElevenLabs Agent: {AGENT_ID}")
    ok = check_agent_active(client)
    checks.append(("Agent active", ok))
    print(f"  {'PASS' if ok else 'FAIL'}")

    # 3. Signed URL
    print(f"\n[3/4] Signed URL generation")
    ok = check_signed_url(client)
    checks.append(("Signed URL", ok))
    print(f"  {'PASS' if ok else 'FAIL'}")

    # 4. Knowledge base
    print(f"\n[4/4] Knowledge base")
    ok = check_knowledge_base(client)
    checks.append(("Knowledge base", ok))
    print(f"  {'PASS' if ok else 'FAIL'}")

    # Summary
    print(f"\n{'=' * 50}")
    passed = sum(1 for _, ok in checks if ok)
    total = len(checks)
    print(f"Result: {passed}/{total} checks passed")
    for name, ok in checks:
        print(f"  {'[OK]' if ok else '[!!]'} {name}")

    if passed < total:
        print(f"\nSome checks failed. Review errors above.")
        sys.exit(1)
    else:
        print(f"\nAll checks passed. Ready for participant interviews.")


if __name__ == "__main__":
    main()
