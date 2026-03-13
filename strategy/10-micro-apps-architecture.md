# 10 — RESPIRE Weekly : Decomposition en Micro-Applications

> **Date** : 24 fevrier 2026
> **Auteur** : Product Architect
> **Inspiration** : Architecture OpenClaw (Hub-and-Spoke, plugins, channel adapters)
> **Philosophie** : Unix "Do one thing well" + Composable Architecture
> **Produit** : RESPIRE Weekly — reconstitue a partir de micro-apps ultra-specialisees

---

## Executive Summary

Au lieu de construire RESPIRE Weekly comme un monolithe, on le decompose en **8 micro-applications independantes** qui, mises bout a bout via un Gateway central, reconstituent l'experience complete. Chaque micro-app est :

- **Ultra-specialisee** : une seule responsabilite, un seul domaine
- **Deployable independamment** : testable, remplacable, scalable seule
- **Communicante** : via un bus d'evenements (event-driven architecture)
- **Open-source-able** : chaque brique peut etre reutilisee dans d'autres projets

Cette approche s'inspire directement d'[OpenClaw](https://github.com/openclaw/openclaw), qui decompose un assistant IA personnel en Gateway + Channel Adapters + Agent Runtime + Tools + Plugins, chaque composant etant independant et extensible.

---

## Architecture Globale

```
                    RESPIRE WEEKLY — Composable Architecture
                    =========================================

  ┌─────────────┐     ┌─────────────┐     ┌─────────────┐
  │  WhatsApp   │     │    SMS      │     │   Email     │
  │  Adapter    │     │  Adapter    │     │  Adapter    │
  │ (micro-app  │     │ (micro-app  │     │ (micro-app  │
  │  #1)        │     │  #1b)       │     │  #1c)       │
  └──────┬──────┘     └──────┬──────┘     └──────┬──────┘
         │                   │                   │
         └──────────────┬────┴────┬──────────────┘
                        │        │
                        ▼        ▼
              ┌──────────────────────────┐
              │     GATEWAY / BUS        │
              │     (micro-app #0)       │
              │                          │
              │  • Message routing       │
              │  • Session management    │
              │  • Event orchestration   │
              │  • Auth & permissions    │
              └──────────┬───────────────┘
                         │
         ┌───────┬───────┼───────┬───────┬───────┐
         │       │       │       │       │       │
         ▼       ▼       ▼       ▼       ▼       ▼
      ┌──────┐┌──────┐┌──────┐┌──────┐┌──────┐┌──────┐
      │CAL   ││BRIEF ││CHAT  ││NUDGE ││ANON  ││FEED  │
      │SYNC  ││GEN   ││NLP   ││      ││      ││BACK  │
      │#2    ││#3    ││#4    ││#5    ││#6    ││#7    │
      └──────┘└──────┘└──────┘└──────┘└──────┘└──────┘

      Calendar  Briefing  Chat    Rappels  Pseudo-  Feedback
      Sync      Generator Handler Quotidiens nymizer  Loop
```

---

## Les 8 Micro-Applications

### Micro-App #0 — `respire-gateway`

**Responsabilite unique** : Orchestration, routing, session management

| Aspect | Detail |
|--------|--------|
| **Role** | Control plane central (inspire du Gateway OpenClaw) |
| **Input** | Messages normalises de tous les channel adapters |
| **Output** | Evenements routes vers les micro-apps appropriees |
| **Stack** | Node.js 22+ / Hono / WebSocket |
| **Donnees** | Sessions actives, registre micro-apps, file d'attente |

**Fonctions** :
- Registre de micro-apps (discovery, health check)
- Routing des messages entrants vers le bon handler
- Orchestration des workflows multi-apps (ex: sync cal → generer briefing → envoyer)
- Gestion des sessions utilisateur (auth, etat, preferences)
- Cron scheduler (dimanche 19h = briefing, 7h = rappels)
- Event bus (BullMQ/Redis)

**Analogie OpenClaw** : Le Gateway `ws://127.0.0.1:18789` qui coordonne tous les composants.

**Complexite** : Moyenne | **Sprint** : S0 | **Effort** : 3-5 jours

---

### Micro-App #1 — `respire-channel-whatsapp`

**Responsabilite unique** : Adapter WhatsApp ↔ format interne normalise

| Aspect | Detail |
|--------|--------|
| **Role** | Channel adapter (inspire des Channel Adapters OpenClaw) |
| **Input** | Webhooks WhatsApp Cloud API (messages entrants) |
| **Output** | Messages normalises vers Gateway + messages WhatsApp sortants |
| **Stack** | Node.js / WhatsApp Cloud API |
| **Donnees** | Aucune persistee (stateless, juste transforme) |

**Fonctions** :
- Reception webhook Meta (validation, parsing)
- Normalisation messages entrants → format unifie `{userId, text, timestamp, metadata}`
- Envoi messages sortants (templates approuves, messages libres dans 24h)
- Gestion read receipts, delivery status
- Rate limiting Meta API (1000 msg/jour tier 1)

**Pourquoi separe** : Si Meta change son API ou bloque le compte, on branche un adapter SMS ou Telegram sans toucher au reste. Exactement comme OpenClaw qui a des adapters Telegram, Discord, WhatsApp, Slack independants.

**Variantes futures** :
- `respire-channel-sms` (fallback Twilio)
- `respire-channel-telegram` (expansion)
- `respire-channel-email` (digest hebdo)

**Complexite** : Faible | **Sprint** : S0 | **Effort** : 2-3 jours

---

### Micro-App #2 — `respire-cal-sync`

**Responsabilite unique** : Synchroniser les calendriers externes → BDD interne

| Aspect | Detail |
|--------|--------|
| **Role** | Connecteur calendrier (Tool plugin dans le vocabulaire OpenClaw) |
| **Input** | Tokens OAuth utilisateurs |
| **Output** | Evenements normalises en BDD |
| **Stack** | Node.js / Google Calendar API v3 / Microsoft Graph API |
| **Donnees** | PostgreSQL : table `events` (titre, date, lieu, recurrence) |

**Fonctions** :
- OAuth 2.0 flow (Google, Microsoft)
- Sync initiale (importer events 2 semaines a venir)
- Sync incrementale (webhook push Google + poll 6h fallback)
- Normalisation multi-provider → schema unifie `{title, start, end, location, source}`
- Detection evenements recurrents (patterns)
- Token refresh automatique (background job)

**Pourquoi separe** : Le calendrier est la source de donnees critique. Si on ajoute Apple Calendar (CalDAV), Doctolib, ou un calendrier scolaire, on etend cette micro-app sans toucher au briefing generator.

**Variantes futures** :
- `respire-cal-apple` (CalDAV)
- `respire-cal-doctolib` (scraping/API)
- `respire-cal-school` (pronote, ENT)

**Complexite** : Moyenne | **Sprint** : S0 | **Effort** : 3-5 jours

---

### Micro-App #3 — `respire-briefing-gen`

**Responsabilite unique** : Generer un briefing intelligent a partir d'events + contexte

| Aspect | Detail |
|--------|--------|
| **Role** | Agent IA coeur (equivalent du Agent Runtime OpenClaw / Pi Agent Core) |
| **Input** | Events semaine (de cal-sync) + profil user + historique feedbacks |
| **Output** | Briefing structure (texte formate WhatsApp) |
| **Stack** | Node.js / Claude API (Haiku 4.5) / Prompt templates |
| **Donnees** | PostgreSQL : table `briefings` (contenu genere, metadata) |

**Fonctions** :
- Assemblage du contexte : events + profil + feedbacks precedents + patterns detectes
- Pseudonymisation pre-envoi (delegue a micro-app #6)
- Appel Claude API avec prompt structure :
  - Extraire les 3-5 priorites
  - Detecter taches implicites ("foot mercredi → maillot a laver mardi")
  - Calculer score charge semaine (1-10)
  - Generer message WhatsApp-friendly (<500 chars)
- De-pseudonymisation post-reception
- Utilisation Batch API Claude (-50% cout) pour briefings planifies

**Prompt engineering** :
```
Tu es l'assistant RESPIRE. Genere un briefing hebdomadaire pour [parent].
REGLES :
- Max 5 priorites, classees par urgence
- Detecte au moins 1 tache implicite non-ecrite dans le calendrier
- Ton = bienveillant, pas directif. "Pense a..." pas "Tu dois..."
- Score charge semaine 1-10
- Format WhatsApp (emojis parcimonieus, listes, gras)
```

**Pourquoi separe** : C'est le coeur de valeur. On peut iterer sur les prompts, changer de modele IA (Claude → Mistral → local), ou A/B tester des formats de briefing sans toucher au reste.

**Complexite** : Haute | **Sprint** : S0-S1 | **Effort** : 5-8 jours

---

### Micro-App #4 — `respire-chat-handler`

**Responsabilite unique** : Comprendre et repondre aux messages conversationnels

| Aspect | Detail |
|--------|--------|
| **Role** | NLP conversationnel (equivalent des Tool Plugins OpenClaw) |
| **Input** | Messages texte libres du parent (via Gateway) |
| **Output** | Actions (ajout event, correction, question, feedback) |
| **Stack** | Node.js / Claude API / Intent classification |
| **Donnees** | PostgreSQL : table `conversations` (historique court-terme) |

**Fonctions** :
- Classification d'intent :
  - `ADD_EVENT` : "Ajoute dentiste jeudi 10h" → creer event dans cal-sync
  - `CORRECT` : "Non c'est vendredi pas jeudi" → corriger event
  - `ASK_DETAIL` : "Detail mercredi ?" → generer vue jour
  - `FEEDBACK` : "Trop long le briefing" → stocker dans feedback-loop
  - `DELETE` : "Retire le foot" → supprimer event
  - `ACCOUNT` : "SUPPRIMER MON COMPTE" → lancer flux RGPD
- Gestion du contexte conversationnel (3-5 messages window)
- Reponses en langage naturel (Claude API, ~200 tokens out)
- Fallback : "Je n'ai pas compris. Tu peux reformuler ?"

**Pourquoi separe** : Le chat est une feature distinct du briefing. On peut le desactiver, le limiter, ou le complexifier (ajout commandes vocales) independamment.

**Complexite** : Moyenne | **Sprint** : S1 | **Effort** : 3-5 jours

---

### Micro-App #5 — `respire-nudge-engine`

**Responsabilite unique** : Envoyer les rappels quotidiens au bon moment

| Aspect | Detail |
|--------|--------|
| **Role** | Scheduler intelligent de micro-rappels |
| **Input** | Events du jour (de cal-sync) + preferences utilisateur |
| **Output** | Messages rappel formattés → Gateway → Channel adapter |
| **Stack** | Node.js / BullMQ (cron jobs) |
| **Donnees** | PostgreSQL : preferences horaires, historique rappels |

**Fonctions** :
- Cron job quotidien (heure personnalisee, default 7h)
- Selection top 3 priorites du jour (depuis events + taches implicites)
- Formatage message court (<200 chars, WhatsApp-optimise)
- Logique de non-repetition (pas de rappel pour event deja passe)
- Adaptation horaire (jour charge = rappel plus tot, jour calme = pas de rappel)
- Gestion "silence" (si parent ne lit jamais les rappels → reduire frequence)

**Pourquoi separe** : Les rappels ont une logique temporelle propre (cron, horaires, frequence) distincte du briefing hebdo. On pourrait ajouter des nudges "soir" ou "mid-journee" sans refactorer.

**Complexite** : Faible | **Sprint** : S1 | **Effort** : 2-3 jours

---

### Micro-App #6 — `respire-anonymizer`

**Responsabilite unique** : Pseudonymisation/de-pseudonymisation des donnees avant envoi IA

| Aspect | Detail |
|--------|--------|
| **Role** | RGPD privacy layer (pas d'equivalent direct OpenClaw — specifique RESPIRE) |
| **Input** | Texte contenant des donnees personnelles |
| **Output** | Texte pseudonymise (pre-IA) ou de-pseudonymise (post-IA) |
| **Stack** | Node.js / regex + mapping table |
| **Donnees** | PostgreSQL : table `pseudonym_map` (user_id, real_name, pseudo) |

**Fonctions** :
- `anonymize(text, userId)` : remplace prenoms enfants par `[enfant_1]`, `[enfant_2]`
- `anonymize(text, userId)` : retire numeros telephone, emails, adresses
- `deanonymize(text, userId)` : restaure les vrais prenoms dans le briefing genere
- Gestion du mapping : creation automatique lors de l'onboarding
- Audit log : tracer chaque operation de pseudonymisation (CNIL compliance)
- Jamais de persistance de donnees reelles dans les logs IA

**Pourquoi separe** : La couche privacy est NON-NEGOCIABLE et doit etre testable independamment. Si la CNIL demande un audit, on montre cette micro-app isolee avec ses tests et son audit trail.

**Complexite** : Faible | **Sprint** : S0 | **Effort** : 1-2 jours

---

### Micro-App #7 — `respire-feedback-loop`

**Responsabilite unique** : Collecter, stocker et exploiter les feedbacks utilisateur

| Aspect | Detail |
|--------|--------|
| **Role** | Learning loop (inspire du Memory Plugin OpenClaw) |
| **Input** | Pouces haut/bas, corrections textuelles, silences detectes |
| **Output** | Signaux pour ameliorer briefing-gen et nudge-engine |
| **Stack** | Node.js / PostgreSQL |
| **Donnees** | PostgreSQL : table `feedbacks` (type, content, briefing_id, timestamp) |

**Fonctions** :
- Reception et stockage des feedbacks (pouces, corrections, commandes "moins"/"plus")
- Detection des silences (briefing non lu apres 24h → signal desengagement)
- Agregation hebdomadaire : quels types de taches implicites sont utiles vs ignorees
- Fourniture de contexte au briefing-gen : "Sophie prefere les briefings courts, ignore les rappels meteo"
- Calcul NPS (enquete trimestrielle via WhatsApp)
- Export pour analytics (PostHog events)

**Pourquoi separe** : Le feedback loop est ce qui rend RESPIRE intelligent avec le temps. Isoler cette logique permet de l'iterer rapidement sans risquer le briefing generation.

**Complexite** : Faible | **Sprint** : S2 | **Effort** : 2-3 jours

---

## Mapping Micro-Apps → Sprints

```
SPRINT S0 (72h — Fondations)
├── #0 respire-gateway .............. Routing + cron + event bus
├── #1 respire-channel-whatsapp .... Webhook Meta + envoi messages
├── #2 respire-cal-sync ............ OAuth Google + sync events
├── #3 respire-briefing-gen ........ V1 prompt + Claude API
└── #6 respire-anonymizer .......... Pseudonymisation pre/post IA

SPRINT S1 (7 jours — Experience complete)
├── #3 respire-briefing-gen ........ Iteration prompt + taches implicites
├── #4 respire-chat-handler ........ Intent classification + reponses
├── #5 respire-nudge-engine ........ Rappels quotidiens 7h
└── #2 respire-cal-sync ............ + Microsoft Calendar

SPRINT S2 (7 jours — Intelligence)
├── #7 respire-feedback-loop ....... Pouces, corrections, adaptation
├── #3 respire-briefing-gen ........ Personnalisation via feedbacks
├── #5 respire-nudge-engine ........ Adaptation frequence intelligente
└── #4 respire-chat-handler ........ Commandes avancees

SPRINT S3 (14 jours — Beta privee)
├── Tous les modules en production
├── Monitoring + alerting (PostHog)
├── 20-50 beta testeurs (Sophie-type)
└── Iteration rapide sur prompts + UX
```

---

## Communication Inter-Apps (Event Bus)

```
Evenements publies sur le bus Redis/BullMQ :

CALENDAR_SYNCED        → #2 publie quand sync terminee
  └─→ #3 consomme : "nouveaux events, re-generer briefing si dimanche"
  └─→ #5 consomme : "events demain changes, ajuster rappel"

BRIEFING_GENERATED     → #3 publie quand briefing pret
  └─→ #0 consomme : router vers channel adapter
  └─→ #7 consomme : initialiser tracking feedback

MESSAGE_RECEIVED       → #1 publie quand message WhatsApp entrant
  └─→ #0 consomme : classifier et router
  └─→ #4 consomme : si message conversationnel
  └─→ #7 consomme : si feedback (pouce, correction)

FEEDBACK_RECEIVED      → #7 publie quand feedback traite
  └─→ #3 consomme : ajuster profil pour prochain briefing

NUDGE_SENT            → #5 publie quand rappel envoye
  └─→ #7 consomme : tracker ouverture

USER_CREATED          → #0 publie quand inscription complete
  └─→ #2 consomme : lancer sync calendrier
  └─→ #6 consomme : creer mapping pseudonymes
```

---

## Avantages de la Decomposition

| Critere | Monolithe | Micro-Apps RESPIRE |
|---------|-----------|-------------------|
| **Deploiement** | Tout ou rien | Deployer #3 seul apres iteration prompt |
| **Test** | Integration complexe | Chaque app testable isolement |
| **Remplacement** | Refactoring massif | Changer Claude → Mistral = modifier #3 seul |
| **Multi-canal** | Rewrite | Ajouter adapter #1b SMS sans toucher au reste |
| **Compliance** | Audit global | Montrer #6 anonymizer a la CNIL isolement |
| **Scaling** | Vertical | Scale #3 horizontalement (GPU-intensive) |
| **Equipe** | Tous sur tout | 1 dev par micro-app |
| **Open-source** | Difficile | Chaque micro-app = repo independant |

---

## Risques et Mitigations

| Risque | Impact | Mitigation |
|--------|--------|-----------|
| Complexite operationnelle | Sur-engineering pour un MVP solo | Deployer comme **monorepo avec modules** (pas Docker separe au MVP). Microservices physiques a M6+. |
| Latence inter-apps | Briefing lent si trop de hops | Event bus Redis local (<1ms). Pipeline sync pour le workflow briefing. |
| Debugging distribue | Tracer un bug entre 3 apps | Correlation ID par request. Logs centralises (PostHog + console). |
| Over-abstraction | Trop d'interfaces pour peu de code | Pragmatisme : au MVP, les micro-apps sont des **modules TypeScript dans un monorepo**, pas des services separes. La separation est **logique**, pas **physique**. |

---

## Architecture Recommandee MVP : Monorepo Modulaire

```
respire-weekly/
├── packages/
│   ├── gateway/          # #0 — Orchestration
│   ├── channel-whatsapp/ # #1 — Adapter WhatsApp
│   ├── cal-sync/         # #2 — Calendar sync
│   ├── briefing-gen/     # #3 — IA briefing generator
│   ├── chat-handler/     # #4 — NLP conversationnel
│   ├── nudge-engine/     # #5 — Rappels quotidiens
│   ├── anonymizer/       # #6 — Pseudonymisation RGPD
│   ├── feedback-loop/    # #7 — Feedback collection
│   └── shared/           # Types, utils, DB schema (Drizzle)
├── apps/
│   └── onboarding/       # Next.js — page web unique
├── drizzle/              # Migrations DB
├── pnpm-workspace.yaml
├── turbo.json
└── package.json
```

**Principe** : separation logique au MVP (modules TypeScript dans un monorepo pnpm), separation physique en M6+ (Docker containers si scaling necessaire).

---

## Inspiration OpenClaw — Correspondances

| OpenClaw | RESPIRE Weekly | Role |
|----------|---------------|------|
| Gateway (WebSocket hub) | `respire-gateway` | Control plane, routing, sessions |
| Channel Adapters (Telegram, WhatsApp, Slack) | `respire-channel-whatsapp` + variantes | Normalisation messages multi-canal |
| Pi Agent Core (Agent Runtime) | `respire-briefing-gen` | Intelligence IA, generation contenu |
| Tool Plugins | `respire-cal-sync`, `respire-chat-handler` | Capabilities specifiques |
| Memory Plugin | `respire-feedback-loop` | Apprentissage et persistence contexte |
| Skills System | Prompts templates | Comportements configurables |
| AGENTS.md / SOUL.md | Personality config | Ton, style, regles du briefing |
| Session isolation | User sessions | Isolation donnees par utilisateur |

---

## Buddy (theonlybuddy.com) — Concurrent adjacent identifie

| Aspect | Detail |
|--------|--------|
| **Nom** | Buddy |
| **Pays** | France |
| **Tagline** | "Gere ta vie administrative... sans prise de tete" |
| **Cible** | Adultes avec charge administrative |
| **Features** | Rappels echeances admin, astuces personnalisees, priorisation taches, chatbot |
| **IA** | Chatbot avec personnalisation rappels/conseils |
| **Pricing** | Gratuit |
| **Equipe** | Celine, Clara, Mehdi |
| **Site** | theonlybuddy.com |
| **Analyse** | Adjacent mais PAS concurrent direct. Focus admin general (impots, demarches), pas parentalite ni charge mentale familiale. Pas de calendrier, pas d'anticipation, pas de couple/equite. Valide le besoin "assistant qui anticipe" mais sur un segment different. |

---

## Sources

- [OpenClaw — GitHub](https://github.com/openclaw/openclaw) — Architecture hub-and-spoke, plugins, channel adapters
- [OpenClaw Architecture Explained](https://ppaolo.substack.com/p/openclaw-system-architecture-overview) — Decomposition detaillee
- [Composable Architecture 2025](https://alokai.com/blog/composable-architecture) — Patterns modulaires
- [Unix Philosophy & Microservices](https://sumitgupta.dev/learnings/the-unix-philosophy-microservices-perfect-analogy-10-key-takeaways-lessons/) — "Do one thing well"
- [WhatsApp Microservices Architecture](https://www.chatarchitect.com/news/leveraging-microservices-for-scalable-whatsapp-integrations) — Patterns scalabilite
- [Buddy App](https://www.theonlybuddy.com/) — Concurrent adjacent FR

---

## Ecosysteme Steipete — Le vrai modele OpenClaw

### Contexte

[Peter Steinberger](https://github.com/steipete) (ex-fondateur PSPDFKit, rejoint OpenAI 2025) a cree une **dizaine de micro-outils CLI** qui, mis bout a bout, forment l'infrastructure de [OpenClaw](https://github.com/openclaw/openclaw) — un assistant IA personnel. Chaque outil fait UNE chose, est package en **Nix flake**, et fonctionne de maniere independante.

### Les 10 micro-outils steipete

| Outil | Responsabilite | Correspondance RESPIRE |
|-------|---------------|----------------------|
| **summarize** | Resume n'importe quel contenu (texte, URL, PDF) via LLM | `respire-briefing-gen` — meme logique de compression intelligente |
| **bird** | Client Bluesky (poster, lire, interagir) | `respire-channel-whatsapp` — adapter canal specifique |
| **imsg** | Lire/envoyer iMessages depuis le terminal | `respire-channel-*` — adapter canal natif |
| **peekaboo** | Capture screenshots macOS + analyse IA | Pas d'equivalent direct — monitoring visuel |
| **poltergeist** | Automatisation UI macOS (cliquer, taper, naviguer) | Pas d'equivalent — automatisation desktop |
| **sag** | Text-to-Speech via ElevenLabs CLI | Futur `respire-voice` si expansion vocale |
| **gogcli** | Client GOG Galaxy (jeux, bibliotheque) | Pas d'equivalent — domaine specifique |
| **goplaces** | Recherche Google Maps + infos lieux | `respire-cal-sync` variante — enrichissement events avec lieux |
| **camsnap** | Capture camera + analyse IA | Pas d'equivalent — capture visuelle |
| **sonoscli** | Controle Sonos depuis le terminal | Pas d'equivalent — domotique |

### Principes architecturaux steipete

```
1. UNIX PHILOSOPHY — Chaque outil fait UNE chose bien
   summarize ne sait que resumer. bird ne sait que Bluesky.
   → RESPIRE : chaque micro-app a UNE responsabilite unique.

2. NIX FLAKES — Packaging reproductible et compose
   Chaque outil est un flake independant dans nix-steipete-tools.
   → RESPIRE : chaque package dans le monorepo pnpm = un flake logique.

3. CLI-FIRST — Interface programmatique avant tout
   Pas de GUI, pas d'API REST complexe. Stdin/stdout.
   → RESPIRE : event bus Redis comme equivalent stdin/stdout.

4. COMPOSABLE — Les outils se chainent
   summarize < bird (resumer un thread Bluesky)
   peekaboo | summarize (capturer ecran + analyser)
   → RESPIRE : CALENDAR_SYNCED → briefing-gen → channel-whatsapp (pipeline events)

5. INDEPENDANCE TOTALE — Aucun outil ne depend d'un autre
   summarize fonctionne seul. bird fonctionne seul.
   → RESPIRE : respire-anonymizer fonctionne et se teste seul.
```

### Lecon cle pour RESPIRE

La force de l'approche steipete n'est pas la sophistication de chaque outil — c'est leur **composabilite**. `summarize` fait 200 lignes de code. `bird` fait 300. Mais enchaines via OpenClaw, ils forment un assistant personnel complet.

**Application RESPIRE** : ne pas sur-developper chaque micro-app. `respire-anonymizer` peut etre 50 lignes de regex + un mapping. `respire-nudge-engine` peut etre un cron BullMQ de 100 lignes. La valeur emerge de la **composition**, pas de la complexite individuelle.

### Mapping steipete → OpenClaw → RESPIRE

```
STEIPETE (micro-outils CLI)     OPENCLAW (assistant IA)        RESPIRE (assistant parental)
─────────────────────────────   ────────────────────────────   ──────────────────────────────
summarize                       Agent Core / LLM Runtime       respire-briefing-gen
bird, imsg                      Channel Adapters               respire-channel-whatsapp
peekaboo, camsnap               Input Plugins                  respire-cal-sync (input)
poltergeist                     Action Plugins                 respire-chat-handler (actions)
sag (ElevenLabs TTS)            Voice Output                   Future: respire-voice
goplaces                        Tool Plugins                   respire-cal-sync (enrichment)
nix-steipete-tools (flakes)     Gateway / Orchestration        respire-gateway
—                               Memory Plugin                  respire-feedback-loop
—                               —                              respire-anonymizer (RGPD)
```

### Difference cle steipete vs RESPIRE

| Aspect | Steipete/OpenClaw | RESPIRE |
|--------|------------------|---------|
| **Environnement** | macOS local, CLI | Cloud, WhatsApp API |
| **Utilisateur** | Developpeur power-user | Parent non-technique |
| **Interface** | Terminal/pipes | WhatsApp (zero friction) |
| **Donnees** | Locales | Cloud + RGPD (anonymizer obligatoire) |
| **Packaging** | Nix flakes | pnpm monorepo + modules TS |
| **Philosophie commune** | Do one thing well, composable, independant |

---

## Sources ajoutees

- [nix-steipete-tools](https://github.com/openclaw/nix-steipete-tools) — 10 micro-outils Nix flakes
- [steipete GitHub](https://github.com/steipete) — Profil + repos (summarize, bird, peekaboo, sag, etc.)
- Peter Steinberger rejoint OpenAI (2025), OpenClaw transition vers fondation

---

> **Decision** : Adopter l'architecture monorepo modulaire au MVP (separation logique), avec migration vers microservices physiques a M6+ si le scaling l'exige. Chaque micro-app a son propre repertoire, ses propres tests, et une interface claire (events in/out). S'inspirer de la philosophie steipete : outils simples (50-300 lignes), valeur par la composition, pas par la complexite individuelle.
