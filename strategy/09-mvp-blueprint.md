# 09 — MVP Blueprint : RESPIRE Weekly

> **Date** : 23 fevrier 2026
> **Auteur** : Product Architect Senior
> **Produit** : RESPIRE Weekly — Bot WhatsApp d'anticipation hebdomadaire
> **Persona primaire** : Sophie (mere active CSP+, couple, 2 enfants)
> **Score produit** : 9.00/10 (08-top3-ideas.md)
> **References** : 00-framing, 04-personas, 05-irritants, 06-legal-ethics, 07-brand-psychology

---

## 1. Executive Summary

### Vision produit

RESPIRE Weekly est un assistant IA accessible via WhatsApp qui anticipe la semaine du parent avant qu'il y pense. Chaque dimanche soir, le parent recoit un briefing intelligent agrege depuis ses calendriers existants, sans installer de nouvelle application. L'IA detecte les taches implicites ("RDV pediatre jeudi = preparer carnet vaccins mercredi") et envoie des rappels quotidiens cibles.

### Metriques de succes MVP

| Metrique | Cible | Horizon | Justification |
|----------|-------|---------|---------------|
| **Taux d'activation** | 70% completent onboarding | S3 | Sophie = fast adopter (04-personas) |
| **Taux ouverture briefing** | 80%+ ouvrent le dimanche | S3 | Benchmark WhatsApp business : 85-95% open rate |
| **Retention S2** | 60%+ reviennent semaine 2 | S3 | Signal early habit |
| **Retention M1** | 50%+ actifs a 30 jours | S3 | Seuil product-market fit |
| **NPS** | 40+ | S3 | Benchmark apps parentales : NPS 20-30 |
| **Aha moment** | 65% Sophie-type dans les 3 premiers jours | S3 | "L'app m'a rappele quelque chose que j'aurais oublie" |

---

## 2. Parcours Utilisateur v0

### Boucle de valeur complete

```
ETAPE 1: INSCRIPTION (3 min)
Sophie decouvre RESPIRE via recommandation amie WhatsApp
  → Clique lien → Page web onboarding (1 ecran)
  → OAuth Google Calendar (1 clic)
  → Renseigne : prenom, nb enfants, preferences horaires
  → Scan WhatsApp QR / envoie "BONJOUR" au numero RESPIRE
  → Confirmation : "Parfait Sophie \! Ton premier briefing arrive dimanche 19h."

ETAPE 2: PREMIER BRIEFING (dimanche 19h)
WhatsApp notification → Sophie ouvre le message
  → Briefing structure : RDV, activites, taches implicites
  → Sophie lit en 90 secondes
  → Repond "Ajoute dentiste jeudi 10h" → IA confirme en 5 secondes
  → AHA MOMENT : "Comment il savait pour le maillot de foot ?"

ETAPE 3: RAPPELS QUOTIDIENS (lundi-samedi 7h)
  → Message WhatsApp : "Bonjour Sophie. Aujourd'hui : 3 priorites."
  → Sophie valide / ajuste en repondant en langage naturel
  → Habitude installee en 7 jours
```

### Wireframes textuels

**Ecran 1 — Page web onboarding (unique ecran web)**

```
┌─────────────────────────────────────────┐
│            RESPIRE Weekly               │
│   "Pour que tu ne penses pas a tout"    │
│                                         │
│   ┌──────────────────────────────────┐  │
│   │  🔗 Connecter Google Calendar    │  │
│   │     [Bouton OAuth Google]        │  │
│   └──────────────────────────────────┘  │
│                                         │
│   Prenom : [___________]               │
│   Nb enfants : [1] [2] [3+]           │
│   Heure briefing : [19h ▼]            │
│   Heure rappel matin : [7h ▼]         │
│                                         │
│   ┌──────────────────────────────────┐  │
│   │  📱 Recevoir sur WhatsApp        │  │
│   │  Scanne ce QR ou envoie          │  │
│   │  "BONJOUR" au +33 X XX XX XX    │  │
│   └──────────────────────────────────┘  │
│                                         │
│   ☐ J'accepte les CGU et la politique  │
│     de confidentialite                  │
│   ☐ Je consens au traitement de mes    │
│     calendriers (detail)               │
│                                         │
│   [  Commencer  ]                      │
│                                         │
│   🔒 Donnees hebergees en France (UE)  │
│   RGPD compliant · Pas de revente      │
└─────────────────────────────────────────┘
```

**Ecran 2 — Briefing WhatsApp (dimanche 19h)**

