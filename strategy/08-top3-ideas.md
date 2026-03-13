# 08 — TOP 3 Idees Produit : Assistant IA de Charge Mentale Parentale

> **Date** : 23 fevrier 2026
> **Auteur** : Stratege Produit Senior, FamTech/IA
> **Methode** : Scoring pondere 7 criteres (00-framing.md §5) + bonus/malus
> **Sources** : 7 rapports de recherche (01-market a 07-brand-psychology, 02b-distribution, 02c-niches)

---

## Executive Summary

Apres analyse croisee de 20 irritants, 4 personas, 28 concurrents, 10 niches et du cadre legal/ethique, trois idees produit emergent avec des scores superieurs au seuil de 6.5/10 :

1. **RESPIRE Weekly** (score 9.00/10) — Assistant IA WhatsApp-first d'anticipation hebdomadaire qui envoie un briefing proactif de la semaine a venir, integre aux calendriers existants. Zero nouvelle app a installer.
2. **RESPIRE Couple** (score 7.70/10) — Dashboard de visibilite de charge mentale couple avec suggestions de repartition, accessible via app legere + notifications WhatsApp.
3. **RESPIRE Solo** (score 7.35/10) — Co-pilote IA pour parents solo combinant anticipation, validation emotionnelle et aide a la decision, via WhatsApp + web app.

**Recommandation** : Construire RESPIRE Weekly en premier (MVP v0 en 4 sprints). C'est le socle commun sur lequel Couple et Solo se greffent naturellement.

---

## Tableau Comparatif

| Dimension | RESPIRE Weekly | RESPIRE Couple | RESPIRE Solo |
|-----------|---------------|----------------|-------------|
| **One-liner** | Briefing IA hebdo via WhatsApp | Rendre visible l'invisible du couple | Co-pilote IA pour parent seul |
| **Persona primaire** | Sophie | Sophie + Karim | Nadia |
| **Irritants resolus** | #1, #3, #6 (top 5) | #2, #4, #5 (top 5) | #1, #3 + isolation |
| **Canal principal** | WhatsApp/SMS | App legere + WhatsApp | WhatsApp + web app |
| **Score final** | **9.00/10** | **7.70/10** | **7.35/10** |
| **MVP scope** | 1 ecran (WhatsApp) | 3 ecrans (dashboard) | 2 ecrans (chat + vue) |
| **Risque RGPD** | Faible (pas de donnees enfants sensibles) | Moyen (donnees couple) | Moyen (donnees emotionnelles) |
| **Vitesse MVP** | 4 sprints (S0-S3, ~5 sem.) | 4 sprints | 4 sprints |
| **Business model** | Freemium 6.99EUR/mois | Couple 12.99EUR/mois | Solo 4.99EUR/mois |

---

## Matrice Scoring Complete

| Critere (poids) | RESPIRE Weekly | RESPIRE Couple | RESPIRE Solo |
|-----------------|---------------|----------------|-------------|
| Douleur resolue (25%) | 9 | 8 | 9 |
| Facilite adoption (20%) | 9 | 7 | 7 |
| Differenciation (15%) | 8 | 8 | 7 |
| Vitesse MVP (15%) | 9 | 7 | 7 |
| Potentiel business (10%) | 7 | 8 | 6 |
| Risque RGPD/ethique (10%) | 8 | 7 | 7 |
| Defensabilite (5%) | 6 | 7 | 7 |
| **Score pondere brut** | **8.40** | **7.50** | **7.40** |
| Bonus 3+ irritants top 5 | +0.5 | +0.5 | +0.0 |
| Bonus WhatsApp/SMS natif | +0.3 | +0.0 | +0.3 |
| Bonus anti-app-fatigue | +0.5 | +0.0 | +0.0 |
| Bonus mode offline | +0.0 | +0.0 | +0.0 |
| Malus donnees enfants sensibles | -0.4 | -0.0 | -0.05 |
| Malus lock-in plateforme | -0.3 | -0.3 | -0.3 |
| **Score final** | **9.00** | **7.70** | **7.35** |

> Note : Le malus donnees enfants sensibles pour Weekly (-0.4) vient du parsing calendrier medical optionnel (desactivable). Pour Couple, les donnees sont adultes uniquement (couple equity). Pour Solo, risque mineur (validation emotionnelle ne traite pas de donnees enfants directement).

---

## IDEE 1 : RESPIRE Weekly

### 1. One-liner

**"Un briefing IA hebdomadaire envoye sur WhatsApp qui anticipe ta semaine de parent avant que tu y penses."**

### 2. Persona cible

- **Primaire** : Sophie (mere active CSP+, 2 enfants, couple) — douleur 9/10 sur anticipation constante
- **Secondaire** : Aminata (mere diaspora, coordination biculturelle) — besoin calendrier multiculturel

### 3. Probleme adresse

Resout les irritants suivants (references 05-irritants-opportunities.md) :

