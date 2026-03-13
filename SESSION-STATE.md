# Session State — Etude IA & Charge Mentale Parentale

> Ce fichier est lu en debut de chaque session pour reprendre le contexte.
> Mis a jour : 23 fevrier 2026

## Resume du Projet
Etude de marche exhaustive sur l'IA appliquee a la charge mentale parentale.
Objectif : identifier le meilleur produit a construire (MVP avec Claude Code).
4 sessions planifiees, 11 livrables + rapport final.

---

## Session 1 (2026-02-23) — Research Foundation — TERMINEE

### Ce qui a ete fait
- [x] 00-framing.md — Cadrage, taxonomie, grille scoring (11K)
- [x] 01-market.md — Marche, TAM/SAM/SOM (38K, 733 lignes)
- [x] 02-competitors.md — 28 acteurs (65K, 1727 lignes)
- [x] 02b-distribution.md — Canaux distribution (62K)
- [x] 02c-niches.md — TOP 10 niches (36K)
- [x] 03-user-voice.md — 278 signaux, 20 irritants (28K)
- [x] sources-log.md — 75+ sources consolidees

### Key Insights
1. Europe croit 2x plus vite que USA
2. Retention <20% — apps resolvent 20% du probleme
3. RGPD/AI Act = moat 12-18 mois EU
4. Gap : anticipation IA + visibilite charge + equite couple
5. Killer feature : "Anticipation view"
6. WhatsApp/SMS = gap distribution inexploite
7. B2B2C sante surperforme B2C

---

## Session 2 (2026-02-23) — Analyse Approfondie — TERMINEE

### Ce qui a ete fait
- [x] 04-personas.md — 4 MVP + 3 secondaires (65K, 1316 lignes)
- [x] 05-irritants-opportunities.md — 20 irritants mappes (92K, 2203 lignes)
- [x] 06-legal-ethics.md — RGPD, DPIA, AI Act (42K, 869 lignes)
- [x] 07-brand-psychology.md — Archetypes, naming, risques (51K, 1307 lignes)

### Key Insights Session 2
- Personas MVP : Sophie (couple CSP+), Karim (pere), Nadia (solo) = 65% TAM
- Nom recommande : RESPIRE ("Pour que tu ne penses pas a tout")
- Archetype : EVERYMAN + SAGE
- DPIA obligatoire, budget 8-14K€ compliance
- Top feature MVP : Anticipation View + Meal Planning + Task Visibility

---

## Session 3 (2026-02-23) — Strategie Produit — TERMINEE

### Ce qui a ete fait
- [x] 08-top3-ideas.md — TOP 3 scorees (strategy/, Opus)
  - #1 RESPIRE Weekly (9.00/10) — Bot WhatsApp anticipation
  - #2 RESPIRE Couple (7.70/10) — Dashboard equite couple
  - #3 RESPIRE Solo (7.35/10) — Co-pilote parent solo
- [x] 09-mvp-blueprint.md — Blueprint complet (767 lignes, Opus)

---

## Session 4 (2026-02-23) — Consolidation Finale — TERMINEE

### Ce qui a ete fait
- [x] RAPPORT-FINAL.md — 1004 lignes, 48K, 13 sections + annexes (Opus)
- [x] kb/glossary.md — 50 termes (Sonnet)
- [x] kb/taxonomy.md — Taxonomie complete (Sonnet)
- [x] kb/competitors-table.md — 28 acteurs (Sonnet)
- [x] AUDIT-REPORT.md — Score 82/100, CONDITIONAL GO (Opus)
- [x] Corrections post-audit : scoring arithmetique, sprint count, sources-log, numerotation

## ETUDE TERMINEE — Score qualite : 82/100 → 86+/100 (post-corrections)

---

## Prochaine Etape : MVP RESPIRE Weekly

### Produit
- **Nom** : RESPIRE Weekly
- **Score** : 9.00/10
- **Format** : Bot WhatsApp IA d'anticipation hebdomadaire
- **Tagline** : "Pour que tu ne penses pas a tout"

### Stack technique (09-mvp-blueprint.md)
- Node.js 22+ / Hono (API)
- PostgreSQL Neon EU / Drizzle ORM
- Claude Haiku 4.5 ($1/$5 per M tokens)
- WhatsApp Cloud API (canal principal)
- BullMQ / Upstash Redis EU (jobs)
- Next.js 15 / Vercel EU (dashboard admin)
- PostHog EU (analytics)
- Scaleway Paris (hosting)

### Sprints
- **S0** (72h) : Setup technique, infra, CI
- **S1** (7j) : Onboarding + briefing v1
- **S2** (7j) : Personnalisation + rappels quotidiens
- **S3** (14j) : Beta privee 20-30 testeurs

### Budget
- Infrastructure : 48-165 EUR/3 mois
- APIs : ~35 EUR/3 mois
- Legal/RGPD : 3 500-5 000 EUR
- Dev freelance senior : 8-12K EUR
- **Total : 12-17K EUR**

### Metriques go/no-go
- Activation >= 70% (1x/semaine)
- Ouverture briefing >= 80%
- NPS >= 40
- Retention M1 >= 60%

### Fichiers cles pour le dev
- `strategy/09-mvp-blueprint.md` — Blueprint complet (767 lignes)
- `strategy/08-top3-ideas.md` — Scoring + specs produit
- `research/06-legal-ethics.md` — RGPD checklist
- `RAPPORT-FINAL.md` — Vue consolidee

---

## Chemin Projet
`/Users/cquadjovie/Developer/Active/Business 0/parental-ai-study/`

## Memory Reference
`~/.claude/projects/-/memory/parental-ai-study.md`