```
┌─────────────────────────────────────────┐
│ RESPIRE Weekly                          │
│                                         │
│ Bonjour Sophie 👋                       │
│ Voici ta semaine du 24 fev – 1 mars     │
│                                         │
│ 📋 *3 RDV a anticiper*                  │
│ • Lun 24 — Pediatre 10h                │
│   → Pense au carnet vaccins            │
│ • Mer 26 — Foot Emma 18h               │
│   → Maillot a laver mardi              │
│ • Ven 28 — Reunion ecole 17h           │
│                                         │
│ ⚡ *2 taches detectees*                  │
│ • Permission sortie a signer (jeu max) │
│ • Anniversaire Eva samedi — cadeau ?   │
│                                         │
│ 📊 *Charge semaine* : 6/10             │
│ Mercredi = journee la plus chargee     │
│                                         │
│ Reponds-moi pour ajuster \!             │
│ "Ajoute X" · "Retire Y" · "Detail Z"  │
└─────────────────────────────────────────┘
```

**Ecran 3 — Rappel quotidien (7h)**

```
┌─────────────────────────────────────────┐
│ RESPIRE Weekly                          │
│                                         │
│ Bonjour Sophie ☀️ Lundi 24 fevrier      │
│                                         │
│ *Tes 3 priorites du jour :*            │
│ 1. Pediatre 10h — carnet vaccins ✓     │
│ 2. Pickup Lucas 17h30                  │
│ 3. Preparer affaires foot demain       │
│                                         │
│ Bonne journee \!                        │
└─────────────────────────────────────────┘
```

---

## 3. Architecture Technique MVP

### Stack technique

| Composant | Technologie | Justification |
|-----------|------------|---------------|
| **Backend** | Node.js 22+ (TypeScript) | Ecosysteme WhatsApp, maturite, pool dev FR |
| **Framework** | Hono (sur Node.js) | Leger, rapide, adapte API-first |
| **BDD** | PostgreSQL (Neon, region EU-Frankfurt) | RGPD-compliant, serverless, cout faible |
| **ORM** | Drizzle ORM | Type-safe, performant, migrations simples |
| **IA** | Claude API (Anthropic) — Haiku 4.5 | Cout optimal ($1/$5 par M tokens), DPA disponible, qualite suffisante pour briefings |
| **Messaging** | WhatsApp Cloud API (Meta) | Direct, pas de BSP intermediaire, gratuit pour messages reponse |
| **Calendar** | Google Calendar API (OAuth 2.0) | 80%+ des personas utilisent Google (04-personas) |
| **Hosting** | Scaleway Paris (ou OVH) | Hebergement EU, RGPD natif, cout ~15-30EUR/mois |
| **Queue** | BullMQ (Redis sur Upstash EU) | Planification briefings dimanche 19h, rappels 7h |
| **Onboarding web** | Next.js 15 (page unique) | SSR, OAuth Google, deploiement Vercel EU |
| **Monitoring** | PostHog (EU cloud) | Analytics RGPD-compliant, funnel tracking |

### Schema d'architecture

```
┌──────────────────────────────────────────────────────────────────┐
│                        RESPIRE Weekly — Architecture MVP         │
└──────────────────────────────────────────────────────────────────┘

  ┌──────────┐     OAuth 2.0      ┌──────────────────┐
  │  Google   │◄──────────────────│   Onboarding     │
  │ Calendar  │                   │   Next.js Page    │
  │   API     │                   │   (Vercel EU)     │
  └─────┬─────┘                   └────────┬─────────┘
        │                                  │
        │ Events sync (webhook + poll)     │ User signup data
        ▼                                  ▼
  ┌────────────────────────────────────────────────────┐
  │                  BACKEND (Hono / Node.js)          │
  │                  Scaleway Paris (EU)                │
  │                                                    │
  │  ┌──────────────┐  ┌──────────────┐  ┌──────────┐│
  │  │ Calendar      │  │ Briefing     │  │ Chat     ││
  │  │ Sync Service  │  │ Generator    │  │ Handler  ││
  │  │               │  │ (Claude API) │  │ (NLP)    ││
  │  └──────┬───────┘  └──────┬───────┘  └────┬─────┘│
  │         │                 │                │      │
  │         ▼                 ▼                ▼      │
  │  ┌──────────────────────────────────────────────┐ │
  │  │         PostgreSQL (Neon EU-Frankfurt)       │ │
  │  │  users | calendars | briefings | feedback    │ │
  │  └──────────────────────────────────────────────┘ │
  │         │                                         │
  │         ▼                                         │
  │  ┌──────────────┐                                 │
  │  │   BullMQ      │  Cron jobs :                   │
  │  │   (Upstash)   │  • Dim 18h : sync calendars    │
  │  │               │  • Dim 19h : envoyer briefings  │
  │  │               │  • Lun-Sam 7h : rappels         │
  │  └──────┬───────┘                                 │
  └─────────┼─────────────────────────────────────────┘
            │
            ▼
  ┌──────────────┐
  │  WhatsApp     │
  │  Cloud API    │◄──── Messages entrants (webhook)
  │  (Meta)       │────► Messages sortants (briefings, rappels)
  └──────────────┘
            │
            ▼
  ┌──────────────┐
  │   Sophie     │
  │  (WhatsApp)  │
  └──────────────┘
```

### Choix technologiques justifies

