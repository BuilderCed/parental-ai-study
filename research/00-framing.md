# 00 — Cadrage : IA & Charge Mentale Parentale

> Synthese des recherches Phase 1 (01-market, 02-competitors, 03-user-voice)
> Date : 23 fevrier 2026

---

## 1. Definition : Charge Mentale Parentale

La charge mentale parentale est le **travail cognitif et emotionnel invisible** de gestion du quotidien familial. Elle depasse largement les taches visibles (menage, courses) pour inclure :

- **L'anticipation** : penser en avance aux besoins (RDV, vetements saison, permissions ecole)
- **La coordination** : synchroniser les emplois du temps de chaque membre
- **La decision** : arbitrer en permanence (repas, activites, priorites)
- **Le suivi** : verifier que les taches sont faites, relancer si necessaire
- **La charge emotionnelle** : gerer les emotions de chacun, consoler, motiver

**Donnee cle** : 71% des meres portent la charge mentale vs 29% des peres. Mais 65% des peres pensent que le partage est equitable — un ecart de perception massif qui alimente les frictions de couple.

---

## 2. Taxonomie des Taches Parentales

### 2.1 Taches Visibles (~20% du poids reel)

| Categorie | Exemples | Frequence |
|-----------|----------|-----------|
| **Domestique** | Menage, lessive, vaisselle, rangement | Quotidien |
| **Repas** | Cuisiner, mettre la table, debarrasser | 3x/jour |
| **Transport** | Emmener/chercher ecole, activites | Quotidien |
| **Hygiene enfants** | Bain, habillage, brossage dents | Quotidien |

### 2.2 Taches Invisibles (~80% du poids reel)

| Categorie | Exemples | Frequence | Difficulte delegation |
|-----------|----------|-----------|----------------------|
| **Anticipation** | RDV medicaux, fournitures, vetements saison, anniversaires | Continue | Tres elevee |
| **Planification repas** | Menus semaine, courses, stock frigo, regimes | Hebdomadaire | Elevee |
| **Admin scolaire** | Permissions, inscriptions, suivi devoirs, communication prof | Variable | Moyenne |
| **Admin sante** | Carnet vaccins, ordonnances, suivi specialistes | Mensuel | Elevee |
| **Coordination couple** | Qui fait quoi, quand, relances, negociation | Continue | Tres elevee |
| **Charge emotionnelle** | Consoler, ecouter, gerer conflits fratrie, soutenir | Continue | Non-delegable (partiellement) |
| **Logistique activites** | Inscription, horaires, covoiturage, equipement | Hebdomadaire | Moyenne |
| **Anticipation saisonniere** | Vacances, changement vetements, rentree | Trimestriel | Elevee |

### 2.3 Niveaux d'Autonomie IA Possibles

| Niveau | Description | Exemples concrets |
|--------|-------------|-------------------|
| **0 — Aucun** | Parent fait tout manuellement | Status quo actuel |
| **1 — Suggest** | IA suggere, parent decide et execute | "Semaine chargee : voici 5 menus rapides" |
| **2 — Draft** | IA prepare, parent valide | Liste courses generee, parent modifie et valide |
| **3 — Execute** | IA agit, parent supervise | RDV pris automatiquement, parent confirme |
| **4 — Autonome** | IA gere, parent informe | Renouvellement ordonnance automatique + notification |

**Contrat d'autonomie recommande (MVP)** : Niveaux 1-2 pour commencer (suggest/draft). Niveau 3 uniquement apres confiance etablie (opt-in explicite). Niveau 4 hors scope MVP (risque RGPD, confiance).

---

## 3. Synthese Marche

### 3.1 Chiffres cles

| Indicateur | Valeur | Source |
|------------|--------|--------|
| TAM global parenting apps | $1.7-4.7B (2024) | Coherent MI, Business Research Insights |
| TAM AI in childcare | $4.7B → $35.2B (2034) | InsightAce Analytic |
| CAGR | 20-22% (2024-2032) | Multiples sources |
| Europe part de marche | 29% (~$308-489M) | Root Analysis |
| France estime | $25-60M (2024) | Interpolation rapports |
| Retention moyenne apps parentales | <20% annuel | Analyse taux abandon |
| Taux abandon Cozi | 70% a 3 mois | Avis utilisateurs |

### 3.2 Tendances structurantes

