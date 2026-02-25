"""
RESPIRE Discovery Agent — Participant Link Generator
=====================================================
Genere un signed URL unique par participant pour l'interview.
Le lien ouvre une page web avec le widget ElevenLabs embede.

Usage:
  python generate-link.py P001 Marie
  python generate-link.py P002 "Jean-Pierre"
  python generate-link.py --list         # Liste les liens generes
  python generate-link.py --batch file.csv  # Batch depuis CSV (user_id,prenom)
"""

import os
import sys
import csv
import json
import hashlib
from datetime import datetime, timezone

from elevenlabs.client import ElevenLabs

# Clean proxy env vars that cause SOCKS errors with httpx
for _var in ["ALL_PROXY", "all_proxy", "HTTPS_PROXY", "HTTP_PROXY",
             "https_proxy", "http_proxy"]:
    os.environ.pop(_var, None)

AGENT_ID = "agent_4301kj6mtc0debes0xew21d3yyhw"
WIDGET_BASE_URL = os.environ.get(
    "RESPIRE_WIDGET_URL",
    "https://BuilderCed.github.io/parental-ai-study/widget/"
)
DATA_DIR = os.path.join(os.path.dirname(__file__), "data")
LINKS_FILE = os.path.join(DATA_DIR, "participant-links.json")

client = ElevenLabs()


def load_links():
    if os.path.exists(LINKS_FILE):
        with open(LINKS_FILE) as f:
            return json.load(f)
    return []


def save_links(links):
    os.makedirs(DATA_DIR, exist_ok=True)
    with open(LINKS_FILE, "w") as f:
        json.dump(links, f, indent=2, ensure_ascii=False)


def _make_nonce(user_id: str) -> str:
    """Generate a short nonce from user_id + timestamp (no PII)."""
    raw = f"{user_id}:{datetime.now(timezone.utc).isoformat()}"
    return hashlib.sha256(raw.encode()).hexdigest()[:12]


def generate_link(user_id: str, prenom: str):
    print(f"Generating signed URL for {prenom} ({user_id})...")

    result = client.conversational_ai.conversations.get_signed_url(
        agent_id=AGENT_ID,
        include_conversation_id=True,
    )

    signed_url = result.signed_url
    nonce = _make_nonce(user_id)

    if WIDGET_BASE_URL:
        base = WIDGET_BASE_URL.rstrip("/")
        participant_url = (
            f"{base}/?participant={user_id}&name={prenom}&nonce={nonce}"
        )
    else:
        participant_url = None

    entry = {
        "user_id": user_id,
        "prenom": prenom,
        "signed_url": signed_url,
        "widget_url": participant_url,
        "generated_at": datetime.now(timezone.utc).isoformat(),
    }

    links = load_links()
    links.append(entry)
    save_links(links)

    print(f"\n{'='*60}")
    print(f"PARTICIPANT : {prenom} ({user_id})")
    print(f"SIGNED URL  : {signed_url}")
    if participant_url:
        print(f"WIDGET URL  : {participant_url}")
    print(f"GENERATED   : {entry['generated_at']}")
    print(f"{'='*60}")

    print(f"\nWidget embed (avec dynamic variables):")
    print(f'  <elevenlabs-convai agent-id="{AGENT_ID}"')
    print(f"    dynamic-variables='{{\"user_id\":\"{user_id}\",\"prenom\":\"{prenom}\"}}'")
    print(f"  ></elevenlabs-convai>")

    if not WIDGET_BASE_URL:
        print(f"\nNote: Definir RESPIRE_WIDGET_URL pour generer des liens widget.")
        print(f"  export RESPIRE_WIDGET_URL='https://your-site.com/interview'")

    return entry


def list_links():
    links = load_links()
    if not links:
        print("Aucun lien genere.")
        return

    print(f"{'='*60}")
    print(f"LIENS GENERES ({len(links)} participants)")
    print(f"{'='*60}")
    for link in links:
        print(f"\n  {link['prenom']} ({link['user_id']})")
        print(f"    Genere: {link['generated_at']}")
        if link.get("widget_url"):
            print(f"    URL: {link['widget_url']}")


def batch_generate(csv_path: str):
    """Generate links for all participants in a CSV file (columns: user_id,prenom)."""
    if not os.path.exists(csv_path):
        print(f"Error: fichier '{csv_path}' introuvable.")
        sys.exit(1)

    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    if not rows:
        print("CSV vide.")
        return

    required = {"user_id", "prenom"}
    if not required.issubset(set(reader.fieldnames or [])):
        print(f"Error: colonnes requises: {required}. Trouvees: {reader.fieldnames}")
        sys.exit(1)

    print(f"Generating {len(rows)} links from {csv_path}...\n")
    for row in rows:
        generate_link(row["user_id"].strip(), row["prenom"].strip())
        print()


def main():
    if len(sys.argv) < 2:
        print("Usage: python generate-link.py <user_id> <prenom>")
        print("       python generate-link.py --list")
        print("       python generate-link.py --batch participants.csv")
        sys.exit(1)

    if sys.argv[1] == "--list":
        list_links()
        return

    if sys.argv[1] == "--batch":
        if len(sys.argv) < 3:
            print("Error: chemin CSV requis.")
            print("Usage: python generate-link.py --batch participants.csv")
            sys.exit(1)
        batch_generate(sys.argv[2])
        return

    if len(sys.argv) < 3:
        print("Error: prenom requis.")
        print("Usage: python generate-link.py P001 Marie")
        sys.exit(1)

    user_id = sys.argv[1]
    prenom = sys.argv[2]
    generate_link(user_id, prenom)


if __name__ == "__main__":
    main()