**Claude Haiku 4.5 vs OpenAI GPT-4o-mini** :
- Claude Haiku : $1/$5 par M tokens. Qualite suffisante pour generation briefings structures.
- GPT-4o-mini : $0.15/$0.60. Moins cher mais qualite inferieure en francais et raisonnement contextuel.
- **Choix Claude** : Meilleure qualite FR, DPA Anthropic disponible, coherent avec stack existant. Cout estimé briefing (~800 tokens in + 600 tokens out) = ~$0.004/briefing.
- Batch API (-50%) applicable pour briefings planifies dimanche soir.

**WhatsApp Cloud API vs BSP (Twilio, MessageBird)** :
- Cloud API direct : gratuit pour reponses dans 24h, $0.02-0.04/message marketing (FR).
- BSP : surcout 20-40% + lock-in fournisseur.
- **Choix Cloud API** : Cout minimal, controle total, pas d'intermediaire.

**Neon PostgreSQL vs Supabase** :
- Neon : serverless natif, autoscaling, region EU-Frankfurt, tier gratuit 500MB.
- Supabase : plus de features (auth, storage) mais overkill pour MVP.
- **Choix Neon** : Minimal, serverless, RGPD EU natif.

---

## 4. Integrations Prioritaires

### Google Calendar (MVP — Sprint 0)

| Aspect | Detail |
|--------|--------|
| **API** | Google Calendar API v3 |
| **Auth** | OAuth 2.0 (consent screen, scope `calendar.readonly`) |
| **Cout** | Gratuit (quota 1M requetes/jour) |
| **Complexite** | Faible — API mature, documentation excellente |
| **Implementation** | Webhook push notifications + poll fallback toutes les 6h |
| **Donnees extraites** | Titre event, date/heure, lieu, description, recurrence |
| **Timeline** | S0 (72h) |

### Microsoft Calendar (MVP — Sprint 1)

| Aspect | Detail |
|--------|--------|
| **API** | Microsoft Graph API (Outlook Calendar) |
| **Auth** | OAuth 2.0 via Azure AD / Microsoft Identity |
| **Cout** | Gratuit (5000 requetes/10min) |
| **Complexite** | Moyenne — Azure AD registration, tokens refresh plus complexe |
| **Timeline** | S1 (7j) |

### WhatsApp Business API (MVP — Sprint 0)

| Aspect | Detail |
|--------|--------|
| **API** | WhatsApp Cloud API (Meta Business Platform) |
| **Auth** | Meta Business Manager + token permanent |
| **Cout** | Depuis juillet 2025 : modele per-message (remplace le per-conversation 24h). Service (reponse 24h) = gratuit. Utility = ~€0.0249/msg FR. Marketing = ~€0.0490/msg FR. Authentication = ~€0.02/msg FR. Volume discounts 5-20% par palier. |
| **Complexite** | Moyenne — webhook setup, template approval, verification business |
| **Contraintes** | Templates pre-approuves pour messages sortants initiatifs. Limit 1000 msg/jour (tier 1), extensible. Facturation uniquement sur livraison reussie. |
| **Timeline** | S0 (72h) — webhook + envoi basique |

**Estimation cout WhatsApp mensuel** (100 utilisateurs beta, tarifs per-message 2025+) :
- 100 briefings/semaine (utility) : 400 msg × €0.025 = ~€10/mois
- 100 rappels × 6 jours (service window) : gratuit si dans 24h
- Frais BSP (360Dialog/Twilio) : €50-100/mois selon provider
- Total : ~€60-115/mois (dont ~€10 WhatsApp + ~€50-100 BSP)

### Email Parsing (v0.1 optionnel — Sprint 2)

| Aspect | Detail |
|--------|--------|
| **API** | Gmail API (labels + search) |
| **Auth** | OAuth 2.0 (scope `gmail.readonly`) |
| **Cout** | Gratuit |
| **Complexite** | Elevee — parsing emails ecole/medecin, NLP extraction |
| **Donnees** | Confirmations RDV, emails ecole, notifications activites |
| **Timeline** | S2 (optionnel) |

### Doctolib (v1 — hors MVP)

| Aspect | Detail |
|--------|--------|
| **API** | Pas d'API publique. Scraping interdit par CGU. |
| **Alternative** | Partenariat officiel (Doctolib Partners) ou parsing emails confirmation |
| **Cout** | Partenariat = negotiation. Email parsing = gratuit. |
| **Complexite** | Elevee (partenariat) / Moyenne (email parsing) |
| **Timeline** | M4-M6 post-MVP |

---

## 5. Contrat d'Autonomie IA — Implementation

### Niveaux d'autonomie MVP (00-framing.md §2.3)

| Niveau | Label | Implementation MVP | Exemple concret |
|--------|-------|-------------------|-----------------|
| **1 — Suggest** | IA informe | Briefing hebdo, rappels quotidiens | "Mercredi foot = journee chargee" |
| **2 — Draft** | IA prepare, parent valide | Taches implicites detectees, suggestions | "Maillot a laver mardi ?" → Sophie confirme |
| **3 — Execute** | IA agit, parent supervise | HORS MVP. Opt-in apres 4+ semaines. | Prise RDV auto Doctolib (v1+) |