1. **Europe croit 2x plus vite que USA** (+18-22% vs +12-15%) — fenetre d'opportunite EU
2. **IA est table-stakes** : 42% des leaders deploient l'IA — expertise domaine = seul moat
3. **RGPD/AI Act (2025-2027)** = avantage competitif 12-18 mois pour startups EU privacy-native
4. **App fatigue severe** : parents utilisent 5-7 apps, veulent consolidation
5. **B2B2C via sante** : LTV superieur au B2C direct (May, Huckleberry)
6. **Async > Sync** : features asynchrones (calendrier, listes) gagnent vs synchrones
7. **Consolidation inevitable** : trop d'acteurs similaires en Tier 1, les gros absorberont

### 3.3 Paysage concurrentiel (28 acteurs analyses)

| Tier | Categorie | Acteurs cles | Saturation |
|------|-----------|-------------|------------|
| 1 | Family Organizers | Cozi, FamilyWall, TimeTree, ClanPlan | **Haute** |
| 2 | Parenting/Dev Tracking | Kinedu, BabyCenter, Huckleberry, May | Moyenne |
| 3 | AI Assistants generalistes | ChatGPT, Gemini, Claude, Alexa | Haute (mais pas specialises) |
| 4 | IA-First Familles | May, TinyPal, Ollie | **Faible** (emergent) |
| 5 | Outils adjacents | Todoist, Notion, Google Calendar | Tres haute |

**Gap majeur** : Aucun acteur ne combine coordination + anticipation IA + visibilite charge mentale + equite couple.

---

## 4. Synthese Voix du Client

### 4.1 Top 5 Irritants (corrrobores par 2+ sources)

| # | Irritant | Mentions | Sources |
|---|----------|----------|---------|
| 1 | "Je pense a tout" — anticipation constante | 45 | Reddit, Doctissimo, MagicMaman |
| 2 | "Fallait demander" — devoir expliciter chaque tache | 42 | Reddit, Doctissimo, forums |
| 3 | Planification repas + courses | 38 | Reddit, MagicMaman |
| 4 | Manque d'initiative du partenaire | 38 | Reddit, forums |
| 5 | Perception masculine d'equite illusoire | 31 | Reddit, Doctissimo |

### 4.2 Pourquoi les apps actuelles echouent

1. **Resolvent 20% du probleme** (taches visibles) — ignorent 80% (anticipation, emotions, equite)
2. **Ajoutent une tache** au lieu d'en supprimer (friction entree donnees)
3. **N'engagent pas le partenaire** → la mere reste seule utilisatrice → friction couple augmente
4. **Pas d'anticipation** : miroir du status quo, pas agent de changement

### 4.3 Ce que les parents veulent reellement

1. **Systeme d'anticipation** : vue 1-2 semaines de ce qui arrive + ce qu'il faut preparer
2. **Equite couple visible** : rendre la charge mentale mesurable, non-accusatrice
3. **Auto-remplissage** : integration ecole, calendrier existant, mails — zero saisie manuelle
4. **Decision support** : suggestions repas, activites, priorites basees sur contexte
5. **Communication sans friction** : partage d'info avec partenaire sans reformuler

### 4.4 Ce qu'ils ne veulent PAS

- Gamification infantilisante
- App supplementaire a ouvrir
- Tracking culpabilisant ("taches non faites")
- Partage social force
- Complexite de configuration

---

## 5. Grille de Scoring — Evaluation Idees Produit

Grille ponderee pour evaluer les idees produit en Session 3 (Phase 5).

| Critere | Poids | Description | Echelle |
|---------|-------|-------------|---------|
| **Douleur resolue** | 25% | Intensite de l'irritant adresse (top 5 = score max) | 1-10 |
| **Facilite d'adoption** | 20% | Friction d'onboarding, anti-app-fatigue, integration existant | 1-10 |
| **Differenciation** | 15% | Distance vs concurrents existants (gap adresse) | 1-10 |
| **Vitesse MVP** | 15% | Faisabilite technique en 4 sprints (S0-S3, ~30 jours) | 1-10 |
| **Potentiel business** | 10% | Taille marche cible, willingness to pay, scalabilite | 1-10 |
| **Risque RGPD/ethique** | 10% | Complexite compliance, donnees enfants, risques psycho | 1-10 (10=faible risque) |
| **Defensabilite** | 5% | Moat a moyen terme (donnees, habitudes, integrations) | 1-10 |

**Score final** = somme ponderee sur 10. Seuil minimum : 6.5/10 pour consideration.

### Bonus/Malus

