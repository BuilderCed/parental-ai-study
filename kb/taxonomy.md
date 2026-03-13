# Taxonomie — IA & Charge Mentale Parentale

> Base de connaissance consultable | Version 1.0 | 23 fevrier 2026
> Source principale : 00-framing.md §2 | Sources complementaires : 04-personas.md

---

## 1. Taxonomie des Taches Parentales

### 1.1 Taches Visibles (~20% du poids reel)

> Definition : Taches observables, delegables, reconnues par les deux partenaires.

```
TACHES VISIBLES
├── Domestique (quotidien)
│   ├── Menage (aspirateur, rangement)
│   ├── Lessive (lancer, etendre, plier)
│   ├── Vaisselle
│   └── Rangement general
│
├── Repas (3x/jour)
│   ├── Planification + decision menu
│   ├── Courses
│   ├── Preparation / cuisson
│   └── Mise en table + debarrasser
│
├── Transport (quotidien)
│   ├── Ecole (matin + soir)
│   ├── Activites extra-scolaires
│   └── Medecins / specialistes
│
└── Hygiene enfants (quotidien)
    ├── Bain / douche
    ├── Habillage
    ├── Brossage dents
    └── Coiffure / toilette
```

### 1.2 Taches Invisibles (~80% du poids reel)

> Definition : Taches cognitives non observables, portees en grande partie par les meres (71%).

```
TACHES INVISIBLES
├── Anticipation (continue — difficulte delegation : TRES ELEVEE)
│   ├── RDV medicaux (carnet vaccins, specialistes, PMI)
│   ├── Fournitures scolaires (rentree, renouvellement)
│   ├── Vetements par saison (tailles, stocks)
│   ├── Anniversaires (camarades, famille, cadeaux)
│   └── Permissions ecole (collecte, signature, retour)
│
├── Planification repas (hebdomadaire — difficulte delegation : ELEVEE)
│   ├── Menus semaine (contraintes: regime, gouts, budget)
│   ├── Liste courses (stock frigo, placard)
│   ├── Gestion stocks (peremption, reapprovisionnement)
│   └── Regimes speciaux (allergies, convictions)
│
├── Admin scolaire (variable — difficulte delegation : MOYENNE)
│   ├── Permissions + autorisations
│   ├── Inscriptions activites
│   ├── Suivi devoirs + agenda
│   └── Communication professeurs
│
├── Admin sante (mensuelle — difficulte delegation : ELEVEE)
│   ├── Carnet de vaccinations
│   ├── Gestion ordonnances
│   ├── Suivi specialistes (kineto, ortho, psy)
│   └── Renouvellements medicaments
│
├── Coordination couple (continue — difficulte delegation : TRES ELEVEE)
│   ├── Qui fait quoi / quand
│   ├── Relances partenaire
│   ├── Negociation taches
│   └── Visibilite de la charge (asymetrie percue)
│
├── Charge emotionnelle (continue — non-delegable partiellement)
│   ├── Consoler / ecouter enfants
│   ├── Gestion conflits fratrie
│   ├── Soutien partenaire
│   └── Propre regulation emotionnelle
│
├── Logistique activites (hebdomadaire — difficulte delegation : MOYENNE)
│   ├── Inscriptions + renouvellements
│   ├── Gestion horaires
│   ├── Covoiturage
│   └── Equipement (achat, entretien)
│
└── Anticipation saisonniere (trimestrielle — difficulte delegation : ELEVEE)
    ├── Vacances scolaires (planning, reservations)
    ├── Changement garde-robe (tri, achat tailles suivantes)
    └── Rentree scolaire (liste, courses, preparation)
```

---

## 2. Niveaux d'Autonomie IA (Echelle 0-4)

> Source : 00-framing.md §2.3 — Contrat d'autonomie recommande MVP : niveaux 1-2