### Regles de progression

```
SEMAINES 1-3 : Niveau 1 uniquement
  → IA observe, suggere, apprend les patterns familiaux
  → Aucune action automatique

SEMAINE 4+ : Proposition Niveau 2
  → Message WhatsApp : "Je remarque que tu laves toujours le maillot
    le mardi. Veux-tu que je te le rappelle automatiquement ?"
  → Sophie repond OUI → rappel automatique active
  → Sophie repond NON → IA continue en Niveau 1

MOIS 3+ (v1) : Proposition Niveau 3 (opt-in explicite)
  → "Veux-tu que je prenne le RDV pediatre automatiquement
    quand un creneau se libere ?" (necessite Doctolib)
  → Confirmation obligatoire avant execution
  → Parent peut revoquer a tout moment
```

### Mecanismes de feedback

| Mecanisme | Implementation | Donnees collectees |
|-----------|---------------|-------------------|
| **Pouce haut/bas** | Boutons WhatsApp sous chaque briefing | Pertinence du briefing |
| **Correction textuelle** | "Non, le foot c'est jeudi pas mercredi" | Erreurs IA a corriger |
| **Silence** | Briefing non lu apres 24h | Desengagement, ajuster contenu |
| **Commande "moins"/"plus"** | "Moins de detail" / "Plus de detail" | Calibration verbosity |

### Transparency Log

Chaque action IA est tracable et visible :

```
Semaine du 24 fev — Journal RESPIRE
---
• Dim 19h : Briefing genere a partir de 8 events Google Calendar
• Lun 7h : Rappel envoye (3 priorites extraites)
• Mar 18h : Tache implicite detectee "laver maillot" (source : event "Foot 18h" + pattern historique)
• Mer 7h : Rappel adapte (jour charge detecte : 4 events)
• Jeu 9h : Sophie a corrige "dentiste = 11h pas 10h" → calendrier mis a jour

Donnees utilisees : Google Calendar (8 events)
Donnees NON utilisees : emails, SMS, localisation
Prochaine revue autonomie : semaine 4
```

Le parent peut demander "Montre-moi ce que tu as utilise" a tout moment via WhatsApp.

---

## 6. RGPD — Implementation Technique

### Privacy by Design (art. 25 RGPD)

#### Donnees traitees et classification

| Donnee | Type RGPD | Stockage | Retention | Justification |
|--------|-----------|----------|-----------|---------------|
| Prenom parent | Ordinaire | PostgreSQL EU | Duree abonnement | Personnalisation briefing |
| Email Google | Ordinaire | PostgreSQL EU | Duree abonnement | Auth OAuth |
| Numero WhatsApp | Ordinaire | PostgreSQL EU | Duree abonnement | Canal communication |
| Events calendrier | Ordinaire | PostgreSQL EU | 6 mois glissants | Generation briefings |
| Nb/ages enfants | Ordinaire | PostgreSQL EU | Duree abonnement | Contextualisation |
| Briefings generes | Ordinaire | PostgreSQL EU | 3 mois | Historique + amelioration |
| Feedback (pouces) | Ordinaire | PostgreSQL EU | 3 mois | Amelioration IA |
| Donnees sante | **Sensible (art. 9)** | NON collectee MVP | N/A | Hors scope MVP |

**Principe : pas de donnees sensibles au MVP.** Les calendriers sont des donnees ordinaires. Les donnees sante enfants (vaccins, allergies) sont exclues du MVP (opt-in futur avec consentement supplementaire).

#### Pseudonymisation avant envoi Claude API

```
AVANT envoi a Claude API :
  "RDV pediatre Emma jeudi 10h, foot Lucas mercredi 18h"
       ↓ Pseudonymisation
  "RDV pediatre [enfant_1] jeudi 10h, foot [enfant_2] mercredi 18h"

Claude genere le briefing avec pseudonymes.

APRES reception :
  "[enfant_1]" → "Emma", "[enfant_2]" → "Lucas"
  Briefing personnalise envoye sur WhatsApp.

Cles de de-pseudonymisation : stockees PostgreSQL EU uniquement.
Anthropic ne recoit JAMAIS de prenoms reels ni de numeros de telephone.
```

### Flux consentement technique

```
INSCRIPTION (page web onboarding) :

1. Consentement calendrier (obligatoire pour le service)
   ☐ "J'autorise RESPIRE a lire mes evenements Google Calendar
      pour generer des briefings hebdomadaires."
   → Base legale : contrat (art. 6.1.b) + consentement (art. 6.1.a)

2. Consentement WhatsApp (obligatoire pour le service)
   ☐ "J'autorise RESPIRE a m'envoyer des messages via WhatsApp."
   → Base legale : contrat

3. Consentement amelioration IA (optionnel)
   ☐ "J'autorise l'utilisation anonymisee de mes feedbacks
      pour ameliorer le service." (toggle, non pre-coche)
   → Base legale : consentement

4. PAS de consentement sante (hors MVP)
   → Sera ajoute en v1 si module medical active

Chaque consentement = horodatage + IP + preuve stockee.
```