| Irritant | Rang | Mentions | Lien |
|----------|------|----------|------|
| **#1 Anticipation constante** | 1er | 45 | Killer feature directe |
| **#3 Planification repas + courses** | 3e | 38 | Module repas integre |
| **#6 Coordination RDV medicaux** | 6e | 32 | Rappels proactifs |
| **#8 Gestion activites extra-scolaires** | 8e | 28 | Consolidation agenda |

**3 irritants du top 5 adresses** (bonus +0.5)

Verbatim cle (03-user-voice, 04-personas) : *"Je veux une IA qui regarde ma semaine et me dit : voici ce qui arrive, voici ce que tu dois anticiper. Pas une app de plus."* — Sophie

### 4. Solution : description fonctionnelle

RESPIRE Weekly est un **assistant IA qui fonctionne via WhatsApp Business API** (ou SMS fallback). Il n'y a pas d'app a telecharger : le parent connecte ses calendriers (Google Calendar, Outlook, Apple Calendar) via un onboarding web en 3 minutes, et recoit chaque dimanche soir un **briefing anticipe de la semaine**.

Le briefing comprend :
- **Vue anticipation** : tous les RDV, activites, echeances de la semaine a venir, synthetises en prose lisible
- **Taches implicites detectees** : "Mercredi foot = laver maillot mardi", "Vendredi pediatre = preparer carnet vaccins jeudi"
- **Suggestions repas** : 5-7 menus adaptes au planning (jours charges = repas rapides), avec liste courses generee
- **Alertes proactives** : "Permission ecole a signer avant jeudi", "Vaccin DTP du a renouveler"
- **Rappels quotidiens** : notification WhatsApp a 7h avec les 3 priorites du jour

Le parent repond en langage naturel ("Ajoute dentiste jeudi 10h", "Mercredi on mange dehors, retire du planning") et l'IA met a jour le briefing en temps reel.

**Philosophie** : L'IA est un **radar passif** (niveau autonomie 1-2) qui detecte et suggere, jamais un pilote automatique. Le parent decide toujours. Archetype EVERYMAN+SAGE (07-brand-psychology) : "On sait que tu geres 100 choses. Nous en anticipons quelques-unes."

### 5. Workflow IA

```
Dimanche 18h : IA agrege sources (Google Cal + emails + SMS + historique)
                 ↓
              NLP : extraction evenements, inference taches implicites
                 ↓
              Generation briefing (template personnalise par famille)
                 ↓
Dimanche 19h : Envoi WhatsApp → Parent lit en 90 secondes
                 ↓
Lundi-Samedi : Rappel quotidien 7h (3 priorites du jour)
                 ↓
              Parent repond en langage naturel → IA met a jour
                 ↓
              Apprentissage : patterns familiaux, preferences repas, rythmes
```

**Niveaux d'autonomie** (00-framing.md §2.3) :
- **Niveau 1 (Suggest)** : Briefing hebdo, rappels quotidiens
- **Niveau 2 (Draft)** : Suggestions repas, listes courses generees
- **Niveau 3 (Execute)** : Opt-in apres 4+ semaines — prise de RDV Doctolib automatique avec confirmation parent

### 6. Scoring detaille

| Critere | Note | Poids | Justification |
|---------|------|-------|---------------|
| **Douleur resolue** | 9/10 | 25% | Adresse irritant #1 (45 mentions, top absolu). L'anticipation constante est LA douleur universelle des 4 personas. Impact estime : -40-50% de charge cognitive hebdomadaire (05-irritants). |
| **Facilite adoption** | 9/10 | 20% | Zero app a installer. WhatsApp deja utilise par 100% des personas. Onboarding 3 min (connect calendar). Sophie : "max 5-8 min/jour tolerance" (04-personas). |
| **Differenciation** | 8/10 | 15% | Aucun concurrent ne fait WhatsApp-first + anticipation IA (02-competitors). Canal inexploite (02b-distribution). Gap majeur identifie (00-framing §3.3). |
| **Vitesse MVP** | 9/10 | 15% | Stack : WhatsApp Business API + Google Calendar API + LLM (Claude). 4 sprints S0-S3 (~5 semaines dont 2 sem. beta). Pas d'UI native a developper. |
| **Potentiel business** | 7/10 | 10% | TAM France estime €25-60M (00-framing). Niche WhatsApp-first TAM €5-8M (02c-niches). WTP Sophie €9.99/mois, Aminata €6.99/mois. |
| **Risque RGPD/ethique** | 8/10 | 10% | Donnees traitees : calendrier (ordinaire) + repas (ordinaire). Pas de donnees sante enfants par defaut (opt-in). Pas de donnees couple. DPIA simplifiee (06-legal-ethics §3.1 : 3-4 criteres vs 6+). |
| **Defensabilite** | 6/10 | 5% | Moat faible court terme (WhatsApp copiable). Moat moyen terme : donnees familiales accumulees + habitude hebdomadaire. |
| **Score pondere brut** | **8.40** | | 9×0.25 + 9×0.20 + 8×0.15 + 9×0.15 + 7×0.10 + 8×0.10 + 6×0.05 |
| **Bonus** | +1.3 | | +0.5 (3+ irritants top 5) + 0.3 (WhatsApp natif) + 0.5 (anti-app-fatigue) |
| **Malus** | -0.7 | | -0.4 (donnees enfants si module medical active) - 0.3 (lock-in WhatsApp/Meta) |
| **SCORE FINAL** | **9.00/10** | | |

