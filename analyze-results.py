"""
RESPIRE Discovery Agent — Results Analysis
============================================
Analyse les conversations exportees et genere un rapport statistique.
Charge data/conversations.json, agrege les donnees, genere data/analysis-report.md.

Usage:
  python analyze-results.py
"""

import os
import sys
import json
from datetime import datetime, timezone
from collections import Counter

DATA_DIR = os.path.join(os.path.dirname(__file__), "data")
INPUT_FILE = os.path.join(DATA_DIR, "conversations.json")
OUTPUT_FILE = os.path.join(DATA_DIR, "analysis-report.md")


def load_conversations():
    if not os.path.exists(INPUT_FILE):
        print(f"Error: {INPUT_FILE} not found.")
        print("Run export-conversations.py first.")
        sys.exit(1)

    with open(INPUT_FILE) as f:
        data = json.load(f)
    return data.get("conversations", [])


def extract_data_collection(conv):
    """Extract data collection fields from analysis."""
    analysis = conv.get("analysis") or {}
    dc = analysis.get("data_collection_results") or analysis.get("data_collection") or {}
    if isinstance(dc, dict):
        result = {}
        for k, v in dc.items():
            if isinstance(v, dict):
                result[k] = v.get("value")
            else:
                result[k] = v
        return result
    return {}


def compute_hypothesis_rates(conversations):
    """Compute validation rate for each hypothesis H1-H5."""
    hypotheses = {f"h{i}_validated": {"yes": 0, "no": 0, "unknown": 0} for i in range(1, 6)}

    for conv in conversations:
        dc = extract_data_collection(conv)
        for h_key in hypotheses:
            val = dc.get(h_key)
            if val is True or val == "true" or val == "True":
                hypotheses[h_key]["yes"] += 1
            elif val is False or val == "false" or val == "False":
                hypotheses[h_key]["no"] += 1
            else:
                hypotheses[h_key]["unknown"] += 1

    return hypotheses