| Facteur | Ajustement |
|---------|-----------|
| Adresse 3+ irritants top 5 | +0.5 |
| Mode offline/low-connectivity | +0.3 |
| Integration WhatsApp/SMS native | +0.3 |
| Necessite donnees enfants sensibles | -0.5 |
| Depend d'une seule plateforme (lock-in) | -0.3 |
| Anti-app-fatigue (pas de nouvelle app) | +0.5 |

---

## 6. Distribution — Analyse Strategique

### 6.1 Canaux de distribution des concurrents (a approfondir)

| Canal | Acteurs | Efficacite | Cout |
|-------|---------|-----------|------|
| **App Store / Google Play** | Tous (Cozi, TimeTree, FamilyWall) | Moyenne (CAC $10-20/famille) | Moyen |
| **B2B2C Sante** | May, Huckleberry | Haute (confiance pediatre) | Faible CAC, long sales cycle |
| **B2B2C Ecoles** | FamilyWall, Klassly | Haute (LTV $5-15K/an) | Long sales cycle |
| **Bouche-a-oreille / viral** | Cozi, Peanut | Haute (parent→parent) | Quasi nul |
| **Content marketing / SEO** | BabyCenter, Kinedu | Haute (trafic organique) | Temps |
| **Partenariats telco** | Bark, Qustodio | Moyenne | Revenue share |
| **Influenceurs parentalite** | TinyPal, Peanut | Variable | $500-5K/post |
| **WhatsApp/SMS natif** | Aucun concurrent actuel | **Inexploite** | Faible |
| **Integration OS (Apple/Google)** | Google Calendar, Apple Family | Tres haute (pre-installe) | Inaccessible |

### 6.2 Patterns observes

1. **Les gagnants combinent 2-3 canaux** : Cozi = App Store + SEO + viral. May = B2B2C sante + App Store.
2. **B2B2C surperforme B2C** en LTV et retention (May, Huckleberry)
3. **Le viral est le seul canal scalable et gratuit** — mais necessite "aha moment" partageable
4. **Canal WhatsApp/SMS = gap majeur** — aucun concurrent ne l'exploite comme canal principal
5. **Marketplace app stores = commoditise** — differentiation impossible par ce seul canal

### 6.3 Axes a approfondir (Session 2-3)

- Distribution specifique FR/EU (canaux, reglementation pub sante)
- Strategies d'acquisition des concurrents IA-first (May, TinyPal, Ollie)
- Potentiel WhatsApp Business API comme canal de distribution
- Partenariats mutuelles/assurances sante FR
- Referral programs dans les apps parentales (patterns qui marchent)
- SEO/GEO/AEO pour l'acquisition organique

---

## 7. Zones d'Incertitude

| Zone | Niveau | Impact | Plan validation |
|------|--------|--------|-----------------|
| Willingness to pay FR/EU | Moyen | Pricing MVP | 20 interviews validation (Session 2+) |
| Taux adoption couples (vs mere seule) | Eleve | Product-market fit | Test A/B onboarding couple vs individuel |
| Cadre legal IA + donnees enfants | Moyen | Architecture technique | Analyse RGPD dediee (Phase 4) |
| Engagement pere dans l'app | Eleve | Retention long terme | UX research specifique peres |
| Fatigue IA ("encore un chatbot") | Moyen | Positionnement | Test messaging pre-launch |

---

## 8. Prochaines Etapes (Sessions 2-4)

| Session | Phase | Livrable | Depend de |
|---------|-------|----------|-----------|
| 2 | Personas + Irritants | 04-personas.md, 05-irritants-opportunities.md | Ce cadrage |
| 2 | Legal/RGPD + Psycho/Brand | 06-legal-ethics.md, 07-brand-psychology.md | Ce cadrage |
| 3 | TOP 3 Idees Produit | 08-top3-ideas.md (utilise grille scoring §5) | Sessions 1-2 |
| 3 | MVP Blueprint | 09-mvp-blueprint.md | TOP 3 |
| 4 | Rapport Final | RAPPORT-FINAL.md | Tout |

---

## Sources principales

Rapport base sur 3 recherches paralleles :
- **01-market.md** : 38K, 14+ sources institutionnelles, TAM/SAM/SOM detailles
- **02-competitors.md** : 65K, 28 acteurs, 40+ sources, fiches structurees
- **03-user-voice.md** : 28K, 278 signaux, 40+ verbatims, 30+ sources

Toutes sources detaillees dans `sources-log.md`.