### 7. Canaux distribution recommandes

D'apres 02b-distribution.md :

| Canal | Priorite | CAC estime | Justification |
|-------|----------|-----------|---------------|
| **WhatsApp viral** (referral) | #1 | €2-4 | Coefficient viral 1.5-2.0x (02b §2.6). Parent partage numero WhatsApp du bot a une amie. |
| **SEO/Content** | #2 | €1-3 | "Comment organiser semaine famille" = 3K recherches/mois FR (02b §2.4). |
| **Micro-influenceurs parentalite** | #3 | €3-8 | 50-100 micro = 500-5000 installs. Budget €1.5K (02b §2.5). |
| **B2B2C PMI/CAF** | #4 (M6+) | €0-2 | CAF modernise outils digitaux 2025-2026 (02c-niches §France). Zero CAC si partenariat reussi. |
| **Podcasts parentalite FR** | #5 | €5-15 | La Boite a Outils des Parents (10-30K/ep). Opportunite car apps parentales absentes du canal (02b §2.4). |

### 8. Integrations techniques cles

| Integration | Priorite | Complexite | Source |
|-------------|----------|-----------|--------|
| **WhatsApp Business API** | MVP | Moyenne | Meta Cloud API, €50-200/mois pour messages (02b §2.6) |
| **Google Calendar API** | MVP | Faible | API bien documentee, OAuth (05-irritants §1.1) |
| **Apple Calendar (CalDAV)** | MVP | Faible | Standard CalDAV |
| **Claude API (Anthropic)** | MVP | Faible | Generation briefings, NLP conversationnel |
| **Doctolib API** | v1 (opt-in) | Moyenne | Auto-booking RDV (05-irritants §6.1). Necessite partenariat. |
| **Marmiton/Yummly API** | v1 | Faible | Base de recettes pour module repas (05-irritants §3.1) |

### 9. Risques + mitigations

| Risque | Probabilite | Impact | Mitigation |
|--------|-------------|--------|-----------|
| **Dependance Meta/WhatsApp** | Moyen | Haut | SMS fallback des v0. Roadmap Telegram + email (06-legal-ethics §transferts). Malus -0.3 applique. |
| **RGPD calendrier + emails** | Faible | Moyen | Consentement explicite par source (06-legal-ethics §1.2). Pseudonymisation avant envoi LLM (Option A recommandee). DPA Anthropic signe. |
| **Notification fatigue** | Moyen | Moyen | Max 1 briefing/semaine + 1 rappel/jour. Opt-in par type (07-brand-psychology §risque dependance). |
| **Erreur IA anticipation** | Moyen | Faible | Niveau 2 = parent valide toujours. Afficher "raison" de chaque suggestion (06-legal-ethics §AI Act transparence). |
| **Adoption pere** | Moyen | Moyen | Karim n'installe rien spontanement (04-personas). WhatsApp = canal neutre, non-gendered. Framing "co-pilote famille" pas "aide-maman" (07-brand-psychology). |

### 10. MVP v0 : scope minimal

**1 boucle de valeur** : Dimanche soir, le parent recoit un briefing WhatsApp anticipant sa semaine.

**Scope strict** :
- 1 ecran : conversation WhatsApp (zero UI custom)
- Onboarding : page web 1 ecran (connecter Google Calendar + entrer preferences famille)
- Input : Google Calendar uniquement
- Output : 1 briefing hebdo (dimanche 19h) + 1 rappel quotidien (7h, 3 priorites)
- IA : Claude API, prompt engineering (pas de fine-tuning)
- Pas de module repas (v1)
- Pas de module medical (v1)
- Pas de partenaire/couple (v1)

**Tech stack** :
- Backend : Node.js + WhatsApp Cloud API + Google Calendar API
- IA : Claude API (Anthropic) avec DPA signe
- Hebergement : EU-based (Scaleway/OVH) pour RGPD
- Base de donnees : PostgreSQL (Neon EU region)
- Pas de frontend natif (WhatsApp = UI)

**Definition of Done** : Parent connecte calendar → recoit briefing pertinent dimanche → repond "Ajoute X" → briefing mis a jour.

### 11. Business model