### Droit d'effacement (art. 17)

```
FLUX SUPPRESSION :

1. Sophie envoie "SUPPRIMER MON COMPTE" sur WhatsApp
   OU clique "Supprimer" sur page web profil

2. RESPIRE confirme : "Es-tu sure ? Toutes tes donnees seront
   supprimees sous 30 jours. Tu recevras une confirmation."

3. Delai de grace : 7 jours (Sophie peut annuler)

4. Apres 7 jours : script automatise
   → DELETE calendars WHERE user_id = X
   → DELETE briefings WHERE user_id = X
   → DELETE feedbacks WHERE user_id = X
   → DELETE user WHERE id = X
   → Revoquer token OAuth Google
   → Log de suppression (preuve CNIL) conserve 12 mois

5. Confirmation WhatsApp : "Tes donnees ont ete supprimees.
   Merci d'avoir utilise RESPIRE."
```

### DPIA — Checklist simplifiee MVP

Le MVP declenche 3-4 criteres CNIL (donnees enfants indirectes, IA nouvelle technologie, transferts hors-EU, profiling). DPIA recommandee mais simplifiee car pas de donnees sante.

| Critere CNIL | Score MVP | Justification |
|-------------|-----------|---------------|
| Donnees sensibles (sante) | NON | Hors scope MVP |
| Donnees vulnerables (enfants indirects) | OUI | Ages, prenoms pseudonymises |
| Profiling / decision auto | PARTIEL | Suggestions IA, pas de decision |
| Transferts hors-EU | OUI | Claude API (US) — pseudonymisation |
| Nouvelle technologie (IA) | OUI | LLM generatif |
| Surveillance systematique | NON | Pas de tracking temps reel |

**Verdict** : 3 criteres = DPIA recommandee (pas obligatoire si sante exclue). Budget : 2-3K EUR avec template CNIL + review juriste.

### Budget compliance estime

| Poste | Cout | Quand |
|-------|------|-------|
| DPIA simplifiee (template CNIL + juriste) | 2 000-3 000 EUR | Avant beta publique |
| DPA Anthropic (inclus dans contrat API) | 0 EUR | S0 |
| CGU + Politique confidentialite (juriste) | 1 500-2 000 EUR | Avant beta publique |
| Audit RGPD post-launch (optionnel) | 3 000-5 000 EUR | M3-M6 |
| **Total MVP** | **3 500-5 000 EUR** | |

---

## 7. Analytics & Metriques

### North Star Metric

**Briefings lus par semaine par utilisateur actif**

Justification : un briefing lu = une semaine ou Sophie a utilise RESPIRE pour anticiper. C'est le proxy direct de la valeur delivree (reduction charge mentale).

### Supporting Metrics

| Metrique | Type | Cible MVP |
|----------|------|-----------|
| Weekly Active Users (WAU) | Engagement | +10% MoM |
| Taux ouverture briefing | Engagement | >80% |
| Messages reponse par briefing | Engagement | >0.5 (1 ajustement sur 2 briefings) |
| Temps onboarding → premier briefing | Activation | <5 min |
| Taux conversion free → premium | Revenue | 15-25% a M3 |
| Churn mensuel | Retention | <10% |

### Events cles a tracker (PostHog)

| Event | Trigger | Proprietes |
|-------|---------|------------|
| `user_signup` | Onboarding complete | source, nb_enfants, calendar_type |
| `calendar_connected` | OAuth Google valide | nb_events_synced |
| `whatsapp_linked` | Premier message recu | — |
| `briefing_sent` | Briefing envoye dimanche | nb_events, nb_taches_implicites |
| `briefing_read` | Message vu (read receipt WhatsApp) | delay_minutes |
| `briefing_response` | Sophie repond au briefing | response_type (ajout/suppression/question) |
| `daily_reminder_sent` | Rappel matin envoye | nb_priorites |
| `daily_reminder_read` | Rappel lu | delay_minutes |
| `feedback_given` | Pouce haut/bas | sentiment, briefing_id |
| `autonomy_upgrade` | Sophie accepte niveau 2 | from_level, to_level |
| `subscription_start` | Passage premium | plan, price |
| `user_churned` | 14 jours sans ouverture | last_active, total_briefings |

### Funnel

```
Inscription (100%)
    │ Cible : 70% completent
    ▼
Onboarding complete (70%)
    │ Cible : 90% recoivent briefing S1
    ▼
1er briefing recu (63%)
    │ Cible : 80% lisent
    ▼
1er briefing lu (50%)  ← AHA MOMENT
    │ Cible : 60% reviennent S2
    ▼
2e semaine active (30%)
    │ Cible : 80% continuent M1
    ▼
Mois 1 actif (24%)
    │ Cible : 25% convertissent premium
    ▼
Premium M1 (6%)
    │ Cible : 80% retention M3
    ▼
Premium M3 (5%)
```