```
NIVEAU 0 — AUCUN (Status quo actuel)
└── Parent fait tout manuellement
    └── Aucune assistance IA

NIVEAU 1 — SUGGEST (Recommande MVP)
├── IA suggere → parent decide ET execute
├── Exemples concrets :
│   ├── "Semaine chargee : voici 5 menus rapides"
│   ├── "Lucas a un RDV dentiste dans 2 semaines, penser a confirmer"
│   └── "Semaine prochaine : 3 anniversaires camarades d'Emma"
└── Risque : faible | Confiance requise : faible

NIVEAU 2 — DRAFT (Recommande MVP)
├── IA prepare → parent valide (modifier si besoin)
├── Exemples concrets :
│   ├── Liste courses generee automatiquement → parent modifie + valide
│   ├── Brouillon email professeur pre-redige → parent envoie
│   └── Proposition repartition taches semaine → couple valide
└── Risque : faible-moyen | Confiance requise : moyenne

NIVEAU 3 — EXECUTE (Post-MVP, opt-in explicite uniquement)
├── IA agit → parent supervise et peut annuler
├── Exemples concrets :
│   ├── RDV pediatre pris automatiquement via Doctolib → parent confirme
│   ├── Commande courses automatique → parent valide avant expedition
│   └── Rappel partenaire envoye automatiquement
└── Risque : moyen | Confiance requise : haute | Prerequis : opt-in explicite

NIVEAU 4 — AUTONOME (Hors scope MVP — risques RGPD + ethiques)
├── IA gere → parent informe (apres coup)
├── Exemples theoriques :
│   ├── Renouvellement ordonnance automatique + notification
│   └── Repartition taches couple sans validation
└── Risque : eleve | RGPD : problematique | Confiance requise : tres haute
```

### Matrice Niveau x Tache

| Type de tache | Niveau 1 possible | Niveau 2 possible | Niveau 3 possible |
|---------------|:-----------------:|:-----------------:|:-----------------:|
| Planification menus | Oui | Oui | Non (gouts variables) |
| Liste courses | Oui | Oui | Oui (avec confirmation) |
| RDV medicaux | Oui (rappel) | Oui (brouillon demande) | Oui (prise RDV Doctolib) |
| Permissions scolaires | Oui (rappel) | Oui (brouillon) | Non (signature requise) |
| Coordination couple | Oui (suggestion) | Oui (proposition) | Non (tension emotionnelle) |
| Charge emotionnelle | Non (humain requis) | Non | Non |

---

## 3. Segmentation des Personas

### 3.1 Axes de Segmentation

> Source : 04-personas.md §framework

```
AXE 1 — STRUCTURE FAMILIALE
├── Couple (2 parents theoriquement 50-50)
│   ├── Standard (Sophie + Karim)
│   └── Recompose (Claire & Thomas — 2 foyers, 5 enfants)
├── Solo parent (charge 100% sur 1 personne)
│   ├── Separe/e (Nadia — pere absent)
│   └── Divorce co-parenting actif (expansion Y+1)
└── Diaspora (reseau elargi, multi-culturel, multi-pays)
    └── Biculturel (Aminata — FR + Senegal)

AXE 2 — CHARGE MENTALE PERCUE (critere primaire)
├── "Je pense a tout" (>80% taches invisibles portees)
│   └── Sophie : archetype — anticipation constante 24/7
├── "Je dois demander" (partenaire n'anticipe pas)
│   └── Karim : ne voit pas ce qu'il ne voit pas
├── "Seul(e) a decider" (aucun co-responsable)
│   └── Nadia : 35 decisions/jour sans co-parent
└── "Personne ne voit mon effort" (reconnaissance nulle)
    └── Aminata : effort invisible + double culture

AXE 3 — RAPPORT A LA TECHNOLOGIE
├── App-savvy / app-fatiguee
│   └── Sophie : 8+ apps quotidien, tolerance onboarding : <15 min
├── Pragmatique / sceptique
│   └── Karim : tech worker, mais resist apps "feminines"
├── Prudente / trust-dependante
│   └── Nadia : budget serre, crainte jugement
└── Trust-builder (adoption lente, culturelle)
    └── Aminata : WhatsApp-native, confiance avant adoption
```

### 3.2 Criteres de Segmentation Secondaires

| Critere | Impact sur persona | Exemple |
|---------|-------------------|---------|
| Age des enfants 0-3 ans | Impredictibilite max (sommeil, sante) | Lucas 4 ans (Sophie) |
| Age des enfants 3-6 ans | Transition scolaire, social, activites | Yasmine 3 ans (Aminata) |
| Age des enfants 6-12 ans | Logistics peak, devoirs, activites | Emma 7 ans (Sophie) |
| Age des enfants 12-18 ans | Charge emotionnelle, autonomie | Non dans personas MVP |
| CSP+ (cadres, professions sup.) | Stress + perfectionnisme + WTP eleve | Sophie, Karim |
| CSP (employe, ouvrier) | Mode survie + contrainte budget | Nadia, Aminata |
| Urbain (Paris, Lyon, etc.) | Transport + horaires + app culture | Sophie, Karim, Nadia, Aminata |
| Rural | Distance, isolement, services reduits | Hors MVP |
| 2 temps pleins | Asymetrie charge maximale | Sophie + Karim |
| Freelance | Revenus instables + flexibilite | Nadia |
| Temps partiel | Pression financiere + presence | Hors MVP principal |
| Famille proche disponible | Charge partagee possible | Sophie (partielle) |
| Isolement reseau | Charge totale sur personne | Nadia, Aminata |
| Gen X (1965-1980) | Sceptique tech, resist apps | Hors MVP |
| Millennial (1981-1996) | App-native, WTP moyen | Sophie, Karim, Nadia, Aminata |