| Element | Valeur | Source |
|---------|--------|--------|
| **Freemium** | Gratuit : 1 briefing/semaine, 1 enfant, vue 1 semaine | — |
| **Premium** | €6.99/mois : multi-enfants, rappels quotidiens, module repas, vue 2 semaines | WTP Sophie €9.99 (04-personas) |
| **Couple** | €12.99/mois : + briefings partenaire, suggestions repartition | WTP Sophie max €19.99 (04-personas) |
| **LTV @12 mois** | €50-70 (retention 60%, ARPU €7/mois) | Benchmark apps parentales (02c-niches) |
| **CAC blended** | €3-5 | WhatsApp viral + SEO (02b-distribution) |
| **LTV/CAC** | **10-14x** | Tres sain (seuil minimum 3x) |
| **Break-even** | Mois 4-5 (400 abonnes premium) | — |

### 12. GTM (Go-to-Market)

| Phase | Periode | Actions | KPI |
|-------|---------|---------|-----|
| **Beta fermee** | S1-S2 (2 semaines) | 30 Sophie-type (CSP+, IDF, 2+ enfants). Recrutement via groupes WhatsApp parentalite. | 70%+ ouvrent briefing dimanche |
| **Beta ouverte** | S3-S4 | 100 parents. Ajout module repas. Referral : "Partage le numero a une amie". | Coefficient viral > 1.0 |
| **Soft launch FR** | M2-M3 | SEO (5 articles), 20 micro-influenceurs, landing page. | 500 utilisateurs actifs, 50 premium |
| **Growth** | M4-M6 | Podcasts, B2B2C PMI pilote 3 regions. Module Couple (idee 2). | 2000 utilisateurs, 200 premium, CAC < €5 |

---

## IDEE 2 : RESPIRE Couple

### 1. One-liner

**"Un dashboard IA qui rend visible la charge mentale invisible du couple et suggere une repartition equitable sans accusation."**

### 2. Persona cible

- **Primaire** : Sophie + Karim (couple en tension, perception gap 50-50 vs 70-30)
- **Secondaire** : Claire & Thomas (couple recompose, double logistique)

### 3. Probleme adresse

| Irritant | Rang | Mentions | Lien |
|----------|------|----------|------|
| **#2 "Fallait demander"** | 2e | 42 | Task visibility engine |
| **#4 Manque initiative partenaire** | 4e | 38 | Coach proactif partenaire |
| **#5 Perception equite illusoire** | 5e | 31 | Equity dashboard |

**3 irritants du top 5 adresses** (bonus +0.5)

Verbatim cle (04-personas) : *"Oh. Je ne savais pas. C'est CA qu'elle porte ?"* — Reaction Karim face au dashboard equity dans scenario aha-moment (80% likelihood adoption).

### 4. Solution : description fonctionnelle

RESPIRE Couple est une **app legere (PWA)** + **notifications WhatsApp** qui rend visible la charge mentale invisible entre partenaires.

Le systeme fonctionne en 3 couches :

1. **Task Visibility Engine** : L'IA detecte les taches implicites a partir du calendrier partage et les rend explicites. "RDV pediatre jeudi" genere automatiquement "Preparer carnet vaccins mardi" + "Confirmer qui emmene". Ces taches apparaissent dans un feed partage.

2. **Equity Dashboard** : Visualisation hebdomadaire de la repartition reelle (taches visibles + invisibles). Pas de score accusatoire mais un "radar d'equilibre" : zones ou un partenaire est surcharge. Framing collaboratif : "Vous travaillez sur QUOI ensemble cette semaine ?" (07-brand-psychology §risque surveillance).

3. **Proactive Partner Coach** : L'IA envoie au partenaire moins charge des suggestions proactives avec timing optimal et framing positif. "Eva a foot mercredi 18h. Son maillot a peut-etre besoin d'un coup de frais. Mardi entre 19h-20h c'est ideal." (05-irritants §4.1).

**Garde-fous ethiques** (07-brand-psychology §6 pieges) :
- JAMAIS d'indicateurs "tu vs lui" style score brut
- Pas de gamification (pas de "streak d'equite")
- Frame collaboratif : "Qui est le mieux place pour quoi ?" pas "Qui ne fait rien ?"
- Validation des deux partenaires requise avant envoi de suggestions
- "Safety Mode" : consentement renouvele chaque semaine si localisation activee (06-legal-ethics §5.2)

### 5. Workflow IA

```
Flux continu : IA parse calendrier partage couple
                 ↓
              Inference taches implicites (NLP contextuel)
                 ↓
              Attribution suggeree (basee sur emplois du temps)
                 ↓
              Parent gestionnaire valide avant envoi (Niveau 2)
                 ↓
              Notification WhatsApp au partenaire (framing positif)
                 ↓
              Partenaire accepte / reporte / redirige
                 ↓
Hebdomadaire : Equity Dashboard mis a jour (feed partage)
                 ↓
              "Rapport couple" bi-mensuel : distribution, tendances, suggestions
```

**Niveaux d'autonomie** :
- **Niveau 1 (Suggest)** : Suggestions au partenaire
- **Niveau 2 (Draft)** : Parent gestionnaire valide avant envoi
- **Niveau 3** : Hors scope MVP (trop risque pour dynamique couple)