---

## 8. Sprint Plan

### S0 — Setup technique (72h)

| Jour | Tache | Critere done |
|------|-------|-------------|
| J1 | Setup projet Node.js/Hono + PostgreSQL Neon + Drizzle schema | `pnpm dev` fonctionne, migrations OK |
| J1 | WhatsApp Cloud API : webhook entrant + envoi message test | "Hello World" recu sur WhatsApp |
| J2 | Google Calendar OAuth : page Next.js onboarding + token storage | Sophie connecte son calendar, events recus |
| J2 | BullMQ + Upstash Redis : job scheduling test | Job planifie s'execute a l'heure prevue |
| J3 | Pipeline bout-en-bout : Calendar → pseudonymisation → Claude API → briefing test | Briefing genere a partir d'events reels |
| J3 | Deploy Scaleway + Vercel EU | Tout tourne en production |

**Definition of Done S0** : Un utilisateur connecte Google Calendar → recoit un briefing WhatsApp test genere par Claude.

### S1 — Onboarding + 1er briefing (7 jours)

| Tache | Detail |
|-------|--------|
| Page onboarding finalisee | OAuth Google, formulaire preferences, lien WhatsApp |
| Briefing generation v1 | Template prompt Claude, extraction events, taches implicites basiques |
| Rappel quotidien v1 | 3 priorites du jour extraites du briefing |
| Conversation WhatsApp basique | "Ajoute X", "Retire Y", "Detail Z" |
| Feedback : pouces haut/bas | Boutons interactifs WhatsApp |
| Logging + monitoring | PostHog events, error tracking |

**Definition of Done S1** : 5 testeurs internes completent le cycle complet inscription → briefing dimanche → rappels lundi-samedi → feedback.

### S2 — Personnalisation + feedback loop (7 jours)

| Tache | Detail |
|-------|--------|
| Taches implicites ameliorees | Patterns : "foot mercredi" → "maillot mardi", "pediatre" → "carnet vaccins" |
| Personnalisation briefing | Ajustement ton/longueur selon feedback (plus/moins de detail) |
| Microsoft Calendar support | OAuth Microsoft Graph API |
| Score charge semaine | Indicateur 1-10 base sur nb events + complexite |
| Page profil web | Modifier preferences, voir historique, supprimer compte |
| RGPD : export donnees + suppression | Boutons fonctionnels |

**Definition of Done S2** : Briefings personnalises avec taches implicites pertinentes. Testeurs internes disent "c'est utile".

### S3 — Beta privee 20-30 testeurs (14 jours)

| Semaine | Actions |
|---------|---------|
| S3-W1 | Recrutement 20-30 Sophie-type (CSP+, IDF, 2+ enfants) via groupes WhatsApp parentalite |
| S3-W1 | Onboarding assiste (appel 5 min si besoin) |
| S3-W1 | Monitoring intensif : chaque briefing review manuellement |
| S3-W2 | Collecte feedback structure : NPS, interview 15 min (3-5 testeurs) |
| S3-W2 | Iterations rapides sur prompts Claude, timing, contenu |
| S3-W2 | Decision go/no-go pour beta ouverte |

**Criteres go/no-go** :

| Critere | Go | No-go |
|---------|-----|-------|
| Taux ouverture briefing S2+ | >70% | <50% |
| NPS beta | >30 | <10 |
| Testeurs disant "je continuerais a payer" | >50% | <30% |
| Bugs critiques | 0 | >2 non resolus |
| Feedback "ca m'a aide a anticiper" | >60% testeurs | <40% |

### Plan 90 jours — Roadmap post-MVP

```
MOIS 1 (Sprints 0-3) : MVP + Beta privee
  v0.1 : Google Calendar + WhatsApp + briefing hebdo + rappels quotidiens
  Objectif : 20-30 beta testeurs, validation product-market fit

MOIS 2 (Sprints 4-5) : Beta ouverte + Monetisation
  v0.2 : Module repas basique (suggestion 5 menus/semaine)
         Onboarding simplifie (auto-detection events)
         Freemium gate (free = 1 briefing/semaine, 1 enfant)
         Premium a 6.99EUR/mois (multi-enfants, rappels quotidiens, repas)
  Objectif : 100 utilisateurs, 10-15 premium

MOIS 3 (Sprints 6-7) : Croissance + Module Couple
  v0.3 : Notifications partenaire (Task Visibility Engine basique)
         Referral WhatsApp ("Partage le numero a une amie")
         SEO : 5 articles "comment organiser semaine famille"
         Micro-influenceurs : 10 contacts
  Objectif : 300+ utilisateurs, 30+ premium, CAC <5EUR
```

---

## 9. Protocole Test Utilisateur