### 3.3 Matrice de Positionnement des Personas

```
                     SUPPORT RESEAU
                    Eleve        Faible
                   ╔══════════════════╗
      DOULEUR       ║  Sophie (6-7/10)  Nadia (9-10/10)
      ELEVEE        ║  Karim (5-6/10)   Marc (9/10)
                    ║  Aminata (8-9/10) ║
                    ║                   ║
      DOULEUR       ║  Hugo+Valerie      Primo-parent
      FAIBLE        ║  (3-4/10)         isole (7-8/10)
                    ╚══════════════════╝

PRIORITE MVP : Quadrant haut-gauche (Sophie + Karim) + haut-droit (Nadia)
EXPANSION Y+1 : Aminata, Marc, Claire & Thomas
```

### 3.4 Tableau Comparatif des Personas Principaux

| Attribut | Sophie | Karim | Nadia | Aminata |
|----------|--------|-------|-------|---------|
| Age | 36 ans | 38 ans | 33 ans | 35 ans |
| Structure | Couple | Couple | Solo | Couple diaspora |
| Enfants | 2 (7+4 ans) | 2 (8+5 ans) | 1 (5 ans) | 2 (6+3 ans) |
| CSP | CSP+ | CSP+ | CSP | CSP |
| Revenue menage | €65-85k | €75-95k | €32-40k | €50-65k |
| Douleur principale | Anticipation + asymetrie | Ne voit pas ce qu'il ne voit pas | Isolement decisionnel | Double culture |
| Douleur intensite | 9/10 | 6/10 | 10/10 | 9/10 |
| WTP mensuel | €9.99-19.99 | €7.99-14.99 | €3.99-9.99 | €6.99-12.99 |
| Tech literacy | Haute | Tres haute | Moyenne | Moyenne |
| Canal acquisition #1 | Bouche-a-oreille amies | Peer tech / podcast | Groupes Facebook solo | WhatsApp diaspora |
| Feature MVP prioritaire | Anticipation + equite couple | Dashboard equity | Mode solo parent validation | Calendrier biculturel |
| Aha moment | Voir charge visualisee | Voir ecart donnees | Se sentir vue sans jugement | Voir 2 mondes synchronises |
| Retention driver | Reduction friction couple | Reconnaissance | Communaute + validation | Resonance culturelle |

### 3.5 Anti-Personas (Ne pas cibler)

| Anti-persona | Raison d'exclusion |
|-------------|-------------------|
| Luddites / tech-resistant | Cout acquisition > revenu possible |
| Familles avec nanny full-time | Charge mentale minimale, probleme different |
| Solo parent aise avec reseau fort | Pain level faible, perception "pity" app |
| Modele patriarcal strict | Positionnement "equite" = non-pertinent |

---

## 4. Segmentation par Etapes de Vie Parentale

| Etape | Age enfant | Charge mentale specifique | Personas concernes | Features prioritaires |
|-------|-----------|--------------------------|-------------------|----------------------|
| Nouveau-ne / nourrisson | 0-1 an | Sommeil, sante, identite, couple | Valerie & Hugo (MVP futur) | Sleep tracker, PPD support, couple reconnexion |
| Tout-petit | 1-3 ans | Impredictibilite, isolation, sante | Sophie (Lucas 4yo young), Nadia | Dev milestones, sante, validation |
| Maternelle | 3-6 ans | Transition scolaire, social, bilinguisme | Sophie, Aminata | School sync, activites, bilingue |
| Primaire | 6-12 ans | Logistics peak, devoirs, activites, social | Sophie (Emma 7yo), Claire | Multi-activites, devoirs, permissions |
| Adolescence | 12-18 ans | Emotionnel, autonomie, academic | Hors MVP | Hors scope actuel |

---

> Taxonomie basee sur 00-framing.md §2 + 04-personas.md | 23 fevrier 2026