### 6. Scoring detaille

| Critere | Note | Poids | Justification |
|---------|------|-------|---------------|
| **Douleur resolue** | 8/10 | 25% | Irritants #2 et #4 = 80 mentions combinees. Douleur intense mais moins universelle que #1 (concerne couples, pas solo). |
| **Facilite adoption** | 7/10 | 20% | Necessite que les DEUX partenaires s'engagent. Karim = "skeptical adopter" (04-personas). Adoption plus lente. |
| **Differenciation** | 8/10 | 15% | Aucun concurrent ne visualise l'equite couple. Gap majeur (00-framing §3.3, 07-brand-psychology §white space). |
| **Vitesse MVP** | 7/10 | 15% | PWA + API calendrier + LLM. 4 sprints. Plus complexe que Weekly (UI dashboard + double utilisateur). |
| **Potentiel business** | 8/10 | 10% | Pricing couple €12.99/mois (04-personas WTP Sophie max €19.99). TAM couples en tension = 50-60% du marche. |
| **Risque RGPD/ethique** | 7/10 | 10% | Risque surveillance couple (06-legal-ethics §5.2). Mitigation : double consentement, Safety Mode. Pas de donnees enfants directes. |
| **Defensabilite** | 7/10 | 5% | Donnees couple accumulees = moat. Habitude couple = switching cost eleve. |
| **Score pondere brut** | **7.50** | | |
| **Bonus** | +0.5 (3+ irritants top 5) | | |
| **Malus** | -0.3 (lock-in potentiel) | | |
| **SCORE FINAL** | **7.70/10** | | |

### 7. Canaux distribution recommandes

| Canal | Priorite | CAC | Justification |
|-------|----------|-----|---------------|
| **Referral couple** (Sophie invite Karim) | #1 | €0 | Boucle virale naturelle : mere adopte → invite partenaire. |
| **Bouche-a-oreille** | #2 | €0-2 | Parents recommandent a d'autres couples. Coefficient viral 0.6-0.8. |
| **Instagram cible** | #3 | €5-12 | CSP+ parents 30-45 ans, ciblage "charge mentale" (02b §2.5). |
| **Podcasts couple/parentalite** | #4 | €5-15 | Positioning "equite couple" = nouveau angle vs "organisation famille". |

### 8. Integrations techniques cles

| Integration | Priorite | Notes |
|-------------|----------|-------|
| Google Calendar API (partage) | MVP | Calendrier couple partage |
| WhatsApp Business API | MVP | Notifications partenaire |
| Claude API | MVP | Inference taches implicites, framing suggestions |
| PWA (React + Next.js) | MVP | Dashboard couple, onboarding |

### 9. Risques + mitigations

| Risque | Mitigation |
|--------|-----------|
| **Partenaire ressent "ordres" de l'app** | Framing : "Suggestion" pas "ordre". Parent valide avant envoi. Partenaire peut contester. Max 3 notifs/jour (05-irritants §2.1). |
| **Outil d'accusation couple** | JAMAIS de scores bruts. Radar equilibre sans classement. "Conversation starter" pas "verdict" (07-brand-psychology §piege surveillance). |
| **Adoption asymetrique** (mere seule utilise) | Fonctionnalite degradee si 1 seul utilisateur = anticipation view (Weekly). Valeur couple = bonus, pas prerequis. |
| **Surveillance domestique** | Double consentement obligatoire. Safety Mode. Hotline 3919 affichee si localisation activee (06-legal-ethics §5.2). |

### 10. MVP v0 : scope minimal

**1 boucle de valeur** : Sophie voit la repartition reelle des taches, Karim recoit une suggestion proactive et agit dessus.

**Scope strict** :
- 3 ecrans PWA : (1) Onboarding couple, (2) Feed taches partagees, (3) Radar equilibre hebdo
- Input : Google Calendar partage du couple
- Notifications WhatsApp au partenaire (1-2/jour max)
- IA : inference taches implicites (Claude API)
- Pas de tracking temps (v1 : declaration, pas tracking obsessif)
- Pas de localisation (trop risque MVP)

### 11. Business model

| Element | Valeur |
|---------|--------|
| **Freemium** | Feed taches partagees, 1 enfant |
| **Premium Couple** | €12.99/mois : equity dashboard, suggestions proactives, multi-enfants |
| **LTV @12 mois** | €80-100 (retention couple 65%, ARPU €10/mois) |
| **CAC** | €2-5 (referral couple naturel) |
| **LTV/CAC** | **16-50x** |

### 12. GTM

| Phase | Actions |
|-------|---------|
| **Beta** (M1) | 20 couples Sophie+Karim type. Recrutement via RESPIRE Weekly (upgrade naturel). |
| **Launch** (M3) | Fonctionnalite integree a Weekly. Upsell in-app. |
| **Growth** (M6) | Partenariats psychologues couple. Contenu "equite parentale" (SEO). |