### Script test 15 minutes

**Profil recrutement** : Sophie-type (mere 30-40 ans, CSP+, 2+ enfants, couple, IDF, utilisatrice Google Calendar + WhatsApp)

**Canaux recrutement** :
- Groupes WhatsApp parentalite IDF (3-5 groupes identifies)
- Instagram DM sur comptes parentalite (20 contacts)
- Bouche-a-oreille : demander aux 5 premiers testeurs de recommander 2 amies

**Introduction (2 min)**

> "Merci d'avoir accepte. On developpe un outil pour aider les parents a anticiper leur semaine. Pas de bonne ou mauvaise reponse — on veut ton avis honnete. Ca dure 15 min."

**5 questions (7 min)**

1. "Decris-moi comment tu prepares ta semaine le dimanche soir." (Comprendre le comportement actuel)
2. "Qu'est-ce que tu oublies le plus souvent ?" (Identifier les vrais pain points)
3. "Si un assistant t'envoyait un message dimanche soir avec ta semaine, qu'est-ce qu'il devrait contenir ?" (Valider le format du briefing)
4. "Montre-moi le briefing test [ecran WhatsApp]. Qu'est-ce qui te parle ? Qu'est-ce qui manque ?" (Feedback contenu)
5. "A 6.99EUR/mois, est-ce que tu t'abonnerais ? Pourquoi ?" (Validation WTP)

**3 taches (5 min)**

1. "Connecte ton Google Calendar via cette page." (Test onboarding — chronometre : objectif <3 min)
2. "Lis ce briefing WhatsApp et dis-moi ce que tu ferais." (Test comprehension — observe reactions)
3. "Reponds au bot pour ajouter un event." (Test conversation — "Ajoute dentiste jeudi 10h")

**Debrief (1 min)**

> "Sur 10, quelle est la probabilite que tu recommandes ca a une amie ? Pourquoi ?"

### Criteres go/no-go (post-test)

| Metrique | Go | Pivot | Kill |
|----------|-----|-------|------|
| NPS (Q debrief) | >40 | 20-40 | <20 |
| Onboarding <3 min | >80% testeurs | 50-80% | <50% |
| "Je paierais 6.99EUR" | >50% | 30-50% | <30% |
| "Ca m'aide a anticiper" | >70% | 50-70% | <50% |
| Comprehension briefing | >90% (intuitif) | 70-90% | <70% |

---

## 10. Risques & Mitigations

### Risques techniques

| Risque | Probabilite | Impact | Mitigation |
|--------|-------------|--------|-----------|
| **WhatsApp rate limits** (1000 msg/jour tier 1) | Moyen | Haut | Demander upgrade tier 2 des beta ouverte. SMS fallback via Twilio. |
| **Latence Claude API** (>5s reponse) | Faible | Moyen | Pre-generer briefings en batch (dimanche 18h). Cache prompts via prompt caching (-90%). |
| **Google Calendar OAuth revocation** | Faible | Haut | Notification parent + re-auth simplifiee. Monitoring quotidien tokens. |
| **WhatsApp policy change** (Meta restreint bots) | Faible | Critique | Architecture multi-canal des v0.2 (SMS Twilio, email). Pas de dependance exclusive. |
| **Downtime Scaleway** | Tres faible | Moyen | Health checks, alerting, migration possible vers OVH/Fly.io. |

### Risques produit

| Risque | Probabilite | Impact | Mitigation |
|--------|-------------|--------|-----------|
| **Faible adoption pere (Karim)** | Moyen | Moyen | MVP cible Sophie uniquement. Module couple v0.3. Framing neutre "co-pilote famille". |
| **Briefings non pertinents** | Moyen | Haut | Feedback loop (pouces). Iteration prompts hebdomadaire pendant beta. Human review des 50 premiers briefings. |
| **Notification fatigue** | Moyen | Moyen | Max 1 briefing/semaine + 1 rappel/jour. Opt-out par type. Horaires configurables. |
| **"Encore un outil a gerer"** | Moyen | Haut | WhatsApp = zero friction (pas d'app). Briefing passif (Sophie lit, pas besoin d'agir). |
| **Valeur percue trop faible pour payer** | Moyen | Haut | Freemium genereux. Beta gratuite 2 mois. Iterer sur valeur avant monetisation. |

### Risques legaux (06-legal-ethics)

| Risque | Probabilite | Impact | Mitigation |
|--------|-------------|--------|-----------|
| **RGPD non-conformite** | Faible (si DPIA faite) | Critique | DPIA avant beta publique. DPA Anthropic signe. Pseudonymisation. Juriste RGPD consulte. |
| **Donnees enfants mal protegees** | Faible | Critique | Pas de donnees sante MVP. Prenoms pseudonymises avant Claude. Consentement explicite parental. |
| **Transferts hors-EU (Claude API)** | Moyen | Moyen | Pseudonymisation + SCC avec Anthropic. Roadmap : Claude EU endpoint quand disponible. |
| **Conseil sante interpretatif** | Faible | Haut | JAMAIS de conseil medical. Disclaimer dans CGU + briefings. "Ceci n'est pas un avis medical." |