def compute_numeric_stats(values):
    """Compute min, max, avg, median for a list of numbers."""
    if not values:
        return {"min": 0, "max": 0, "avg": 0, "median": 0, "count": 0}

    values = sorted(values)
    n = len(values)
    return {
        "min": values[0],
        "max": values[-1],
        "avg": round(sum(values) / n, 1),
        "median": values[n // 2] if n % 2 else round((values[n // 2 - 1] + values[n // 2]) / 2, 1),
        "count": n,
    }


def generate_report(conversations):
    """Generate the full analysis report."""
    total = len(conversations)
    if total == 0:
        return "# Rapport d'Analyse RESPIRE\n\nAucune conversation a analyser."

    # Extract all data
    all_dc = [extract_data_collection(c) for c in conversations]

    # Hypothesis validation
    h_rates = compute_hypothesis_rates(conversations)

    # Numeric aggregations
    charge_scores = [dc["charge_mentale_score"] for dc in all_dc
                     if dc.get("charge_mentale_score") is not None
                     and isinstance(dc["charge_mentale_score"], (int, float))]
    wtp_values = [dc["willingness_to_pay"] for dc in all_dc
                  if dc.get("willingness_to_pay") is not None
                  and isinstance(dc["willingness_to_pay"], (int, float))]
    depense_values = [dc["depense_temps_mensuelle"] for dc in all_dc
                      if dc.get("depense_temps_mensuelle") is not None
                      and isinstance(dc["depense_temps_mensuelle"], (int, float))]
    enfants_count = [dc["nombre_enfants"] for dc in all_dc
                     if dc.get("nombre_enfants") is not None
                     and isinstance(dc["nombre_enfants"], (int, float))]

    # Categorical aggregations
    irritants = Counter(dc.get("top_irritant", "").strip()
                        for dc in all_dc if dc.get("top_irritant"))
    situations = Counter(dc.get("situation_couple", "").strip()
                         for dc in all_dc if dc.get("situation_couple"))
    apps = Counter()
    for dc in all_dc:
        raw = dc.get("apps_essayees", "")
        if raw:
            for app in str(raw).split(","):
                app = app.strip()
                if app:
                    apps[app] += 1

    # Boolean rates
    def bool_rate(field):
        t = sum(1 for dc in all_dc if dc.get(field) in (True, "true", "True"))
        f = sum(1 for dc in all_dc if dc.get(field) in (False, "false", "False"))
        total_known = t + f
        return (t, total_known)

    ia_usage = bool_rate("usage_ia_famille")
    wa_actif = bool_rate("whatsapp_actif")
    opt_in = bool_rate("opt_in_beta")

    # Verbatims
    abandons = [dc.get("raison_abandon_app", "")
                for dc in all_dc if dc.get("raison_abandon_app")]

    # Transcript stats
    turn_counts = [len(c.get("transcript", [])) for c in conversations]

    # Build report
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    charge_stats = compute_numeric_stats(charge_scores)
    wtp_stats = compute_numeric_stats(wtp_values)
    depense_stats = compute_numeric_stats(depense_values)

    lines = [
        f"# Rapport d'Analyse RESPIRE Discovery",
        f"",
        f"> Genere le {now} — {total} conversations analysees",
        f"",
        f"---",
        f"",
        f"## 1. Validation des Hypotheses",
        f"",
        f"| Hypothese | Description | Valide | Non valide | Inconnu | Taux |",
        f"|-----------|-------------|--------|------------|---------|------|",
    ]

    h_labels = {
        "h1_validated": "H1 — Anticipation = pain #1",
        "h2_validated": "H2 — Asymetrie couple",
        "h3_validated": "H3 — Apps ne resolvent pas",
        "h4_validated": "H4 — WhatsApp canal pertinent",
        "h5_validated": "H5 — Willingness to pay",
    }

    for key, label in h_labels.items():
        data = h_rates[key]
        known = data["yes"] + data["no"]
        rate = f"{data['yes']}/{known}" if known > 0 else "N/A"
        pct = f"({round(data['yes']/known*100)}%)" if known > 0 else ""
        lines.append(f"| {label} | {data['yes']} | {data['no']} | {data['unknown']} | {rate} {pct} |")

    lines.extend([
        f"",
        f"## 2. Profil des Participants",
        f"",
        f"- **Nombre total**: {total} conversations",
        f"- **Turns moyen**: {compute_numeric_stats(turn_counts)['avg']} exchanges/conversation",
        f"- **Enfants**: avg {compute_numeric_stats(enfants_count)['avg']}, "
        f"median {compute_numeric_stats(enfants_count)['median']}",
        f"",
        f"### Situation familiale",
        f"",
    ])
    for situation, count in situations.most_common():
        lines.append(f"- {situation}: {count} ({round(count/total*100)}%)")

    lines.extend([
        f"",
        f"## 3. Charge Mentale",
        f"",
        f"- **Score moyen**: {charge_stats['avg']}/10",
        f"- **Median**: {charge_stats['median']}/10",
        f"- **Min/Max**: {charge_stats['min']} — {charge_stats['max']}",
        f"- **Repondants**: {charge_stats['count']}/{total}",
        f"",
        f"### Top Irritants",
        f"",
    ])
    for irritant, count in irritants.most_common(10):
        lines.append(f"1. **{irritant}** — {count} mentions")

    lines.extend([
        f"",
        f"## 4. Solutions Actuelles",
        f"",
        f"### Apps essayees",
        f"",
    ])
    for app, count in apps.most_common(10):
        lines.append(f"- {app}: {count} mentions")

    lines.extend([
        f"",
        f"### Raisons d'abandon",
        f"",
    ])
    for i, raison in enumerate(abandons[:10], 1):
        lines.append(f'{i}. "{raison}"')

    lines.extend([
        f"",
        f"### Usage IA famille",
        f"",
        f"- Utilise ChatGPT/IA: {ia_usage[0]}/{ia_usage[1]} "
        f"({round(ia_usage[0]/ia_usage[1]*100) if ia_usage[1] else 0}%)",
        f"- WhatsApp actif: {wa_actif[0]}/{wa_actif[1]} "
        f"({round(wa_actif[0]/wa_actif[1]*100) if wa_actif[1] else 0}%)",
        f"",
        f"## 5. Valeur & Paiement",
        f"",
        f"### Depense actuelle (gagner du temps)",
        f"",
        f"- **Moyenne**: {depense_stats['avg']} EUR/mois",
        f"- **Median**: {depense_stats['median']} EUR/mois",
        f"- **Min/Max**: {depense_stats['min']} — {depense_stats['max']} EUR",
        f"",
        f"### Willingness to Pay",
        f"",
        f"- **Moyenne**: {wtp_stats['avg']} EUR/mois",
        f"- **Median**: {wtp_stats['median']} EUR/mois",
        f"- **Min/Max**: {wtp_stats['min']} — {wtp_stats['max']} EUR",
        f"",
        f"## 6. Opt-in Beta",
        f"",
        f"- Accepte de tester: {opt_in[0]}/{opt_in[1]} "
        f"({round(opt_in[0]/opt_in[1]*100) if opt_in[1] else 0}%)",
        f"",
        f"---",
        f"",
        f"*Rapport genere automatiquement par analyze-results.py*",
    ])

    return "\n".join(lines)


def main():
    print(f"{'='*60}")
    print("RESPIRE Discovery — Results Analysis")
    print(f"{'='*60}")

    conversations = load_conversations()
    print(f"\nLoaded {len(conversations)} conversations from {INPUT_FILE}")

    report = generate_report(conversations)

    os.makedirs(DATA_DIR, exist_ok=True)
    with open(OUTPUT_FILE, "w") as f:
        f.write(report)

    print(f"\nReport saved to {OUTPUT_FILE}")
    print(f"\n{report}")


if __name__ == "__main__":
    main()