---

## IDEE 3 : RESPIRE Solo

### 1. One-liner

**"Un co-pilote IA bienveillant pour parents solo qui anticipe la semaine, valide les efforts et aide a decider sans juger."**

### 2. Persona cible

- **Primaire** : Nadia (mere solo freelance, burnout silencieux, douleur 10/10)
- **Secondaire** : Marc (pere solo, enfant handicape)

### 3. Probleme adresse

| Irritant | Rang | Mentions | Lien |
|----------|------|----------|------|
| **#1 Anticipation constante** | 1er | 45 | Vue anticipation (core) |
| **#3 Planification repas + courses** | 3e | 38 | Suggestions adaptees budget serre |
| **Isolement decisionnel** (non-numerote) | — | 04-personas | "Pas de co-parent pour valider" |
| **Culpabilite + jugement social** | — | 04-personas | Validation emotionnelle |

**2 irritants du top 5** (pas de bonus 3+)

Verbatim cle : *"J'ai besoin de quelque chose qui me voit. Pas qui me juge. Juste : tu es en train de faire quelque chose d'impossible et tu es assez."* — Nadia (04-personas)

### 4. Solution : description fonctionnelle

RESPIRE Solo combine l'anticipation hebdomadaire de Weekly avec une couche de **validation emotionnelle et aide a la decision** specifique aux parents solo.

Differenciateurs vs Weekly :
- **Solo Parent Mode** : premier ecran = "Tu portes a lot. Voici ce qui compte vraiment cette semaine, et voici ce que tu peux lacher." Permission de l'imperfection.
- **Decision Helper** : quand Nadia hesite ("Leo devrait-il aller a cette activite ou c'est trop ?"), l'IA propose 2-3 options avec pour/contre, sans prescrire. "Tu connais Leo mieux que quiconque."
- **Budget-aware** : suggestions repas et activites adaptees au budget serre (€120/semaine courses, pas €200).
- **Micro-communaute** : anonymised stories d'autres parents solo ("Cette semaine j'ai laisse Leo devant l'ecran 2h parce que j'avais besoin. 142 coeurs."). Pas un forum, juste de la normalisation.
- **Urgence mode** : quand crise (Leo malade + deadline), IA propose ressources hyperlocales (babysitter, SOS medecin, solution quick).

**Ton** (07-brand-psychology) : EVERYMAN pur. "On sait que tu fais ca seul(e). Tu n'es pas en echec. Tu es en survie, et c'est deja enorme."

### 5. Workflow IA

```
Dimanche 18h : Briefing Weekly (identique idee 1)
              + Couche Solo : "Semaine intense (7/10). Voici les 2 vrais urgents. Le reste peut attendre."
                 ↓
Lundi-Samedi : Rappels quotidiens + "Comment tu te sens ?" (1x/semaine, optionnel)
                 ↓
              Si stress detecte : "Tu veux une suggestion?" → Decision Helper
                 ↓
              Si crise : "Urgence mode" → ressources locales + reduction planning
                 ↓
Hebdomadaire : "Tu as gere X choses cette semaine. C'est remarquable pour 1 personne."
```

**Niveaux d'autonomie** :
- **Niveau 1** : Briefing + validation emotionnelle
- **Niveau 2** : Suggestions repas budget-aware, decision helper
- Pas de niveau 3+ (parent solo = besoin de controle, pas de delegation)

### 6. Scoring detaille