### Risques business

| Risque | Probabilite | Impact | Mitigation |
|--------|-------------|--------|-----------|
| **WTP insuffisant a 6.99EUR** | Moyen | Haut | Tester 4.99EUR en parallele. B2B2C mutuelles (v1). |
| **Concurrence Google/Apple** | Faible (12-18 mois) | Haut | Moat : personnalisation familiale + habitude WhatsApp + donnees contextuelles accumulees. |
| **CAC > LTV** | Faible | Critique | WhatsApp viral = CAC 2-4EUR. LTV 50-70EUR a 12 mois. Ratio sain 10-14x. |

---

## 11. Budget & Resources

### Couts infrastructure MVP (3 mois)

| Poste | Mensuel | 3 mois | Detail |
|-------|---------|--------|--------|
| **Scaleway DEV1-S** | 15 EUR | 45 EUR | 2 vCPU, 2GB RAM, Paris |
| **Neon PostgreSQL** (Free → Pro) | 0-19 EUR | 0-57 EUR | Free tier suffit beta, Pro si >100 users |
| **Upstash Redis** (Free tier) | 0 EUR | 0 EUR | 10K commandes/jour suffit |
| **Vercel** (Hobby → Pro) | 0-20 EUR | 0-60 EUR | Page onboarding, hobby suffit beta |
| **PostHog** (Free tier) | 0 EUR | 0 EUR | 1M events/mois gratuit |
| **Domaine + DNS** | 1 EUR | 3 EUR | respire.app ou respire-weekly.fr |
| **Total infra** | **16-55 EUR** | **48-165 EUR** | |

### Couts API (3 mois, 100 utilisateurs beta)

| API | Calcul | Mensuel | 3 mois |
|-----|--------|---------|--------|
| **Claude Haiku 4.5** | 100 users × 4 briefings/mois × ~1400 tokens = 560K tokens/mois | ~$1.50 | ~$4.50 |
| **Claude Haiku** (rappels) | 100 users × 24 rappels/mois × ~400 tokens = 960K tokens/mois | ~$1.50 | ~$4.50 |
| **Claude Haiku** (conversations) | 100 users × 8 messages/mois × ~600 tokens = 480K tokens/mois | ~$0.75 | ~$2.25 |
| **WhatsApp Cloud API** | 400 msg utility/mois × $0.02 | ~$8 | ~$24 |
| **Google Calendar API** | Gratuit | $0 | $0 |
| **Total API** | | **~$12/mois** | **~$35** |

### Budget total MVP (3 mois)

| Categorie | Cout | Note |
|-----------|------|------|
| **Infrastructure** | 50-165 EUR | Scaleway + Neon + Vercel |
| **APIs** | 30-35 EUR | Claude + WhatsApp |
| **RGPD / Legal** | 3 500-5 000 EUR | DPIA + CGU + juriste |
| **Domaine / divers** | 50 EUR | DNS, outils |
| **Total (sans dev)** | **3 630-5 250 EUR** | |

### Timeline solo developer vs equipe

| Config | Timeline MVP | Cout dev | Recommandation |
|--------|-------------|---------|----------------|
| **Solo founder (toi)** | 5-6 semaines (S0-S3) | 0 EUR | Si competences Node.js/API. Viable. |
| **1 dev freelance senior** | 4 semaines | 8 000-12 000 EUR | Accelere de 30%. Recommande si non-dev. |
| **Equipe 2 (dev + product)** | 3 semaines | 15 000-20 000 EUR | Optimal mais overhead communication. |
| **Agence/studio** | 6-8 semaines | 20 000-35 000 EUR | Non recommande (iteration lente, pas owner). |

**Recommandation** : 1 dev freelance senior Node.js/TypeScript (4 semaines, 8-12K EUR) + toi en product/test. Budget total MVP : **12 000-17 000 EUR** tout compris.

---

## Sources

| Ref | Fichier | Usage dans ce document |
|-----|---------|----------------------|
| 00 | 00-framing.md | Niveaux autonomie IA, taxonomie taches, grille scoring |
| 04 | 04-personas.md | Sophie (WTP, journee type, aha moment, canaux) |
| 05 | 05-irritants-opportunities.md | Irritants #1 #3 #6, solutions IA, workflows |
| 06 | 06-legal-ethics.md | RGPD, DPIA, DPA, transferts hors-EU, risques ethiques |
| 07 | 07-brand-psychology.md | Archetypes EVERYMAN+SAGE, 6 pieges, naming RESPIRE |
| 08 | 08-top3-ideas.md | Score 9.00, scope MVP, business model, GTM |
| WA | WhatsApp Business API Pricing (2026) | Couts messaging par categorie |
| CL | Claude API Pricing (2026) | Haiku 4.5 : $1/$5 par M tokens |
