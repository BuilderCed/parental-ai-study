"""
RESPIRE Discovery Agent — Conversation Export
==============================================
Exporte toutes les conversations de l'agent vers un fichier JSON centralise.
Inclut: transcripts, metadata, analysis, data collection.

Usage:
  python export-conversations.py
  python export-conversations.py --csv     # Export aussi en CSV
  python export-conversations.py --user P001  # Filtrer par user_id
"""

import os
import sys
import json
import csv
from datetime import datetime, timezone

from elevenlabs.client import ElevenLabs

# Clean proxy env vars that cause SOCKS errors with httpx
for _var in ["ALL_PROXY", "all_proxy", "HTTPS_PROXY", "HTTP_PROXY",
             "https_proxy", "http_proxy"]:
    os.environ.pop(_var, None)

AGENT_ID = "agent_4301kj6mtc0debes0xew21d3yyhw"
DATA_DIR = os.path.join(os.path.dirname(__file__), "data")
OUTPUT_JSON = os.path.join(DATA_DIR, "conversations.json")
OUTPUT_CSV = os.path.join(DATA_DIR, "conversations.csv")

client = ElevenLabs()


def serialize(obj):
    """Recursively convert pydantic models and objects to dicts."""
    if hasattr(obj, "model_dump"):
        return obj.model_dump()
    if hasattr(obj, "__dict__"):
        return {k: serialize(v) for k, v in obj.__dict__.items() if not k.startswith("_")}
    if isinstance(obj, list):
        return [serialize(i) for i in obj]
    if isinstance(obj, dict):
        return {k: serialize(v) for k, v in obj.items()}
    return obj


def fetch_all_conversations(user_id_filter=None):
    """Fetch all conversations with pagination."""
    all_convs = []
    cursor = None

    while True:
        kwargs = {"agent_id": AGENT_ID, "page_size": 100}
        if cursor:
            kwargs["cursor"] = cursor
        if user_id_filter:
            kwargs["user_id"] = user_id_filter

        page = client.conversational_ai.conversations.list(**kwargs)
        all_convs.extend(page.conversations)

        if not page.has_more or not page.next_cursor:
            break
        cursor = page.next_cursor

    return all_convs


def fetch_conversation_detail(conversation_id):
    """Fetch full detail for a single conversation."""
    return client.conversational_ai.conversations.get(conversation_id)


def export_conversations(user_id_filter=None, include_csv=False):
    os.makedirs(DATA_DIR, exist_ok=True)

    print(f"{'='*60}")
    print("RESPIRE Discovery — Conversation Export")
    print(f"{'='*60}")

    # 1. List conversations
    print("\n1/3 — Fetching conversation list...")
    summaries = fetch_all_conversations(user_id_filter)
    print(f"   Found {len(summaries)} conversations")

    if not summaries:
        print("   No conversations to export.")
        return

    # 2. Fetch details
    print("\n2/3 — Fetching conversation details...")
    conversations = []

    for i, summary in enumerate(summaries, 1):
        conv_id = getattr(summary, "conversation_id", getattr(summary, "id", None))
        if not conv_id:
            continue

        print(f"   [{i}/{len(summaries)}] {conv_id}...")
        try:
            detail = fetch_conversation_detail(conv_id)

            transcript = []
            for msg in detail.transcript:
                transcript.append({
                    "role": getattr(msg, "role", "unknown"),
                    "message": getattr(msg, "message", ""),
                    "time_in_call_secs": getattr(msg, "time_in_call_secs", None),
                })

            analysis_data = None
            if detail.analysis:
                analysis_data = serialize(detail.analysis)

            metadata_data = None
            if detail.metadata:
                metadata_data = serialize(detail.metadata)

            conversations.append({
                "conversation_id": detail.conversation_id,
                "agent_id": detail.agent_id,
                "user_id": detail.user_id,
                "status": str(detail.status),
                "transcript": transcript,
                "analysis": analysis_data,
                "metadata": metadata_data,
                "has_audio": detail.has_audio,
                "exported_at": datetime.now(timezone.utc).isoformat(),
            })
        except Exception as e:
            print(f"   [!] Error fetching {conv_id}: {e}")

    # 3. Save
    print(f"\n3/3 — Saving exports...")

    with open(OUTPUT_JSON, "w") as f:
        json.dump({
            "agent_id": AGENT_ID,
            "export_date": datetime.now(timezone.utc).isoformat(),
            "total_conversations": len(conversations),
            "conversations": conversations,
        }, f, indent=2, ensure_ascii=False)
    print(f"   JSON: {OUTPUT_JSON} ({len(conversations)} conversations)")

    if include_csv:
        _export_csv(conversations)
        print(f"   CSV:  {OUTPUT_CSV}")

    # Summary
    print(f"\n{'='*60}")
    print("EXPORT SUMMARY")
    print(f"{'='*60}")
    print(f"  Total: {len(conversations)} conversations")

    statuses = {}
    for c in conversations:
        s = c["status"]
        statuses[s] = statuses.get(s, 0) + 1
    for status, count in sorted(statuses.items()):
        print(f"  {status}: {count}")

    users = set(c["user_id"] for c in conversations if c.get("user_id"))
    if users:
        print(f"  Participants: {', '.join(sorted(users))}")

    print(f"\n  Output: {OUTPUT_JSON}")


def _export_csv(conversations):
    """Export flat CSV with key data collection fields."""
    DATA_FIELDS = [
        "nombre_enfants", "ages_enfants", "situation_couple",
        "charge_mentale_score", "top_irritant", "apps_essayees",
        "raison_abandon_app", "usage_ia_famille", "whatsapp_actif",
        "groupes_whatsapp_count", "depense_temps_mensuelle",
        "willingness_to_pay", "referrals", "opt_in_beta",
        "h1_validated", "h2_validated", "h3_validated",
        "h4_validated", "h5_validated",
    ]

    headers = ["conversation_id", "user_id", "status", "turns"] + DATA_FIELDS

    with open(OUTPUT_CSV, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()

        for conv in conversations:
            row = {
                "conversation_id": conv["conversation_id"],
                "user_id": conv.get("user_id", ""),
                "status": conv["status"],
                "turns": len(conv.get("transcript", [])),
            }

            analysis = conv.get("analysis") or {}
            # API returns data_collection_results (Dict[str, {value, rationale}])
            dc = analysis.get("data_collection_results") or analysis.get("data_collection") or {}
            if isinstance(dc, dict):
                for field in DATA_FIELDS:
                    val = dc.get(field)
                    if isinstance(val, dict):
                        val = val.get("value", "")
                    row[field] = val if val is not None else ""

            writer.writerow(row)


def main():
    user_filter = None
    include_csv = "--csv" in sys.argv

    for arg in sys.argv[1:]:
        if arg.startswith("--user="):
            user_filter = arg.split("=", 1)[1]
        elif arg == "--user" and sys.argv.index(arg) + 1 < len(sys.argv):
            user_filter = sys.argv[sys.argv.index(arg) + 1]

    export_conversations(user_id_filter=user_filter, include_csv=include_csv)


if __name__ == "__main__":
    main()