| Critere | Note | Poids | Justification |
|---------|------|-------|---------------|
| **Douleur resolue** | 9/10 | 25% | Pain level Nadia = 10/10 (04-personas). Parents solo : burnout 68% vs 35% couples (02c-niches §niche 1). Besoin le plus aigu de tout le marche. |
| **Facilite adoption** | 7/10 | 20% | WhatsApp + web app legere. Nadia = "cautious adopter" (04-personas). Besoin de confiance d'abord. Onboarding emotionnel necessaire. |
| **Differenciation** | 7/10 | 15% | Zero app dediee parents solo (02c-niches). Mais differenciation technique plus faible que Couple (c'est Weekly + couche emotionnelle). |
| **Vitesse MVP** | 7/10 | 15% | Weekly + couche validation + decision helper. 4 sprints. Module communaute = complexite supplementaire. |
| **Potentiel business** | 6/10 | 10% | WTP Nadia = €3.99-9.99/mois (budget serre, 04-personas). TAM parents solo FR = €12-18M (02c-niches) mais ARPU bas. |
| **Risque RGPD/ethique** | 7/10 | 10% | Validation emotionnelle = donnees sensibles (humeur, stress). Pas de donnees sante enfants directes. Risque : dependance emotionnelle a l'IA (07-brand-psychology §piege dependance). |
| **Defensabilite** | 7/10 | 5% | Communaute solo = moat fort. Donnees emotionnelles = switching cost eleve. |
| **Score pondere brut** | **7.40** | | |
| **Bonus** | +0.3 (WhatsApp natif) | | |
| **Malus** | -0.3 (lock-in WhatsApp) -0.05 (donnees emotionnelles mineures) | | |
| **SCORE FINAL** | **7.35/10** | | |

### 7. Canaux distribution recommandes

| Canal | Priorite | CAC | Justification |
|-------|----------|-----|---------------|
| **Facebook groupes parents solo** | #1 | €3-5 | 60% likelihood adoption Nadia (04-personas). 100k+ membres SPF FR. |
| **Instagram comptes monoparentalite** | #2 | €5-10 | 40% likelihood Nadia. |
| **B2B2C PMI / associations** | #3 | €0-2 | PMI modernise outils 2025 (02c-niches). CAF partenariat potential. |
| **SEO** | #4 | €1-3 | "Aide parent solo" = requetes en croissance. |

### 8. Integrations techniques cles

| Integration | Priorite |
|-------------|----------|
| WhatsApp Business API | MVP |
| Google Calendar API | MVP |
| Claude API (validation emotionnelle + decision helper) | MVP |
| PWA minimale (web app) | MVP |
| Ressources locales API (Doctolib, Yoopies) | v1 |

### 9. Risques + mitigations

| Risque | Mitigation |
|--------|-----------|
| **Dependance emotionnelle a l'IA** | Disclaimer : "Cet outil ne remplace pas un professionnel." Lien vers therapist finder si stress > seuil. Design "augmentation" pas "remplacement" (07-brand-psychology §piege dependance). |
| **IA qui juge** | Audit biais genre pre-launch (06-legal-ethics §5.3). Ton neutre valide par psychologue parentale. JAMAIS de "Tu devrais..." mais "Voici des options." |
| **Budget paywall** | Freemium genereux (briefing hebdo gratuit). Premium a €3.99 (pas €9.99). Trial 1 mois gratuit pour parents solo (CAF-subsidized a terme). |
| **Faible WTP** | B2B2C mutuelles (Harmonie, MGEN) = mutuelle paie, parent recoit gratuitement (02c-niches §modeles B2B2C). |

### 10. MVP v0 : scope minimal

**1 boucle de valeur** : Nadia recoit le briefing + "Tu portes beaucoup. Voici les 2 priorites." → se sent vue.

**Scope strict** :
- 2 ecrans : (1) Conversation WhatsApp (briefing + validation), (2) Page web "Mon espace" (preferences, historique)
- Input : Google Calendar
- Output : briefing hebdo + validation emotionnelle + 1 "decision helper" interactif
- Pas de communaute (v1)
- Pas d'urgence mode (v1)

### 11. Business model

| Element | Valeur |
|---------|--------|
| **Freemium** | Briefing hebdo, 1 enfant, validation basique |
| **Premium Solo** | €4.99/mois : decision helper, multi-enfants, ressources locales |
| **LTV @12 mois** | €35-50 (retention 80%+, ARPU €4.50/mois) |
| **CAC** | €3-5 (communautes + PMI) |
| **LTV/CAC** | **7-10x** |

### 12. GTM

| Phase | Actions |
|-------|---------|
| **Beta** (M1) | 30 Nadia-type via groupes Facebook solo parents. Trial gratuit 2 mois. |
| **Launch** (M3) | Module Solo integre a Weekly. Upsell via detection "parent seul" a l'onboarding. |
| **Growth** (M6) | PMI pilote. Partenariat associations monoparentalite FR. |

---

## Recommandation Finale

### Construire RESPIRE Weekly en premier

**Pourquoi Weekly et pas Couple ou Solo ?**

1. **Score le plus eleve** (9.00 vs 7.70 et 7.35) sur tous les criteres ponderes.

2. **C'est le socle commun**. Weekly est le noyau technique (calendrier + LLM + WhatsApp) sur lequel Couple et Solo se greffent comme des modules :
   - Weekly + module equity = Couple
   - Weekly + module validation = Solo
   - Construire Weekly d'abord = 60% du travail de Couple et Solo deja fait.

3. **Vitesse MVP maximale** : 4 sprints S0-S3 (~5 semaines dont S3 = beta privee 14j). Zero UI native. La v0 est litteralement un bot WhatsApp connecte a Google Calendar.

4. **Risque RGPD minimal** : pas de donnees couple, pas de donnees emotionnelles, pas de donnees sante par defaut. DPIA simplifiee (06-legal-ethics).

5. **Anti-app-fatigue** : le parent n'installe rien. WhatsApp est deja la (04-personas : 100% des personas l'utilisent). C'est le seul des 3 produits qui obtient le triple bonus (+0.5 anti-app-fatigue, +0.3 WhatsApp natif, +0.5 irritants top 5).

6. **Validation de marche rapide** : si le briefing WhatsApp ne cree pas d'habitude en 4 semaines, les modules Couple et Solo n'ont pas de fondation. Weekly est le test acide.

**Roadmap recommandee** :

```
Mois 1-2 : RESPIRE Weekly MVP (bot WhatsApp + Google Calendar)
Mois 3   : Ajout module repas + onboarding simplifie
Mois 4   : RESPIRE Couple (upgrade pour couples, equity dashboard PWA)
Mois 5   : RESPIRE Solo (upgrade pour parents solo, validation + decision helper)
Mois 6+  : B2B2C (PMI, mutuelles), expansion Aminata (bilingual), integrations Doctolib
```

---

## Idees Rejetees

### 1. Carnet de Sante Numerique IA (Score estime : 6.2/10 — sous le seuil)
**Description** : App dediee au suivi medical enfants (vaccins, allergies, RDV specialistes) avec IA d'anticipation medicale.
**Raison du rejet** :
- Donnees sante enfants = art. 9 RGPD, DPIA lourde obligatoire (06-legal-ethics §1.1). Malus -0.5.
- Risque classification "Software as Medical Device" si conseils nutrition/sante (06-legal-ethics §4.1). Investissement legal 50-100K EUR.
- Doctolib API non ouverte publiquement. Dependance partenariat non garanti.
- **Mieux comme module opt-in de Weekly** (v1+) que comme produit standalone.

### 2. Family OS All-in-One (Score estime : 5.8/10 — sous le seuil)
**Description** : Plateforme integrale (calendrier + sante + budget + courses + activites + couple) = "Notion pour familles".
**Raison du rejet** :
- Vitesse MVP catastrophique (8+ sprints minimum). Score 3/10 sur critere "Vitesse MVP".
- Risque app-fatigue maximal : ENCORE une app a installer, configurer, remplir (00-framing §4.2 : "Apps actuelles echouent car ajoutent une tache").
- Concurrence directe Cozi, FamilyWall, Google Family (00-framing §3.3 : Tier 1 = saturation haute).
- **YAGNI** : construire le minimum d'abord, etendre organiquement.

### 3. Chatbot Parentalite Generaliste (Score estime : 5.5/10)
**Description** : ChatGPT specialise parentalite, accessible via app. Questions libres sur education, sante, discipline.
**Raison du rejet** :
- Differenciation nulle (ChatGPT, Gemini, Claude font deja ca — 00-framing §3.3 Tier 3 = saturation haute).
- Pas de proactivite (chatbot reactif = l'oppose de l'anticipation).
- Risque ethique eleve : conseils parentaux prescriptifs = responsabilite legale + biais genre (06-legal-ethics §5.3).
- **Pas de moat** : n'importe qui peut wrapper un LLM en "parenting bot".

### 4. App Covoiturage Parents (Score estime : 5.0/10)
**Description** : Plateforme de covoiturage entre parents pour activites extra-scolaires.
**Raison du rejet** :
- Resout 1 seul irritant (#8, rang 8, 28 mentions). Trop etroit pour un produit standalone.
- Effet reseau necessaire (cold start problem massif — besoin de densite locale).
- Concurrence : BlaBlaCar Kids, Karos, services scolaires existants.
- **Mieux comme feature de Weekly** (v2+ carpooling coordinator).

### 5. Gamification Equite Couple (Score estime : 4.5/10 — nettement sous le seuil)
**Description** : App ou les partenaires "scorent" leurs taches et gagnent des points d'equite.
**Raison du rejet** :
- Piege psychologique #1 identifie dans 07-brand-psychology : gamification infantilisante.
- Transforme l'equite en competition = toxicite relationnelle (07-brand-psychology §piege surveillance).
- Parents rejettent explicitement la gamification (00-framing §4.4 : "Gamification infantilisante" dans ce qu'ils ne veulent PAS).
- Contrairement a RESPIRE Couple, qui utilise un radar d'equilibre sans score.

---

## Sources

| Fichier | Contenu utilise | References |
|---------|----------------|------------|
| **00-framing.md** | Grille scoring §5, taxonomie taches, synthese marche, voix du client | TAM, irritants top 5, niveaux autonomie |
| **02b-distribution.md** | CAC par canal, WhatsApp Business data, B2B2C modeles | Strategies distribution, coefficients viraux |
| **02c-niches.md** | TOP 10 niches, TAM par niche, LTV/CAC, segmentation FR | Parents solo, sante, familles nombreuses |
| **04-personas.md** | 4 personas MVP (Sophie, Karim, Nadia, Aminata) | WTP, canaux decouverte, aha moments, journees types |
| **05-irritants-opportunities.md** | 20 irritants x solutions IA, workflows, faisabilite | Anticipation view, task visibility, meal planning, equity dashboard |
| **06-legal-ethics.md** | RGPD, DPIA, AI Act, risques ethiques, disclaimers | Bases legales, transferts hors-EU, donnees enfants, surveillance |
| **07-brand-psychology.md** | Archetypes, naming, messaging, 6 pieges psychologiques | EVERYMAN+SAGE, framing, risques culpabilisation/dependance |
