# 05 — Cartographie Irritants → Opportunités IA
## Charge Mentale Parentale : Mapping vers Solutions Concrètes

> **Date** : 23 février 2026  
> **Auteur** : Product Strategy, AI/Parental Tech  
> **Scope** : 20 irritants prioritaires × 4 niveaux autonomie IA × faisabilité technique  
> **Horizon** : MVP (v0 quick-wins) → v1 (high-impact medium-effort) → v2+ (transformationnel)

---

## SECTION 1 : MATRICE IRRITANT × OPPORTUNITÉ IA

### Vue d'ensemble

La matrice ci-dessous mappe les **20 irritants principaux** vers des **opportunités IA concrètes**, en tenant compte de :
- Capacités NLP/IA requises (classification, planning, recommendation, extraction)
- Niveaux d'autonomie (1-Suggest à 4-Autonome)
- Données d'entrée nécessaires
- Risques (RGPD, confiance, erreur IA)
- Faisabilité technique (1-10) et impact utilisateur (1-10)

---

## IRRITANT #1 : Anticipation Constante (45 mentions)

### Description détaillée du problème

**Verbatim clé** : *"C'est moi qui pense à tout : les RDV dentiste, que j'ai oublié la permission d'école, les fournitures, les anniversaires... mon mari ne demande jamais."*

Le parent doit maintenir une **simulation mentale continue** des besoins futurs : 
- RDV médicaux (pédiatre, dentiste, orthodontiste, spécialistes)
- Documents administratifs (carnet vaccination, assurance)
- Permissions scolaires et démarches école
- Changements saisonniers (vêtements, sports d'hiver/été)
- Anticipation repas/courses basée sur planning
- Anniversaires camarades, cadeaux

**Impact** : Hypervigilance cognitive 24/7. Insomnies (cerveau qui "tourne" la nuit). Sentiment de responsabilité écrasante.

---

### Opportunité IA #1.1 : "Anticipation View" (KILLER FEATURE)

#### Solution IA concrète

**Concept** : Tableau de bord affichant les 2 semaines à venir, agrégé par :
1. **RDV médicaux** (extraits de l'historique médicale digitalisée)
2. **Activités enfants** (école, sports, loisirs)
3. **Repas à planifier** + courses manquantes
4. **Documents à préparer** (permissions, carnet vaccins)
5. **Anniversaires enfants de l'école** (extraits liste classe)
6. **Transitions saisonnières** (rappel si passage à vêtements d'hiver)

**Trigger** : Notification quotidienne 7h : *"Semaine chargée détectée : 3 RDV + 4 activités. Voici l'anticipation du moment."*

#### Capacité IA requise

| Capacité | Description | Faisabilité |
|----------|-------------|------------|
| **Event extraction** | Parser calendrier Google Family, SMS/email RDV | 9/10 |
| **Knowledge assembly** | Combiner 3+ sources (cal + mail + SMS + contacts) | 8/10 |
| **Seasonality inference** | Détecter quand les enfants sortent de vêtements | 7/10 |
| **Personalization** | Apprendre les habitudes saisonnières de la famille | 7/10 |
| **Natural language briefing** | Résumer anticipation en prose lisible | 9/10 |

#### Niveau d'autonomie recommandé

**Niveau 2 (Draft)** initialement :
- IA construit la vue anticipation
- Parent valide, ajoute, supprime, ajuste
- Progression vers Niveau 3 après 4+ semaines (opt-in)

#### Données nécessaires (input)

| Source | Type | Comment intégrer |
|--------|------|------------------|
| **Google Calendar** (famille) | Events, RDV, activités | API Family Calendar |
| **Emails** | Confirmations RDV, messages école | Gmail API + parsing règles |
| **SMS** | Rappels RDV, notifications école | Twilio/Nexmo parsing (si autorisation) |
| **Calendrier scolaire** | Vacances, fêtes école, rentrée | ICS/iCal des écoles |
| **Liste classe** | Anniversaires enfants, événements | Import CSV ou API école (si disponible) |
| **Historique médical** | Prochain RDV, vaccinations dues | Doctolib API ou manuel |

#### Output attendu

```markdown
## Anticipation : Semaine du 23-29 février 2026

### 📋 RDV à anticiper
- **Lundi 24** : Pédiatre (10h) — Carnet vaccins à apporter
- **Mercredi 26** : Orthodontiste (14h) — Amener bonne chaussures
- **Vendredi 28** : Ophtalmologue (15h) — Ordonnance à renouveler avant

### 📚 Activités enfants
- **Lun-ven** : École (8h30-16h30)
- **Mercredi 26** : Foot (18h-19h) — Maillot lavé ?
- **Samedi 1er mars** : Anniversaire Eva (copine) — Cadeau ? (budget ~€15)

### 🍳 Repas à planifier
- Lundi : Restes poulet + salade
- Mardi : Pâtes bolognaise
- Mercredi : Rapide (foot le soir) → Pizzas ?
- Jeudi : [À remplir]
- Vendredi : [À remplir]

### 📦 Courses manquantes
- Œufs (quiche mercredi)
- Lait
- Pain
- Fruits (pommes, bananes)
- Produits hygiène enfant

### ⚡ Anticipation saisonnière
- Février → passages hiver → printemps : vérifier que short/T-shirt été sont rangés (passage courant)
- Vacances printemps dans 4 semaines : réserver gîte ?
```

#### Exemples de prompts/interactions

**User prompt 1** :
> *"Ajoute RDV dentiste jeudi 27 février 10h — anticipe ça pour moi"*

**IA response** :
> *"OK. J'ai ajouté le RDV dentiste. Voici anticipation mise à jour : 4 RDV cette semaine, 2 activités scolaires, repas à confirmer pour jeudi (dentiste après lunch = manger plus tôt ?)."*

**User prompt 2** :
> *"Mercredi soir c'est foot. Rappelle-moi de laver le maillot mardi."*

**IA response** :
> *"Maillot ajouté à liste tâches mardi. Anticipation : semaine physiquement chargée, 3 jours avec activités après école."*

#### Risques

| Risque | Mitigation |
|--------|-----------|
| **RGPD : données enfants** | Encryption end-to-end, retention 90j, consent explicite parents (CNIL guidelines) |
| **Erreur IA** (date mal parsée) | Validation humaine obligatoire avant notification (Niveau 2) |
| **Notification fatigue** | 1 notification/jour max, condensée, opt-in par type |
| **Trust break** (IA oublie RDV) | Fallback : user peut override tout moment + weekly audit log |

#### Score faisabilité & impact

| Métrique | Score | Justification |
|----------|-------|---------------|
| **Faisabilité technique** | **8/10** | API Google/email bien documentées, parsing NLP standard, RGPD surmontable |
| **Impact utilisateur** | **9/10** | Élimine ~40-50% du "mental load" cognitif (anticipation constante) |
| **Complexity d'implémentation** | **Medium** | 4-6 semaines dev (MVP) |
| **Priorité MVP** | **#1 (killer feature)** | Plus haut ROI, résout irritant #1, crée habitude |

---

## IRRITANT #2 : "Fallait Demander" — Délégation impossible (42 mentions)

### Description détaillée du problème

**Verbatim clé** : *"Je suis obligée de demander à chaque fois. 'Peux-tu donner son bain ?' 'Peux-tu préparer ses affaires pour l'école ?' Pourquoi ne 'voit' il pas ce qui doit être fait ?"*

Le partenaire (généralement père) ne voit pas les tâches non-explicites. Cela crée un double travail :
1. Identifier la tâche
2. Formuler la demande
3. Vérifier qu'elle est faite
4. Corriger si mal faite

**Impact émotionnel** : Sentiment de solitude (pas de co-parent impliqué), frustration de gérer quelqu'un d'autre. Perte d'intimité (management vs partnership).

---

### Opportunité IA #2.1 : "Task Visibility Engine" avec notifs partenaire

#### Solution IA concrète

**Concept** : Système qui détecte les tâches implicites et les rend explicites + envoie notifications au partenaire **sans passer par le parent** :

1. **Event-to-task conversion** : "RDV pédiatre jeudi" → tâche "Préparer carnet vaccins mardi"
2. **Implicit task detection** : "Mercredi foot à 18h" → tâche "Laver maillot" 
3. **Partenaire notification** : Envoyer notification au père directement (pas au parent gestionnaire)
4. **Load balancing** : Suggérer qui devrait faire quoi (basé sur emploi du temps)

#### Capacité IA requise

| Capacité | Description | Faisabilité |
|----------|-------------|------------|
| **Contextual task inference** | "RDV dentiste" → déduire 5-8 tâches préalables | 8/10 |
| **Timeline planning** | Calculer backoff : "RDV jeudi" → "Préparer doc mardi" | 7/10 |
| **Partenaire load awareness** | Parser emploi du temps couple, suggérer répartition | 7/10 |
| **Predictive task generation** | Apprendre patterns saisonniers, anticiper tâches | 6/10 |

#### Niveau d'autonomie recommandé

**Niveau 1-2 (Suggest → Draft)** :
- IA détecte tâches implicites
- Parent vérifie la liste avant envoi (pour éviter friction)
- Partenaire reçoit notification, confirme ou redirige

#### Données nécessaires

| Source | Type |
|--------|------|
| **Calendrier couple** | Emplois du temps combinés |
| **Historique tâches** | Patterns de qui fait quoi généralement |
| **Contexte RDV** | Type RDV → tâches préalables standard |
| **Enfants profils** | Ages, activités (foot vs danse ≠ préparation) |

#### Output attendu

```markdown
## Tâches implicites détectées pour semaine du 23-29 février

### 📝 Tâches pour toi (parent gestionnaire)
- [⚠️ VALIDATION] Préparer carnet vaccins pour RDV pédiatre lundi (doc stockée?)
- [✅] Commander cadeau anniversaire Eva (vendredi livraison?)

### 📤 À envoyer à [Partenaire]
- **Lundi soir** : Préparer affaires école mercredi (leçon EPS, tenue spéciale)
- **Mardi** : Laver maillot foot pour mercredi soir
- **Jeudi après RDV** : Pickup enfant à 16h école (ma journée chargée)

**Suggestion de répartition** (basé sur emplois du temps) :
- Toi : Tâches médicales, administratives (expertise)
- Lui : Tâches quotidiennes, pickups (Il moins occupé jeudi/vendredi)
```

#### Risques

| Risque | Mitigation |
|--------|-----------|
| **Couple friction** (partenaire reçoit "ordres" de l'app) | Reframing : "Avis" pas "ordre". Parent valide avant envoi. Partner peut contester/rediriger |
| **Tâches mal inférées** | Parent vérification manuelle (Niveau 1-2) avant notification |
| **Notification fatigue partenaire** | Max 3 notifs/jour, groupées par type, soft language |

#### Score faisabilité & impact

| Métrique | Score | Justification |
|----------|-------|---------------|
| **Faisabilité technique** | **7/10** | NLP + pattern matching classique, pas de technologie exotique |
| **Impact utilisateur** | **8/10** | Réduit friction couple, rend invisible visible, élève partenaire implication |
| **Priorité MVP** | **#2 (high impact, medium-high effort)** | Complément direct de #1 |

---

## IRRITANT #3 : Planification repas + courses (38 mentions)

### Description détaillée du problème

**Verbatim clé** : *"Les courses, les menus, c'est le poids. Je dois penser à ce qu'on va manger chaque soir, puis faire les courses, puis vérifier les allergies/régimes."*

Parents doivent :
1. Planifier menus 1-2 semaines (combien de temps ?)
2. Décider budget + régimes (gluten-free, végétarien, allergies)
3. Faire liste courses
4. Faire courses
5. Préparer les repas
6. Gérer stocks frigo (waste minimization)

**Friction spécifique** : Apps type Menus Semaine = trop de clics, pas intégrées avec ce qu'on a en stock, menus génériques pas adaptés budget/préférences.

---

### Opportunité IA #3.1 : "Meal Planning + Smart Grocery"

#### Solution IA concrète

**Concept** : IA génère menus personnalisés + liste courses automatique :

1. **Input family profile** : Budget/semaine, régimes (gluten-free, végétarien), allergies, préférences enfants
2. **Smart meal suggestions** : Basées sur saison + budget + temps (rapide vs slow-cooked)
3. **Inventory awareness** : Parser frigo (photo? inventaire manuel?), suggérer repas utilisant ce qu'on a
4. **Auto-grocery list** : Menus → liste courses formatée par rayon (layout marché)
5. **Notification** : "Shopping list prête, optimisée pour Casino près de toi" (si prix disponibles)

#### Capacité IA requise

| Capacité | Description | Faisabilité |
|----------|-------------|------------|
| **Recipe reasoning** | Générer menus adaptés profil | 9/10 |
| **Dietary constraint** | Respecter allergies, régimes | 9/10 |
| **Seasonality awareness** | Suggérer tomates en juillet, courges en septembre | 8/10 |
| **Inventory parsing** | Lire frigo (vision? liste?) | 7/10 |
| **Price optimization** | Adapter suggestions au budget | 6/10 |
| **Cultural preference** | Apprendre ce que la famille aime | 8/10 |

#### Niveau d'autonomie recommandé

**Niveau 2 (Draft)** :
- IA propose menus + liste courses
- Parent valide, modifie, supprime repas
- Pas autonome encore (Niveau 3 plus tard avec trust)

#### Données nécessaires

| Source | Type |
|--------|------|
| **Family preferences** | Régimes, allergies, cuisine aimée |
| **Frigo inventory** | Photo + parsing ou entrée manuelle |
| **Budget** | €/semaine |
| **Time availability** | Jours avec peu de temps (rapide) |
| **Kids profiles** | Ages (nourriture diverse si bébé) |
| **Recipe DB** | API recettes (Marmiton? Avec permissions) |

#### Output attendu

```markdown
## Proposition Menus + Courses — Semaine 24-29 février

### 📋 Menus proposés (Budget: €120/semaine, famille 4, repas 2 allergies arachide)

**Lundi 24** : Pâtes bolognaise (rapide 20min) 
- Ingrédients ✅ Tomate (en stock), viande (surgelé)
- À acheter : Pâtes fraîches, oignons

**Mardi 25** : Poisson pané + riz + carottes
- Budget: €8 | Rapide : 25min

**Mercredi 26** : Poulet rôti (slow cooker, préparé 15min le matin)
- ✅ Poulet congelé (j'ai vu) + pommes de terre
- + Salade

**Jeudi 27** : Restes poulet en salade + œufs
- ✅ Zéro achat (utiliser stock)

**Vendredi 28** : Pizzas maison (enfants aiment, samedi je dors après)
- À acheter : Farine, fromage râpé, sauce tomate
- Budget: €7

**Samedi 1er mars** : Quiche épinards + salade
- À acheter : Œufs, épinards, crème

**Dimanche 2** : Couscous merguez (rapide, conviviality)
- À acheter : Merguez, pois chiches (boîte)

### 🛒 Liste courses — Optimisée supermarché (Casino Decathlon)

**Fruits & Légumes** (€20)
- Oignons x2
- Carottes x1kg
- Épinards frais (ou surgelé?)
- Salade (laitue)
- Pommes de terre (5kg sac)
- Tomates (voir prix, sinon boîte)

**Viandes & Poisson** (€35)
- Poulet fermier 1.2kg (€5.50/kg) [CONGELÉ OK?]
- Poisson pané x4 (surgelé)
- Œufs x12 (€2.50)

**Féculents & Base** (€15)
- Pâtes fraîches 500g
- Riz blanc 1kg
- Farine 1kg (pizza)

**Produits laitiers** (€12)
- Fromage râpé 250g
- Crème fraîche 200g

**Épicerie & Basics** (€20)
- Sauce tomate 2x boîte
- Huile olive
- Sel, poivre
- Pois chiches x2 boîtes

**À vérifier en stock** :
- Beurre, lait (as needed)
- Surgelés poulet

### 💡 Notes IA
- **Budget estimé** : €118/semaine (dans budget ✅)
- **Temps de cuisine** : 3 jours rapides (20-25min), 2 jours normaux, 2 jours repas-stock
- **Allergy safe** : 0 arachides détectées ✅
- **Suggestion** : Acheter œufs cette semaine (mercredi quiche, samedi petit-déj)
```

#### Exemples de prompts

**User prompt 1** :
> *"Mercredi c'est chargé (foot 18h). Propose juste des repas super rapides ce jour."*

**IA response** :
> *"OK. Mercredi = pizzas surgelées + salade (rapide 10min). Vendredi = pizza maison (on compense). Liste courses mise à jour."*

**User prompt 2** :
> *"Ajoute 'végétarien' mercredi + jeudi, ma fille fait défi école."*

**IA response** :
> *"Mercredi pizza végétalienne (oignons, tomates, mozzarella). Jeudi = quiche épinards (déjà prévue\!). Pas d'achat supplémentaire."*

#### Risques

| Risque | Mitigation |
|--------|-----------|
| **Picky eaters** (enfants refusent suggestions) | Parent peut remplacer repas proposés. IA apprend ce que la fam aime (patterns) |
| **Inventory parsing** (hard) | Accepter entrée semi-manuelle : "J'ai du poulet congelé" |
| **Price data** (variable, non-fiable) | Ignorer prix précis si data absente; utiliser estimés moyennes France |

#### Score faisabilité & impact

| Métrique | Score | Justification |
|----------|-------|---------------|
| **Faisabilité technique** | **8/10** | Recipe APIs existantes (Marmiton, Yummly), NLP standard |
| **Impact utilisateur** | **8/10** | Élimine mental load majeur (30-40% du temps parental cognitif) |
| **Priorité MVP** | **#1 ou #2** | Très haut ROI, parents adorent |

---

## IRRITANT #4 : Manque d'initiative partenaire (38 mentions)

### Description détaillée du problème

**Verbatim clé** : *"Il faut que je dise : 'Va lui donner son bain', 'Prépare ses affaires demain'. Pourquoi ne prend-il pas initiative ?"*

Cela diffère d'irritant #2 ("Fallait demander") : c'est spécifiquement l'absence d'initiative spontanée. Parent doit manager le partenaire comme on gère une tâche.

**Psychologie sous-jacente** : Père se voit comme "helping" mère (pas comme co-responsable). Mère se voit comme "responsible" (pas "helping").

---

### Opportunité IA #4.1 : "Pro-active Partenaire Coach"

#### Solution IA concrète

**Concept** : IA envoie au partenaire des suggestions pro-actives de tâches, formatées pour l'encourager :

1. **Detect opportunities** : Mercredi foot à 18h → partenaire peut laver maillot mardi
2. **Timing-aware notifications** : Envoyer suggestion mardi soir ("Petit coup de frais d'1h: laver maillot?") vs cri de détresse mercredi matin
3. **Positive framing** : "Tu peux épargner 30min à [partenaire] en lavant le maillot" vs "Lave le maillot"
4. **Learning loop** : Si partenaire toujours oublie, ajuster frequency/framing ou demander parent d'intervenir
5. **Surprise mode** : Parfois, IA fait la tâche pour partenaire (décider quoi, puis il l'exécute) → sentiment de "j'ai pris une initiative"

#### Capacité IA requise

| Capacité | Description | Faisabilité |
|----------|-------------|------------|
| **Opportunity detection** | Identifier tâches que partenaire peut faire | 8/10 |
| **Behavioral psychology** | Framing pro-actif (pas accusation) | 7/10 |
| **Timing optimization** | Quand envoyer notification (pas trop tôt, pas trop tard) | 7/10 |
| **Learning compliance** | Adapter si partenaire ignore suggestions | 6/10 |
| **Role inversion** | Proposer tâches "au féminin" aussi (parité) | 7/10 |

#### Niveau d'autonomie recommandé

**Niveau 1 (Suggest)** :
- IA suggère au partenaire directement
- Partenaire peut accepter, reporter, ou rediriger
- Parent ne doit pas rappeler (IA le fait)

#### Données nécessaires

| Source | Type |
|--------|------|
| **Partenaire profil** | Emploi du temps, skills, préférences tâches |
| **Tâches historiques** | Qui fait quoi généralement (patterns) |
| **Enfants schedule** | Activités, RDV, timing |
| **Partenaire behavior** | Réactions passées aux suggestions (ignore? fait?) |

#### Output attendu

**Notification to father (Slack/SMS/App):**
```
🎯 Conseil express (30min)

Eva a foot mercredi 18h. Son maillot a peut-être besoin d'un coup de frais 👕

Mardi entre 19h-20h c'est idéal (tu es dispo, machine lavage libre).
Ça épargnerait ~20min à [mère] mercredi matin rush.

Plutôt lundi? Je peux changer suggestion.

[Accepter] [Plutôt demain] [Pas possible]
```

#### Exemples de prompts

**User prompt 1** (père) :
> *"Je suis pas dispo mardi, j'ai réunion."*

**IA response** :
> *"OK. Lundi soir 20h-21h? Ou mercredi matin 7h avant école? [Qui peux pas, fais lundi]"*

**User prompt 2** (mère, vue partenaire) :
> *"Il a ignoré la suggestion maillot lundi. Peux-tu être plus insistant?"*

**IA response** :
> *"Compris. Jeudi j'ai envoyé version 'urgent' si pas fait mercredi soir. Mais attention: trop insistant risque frustration. Préfère je parle avec lui directement (partenaire coaching)?"*

#### Risques

| Risque | Mitigation |
|--------|-----------|
| **Partenaire resent** (se sent microgéré) | Framing pro-actif crucial. Tested on behavior change psychology |
| **Mère frustration** (toujours partenaire oublie) | Si pattern persiste, cela révèle problème couple (pas IA) → suggest explicit conversation |
| **Gender bias** (IA suggère tâches "féminines" à père, "masculines" à mère) | Balanced suggestion pool; monitor IA bias |

#### Score faisabilité & impact

| Métrique | Score | Justification |
|----------|-------|---------------|
| **Faisabilité technique** | **7/10** | NLP + notification strategy |
| **Impact utilisateur** | **7/10** | Réduit friction avec partenaire, augmente implication |
| **Priorité MVP** | **#3-4** | Moyen-haut impact, mais dépend de données historiques solides |

---

## IRRITANT #5 : Perception d'équité illusoire (31 mentions)

### Description détaillée du problème

**Verbatim clé** : *"Mon mari pense qu'on partage 50-50 les tâches. Il compte une balade au parc comme 'sa' contribution."*

**Gap massif** : 65% des pères pensent équité vs 40% des mères. Pères comptent tâches visibles; mères pèsent tâches invisibles.

---

### Opportunité IA #5.1 : "Equity Dashboard" (couple visibility)

#### Solution IA concrète

**Concept** : IA génère visualisation d'équité couple :

1. **Task accounting** : Visible + invisible, pondérée par effort/temps
2. **Sentiment analysis** : Détecter ressenti d'équité vs réalité
3. **Couple report** : "Vous avez l'impression 50-50, mais distribution réelle est 30-70"
4. **Goal setting** : "Pour atteindre 50-50, [partenaire] doit prendre 40h tâches/mois"
5. **Recommendation** : Tâches spécifiques à redéfinir

#### Capacité IA requise

| Capacité | Description | Faisabilité |
|----------|-------------|------------|
| **Time tracking** | Logger tâches + durée (auto ou manuel) | 8/10 |
| **Effort weighting** | "Trier linge" (20min) vs "Anticiper repas mois" (60min) | 7/10 |
| **Sentiment sampling** | Periodic survey : "Te sens-tu overchargé?" | 6/10 |
| **Visualization** | Dashboard clair, pas accusatoire | 8/10 |

#### Niveau d'autonomie recommandé

**Niveau 1 (Suggest/Inform)** :
- IA collecte data (tâches + temps)
- Couple regarde ensemble dashboard
- IA suggère tâches à redéfinir (non-prescriptive)

#### Données nécessaires

| Source | Type |
|--------|------|
| **Task logging** | Qui a fait quoi, combien de temps (auto-tracked via app ou manual entry) |
| **Sentiment surveys** | "On équité?" (bi-weekly ou monthly) |
| **Calendar + activity data** | Work hours, commute, availability |

#### Output attendu

```markdown
## Équité Couple — Rapport bi-mensuel (23 fév - 9 mars 2026)

### 📊 Distribution réelle (heures/mois)

| Type tâche | Toi | Lui | Total | Idéal |
|-----------|-----|-----|-------|-------|
| **Tâches visibles** (cuisine, menage, shopping) | 60h | 15h | 75h | 37.5h |
| **Tâches invisibles** (anticipation, coordination, admin) | 80h | 5h | 85h | 42.5h |
| **Enfants direct** (bain, devoirs, jeux) | 40h | 35h | 75h | 37.5h |
| **Couple/maison** (couple intimacy time, finances, maintenance) | 10h | 20h | 30h | 15h |
| **TOTAL** | **190h** | **75h** | **265h** | **132.5h (50-50)** |

### 💔 Sentiment vs Réalité

| Personne | Perçoit | Réalité | Gap |
|----------|---------|---------|-----|
| **Toi** | "Je fais 70% du mental load" | **72%** ✅ | Perception juste |
| **Lui** | "Je fais 50-50 ou presque" | **28%** ❌❌ | **Perception écart 22%** |

### ⚡ Où est le déséquilibre?

**Tâches invisibles** = le vrai problème
- Anticipation + coordination: Tu 95%, Lui 5%
- Admin/documents: Tu 100%, Lui 0%
- Planning/décisions: Tu 90%, Lui 10%

**Tâches visibles** ne reflètent pas charge mentale réelle.

### 🎯 Pour atteindre 50-50 (réaliste en 8 semaines)

**Lui doit prendre** :
1. **Anticipation repas** (30min/jour planning) → Lui décide 2-3 menus/semaine
2. **Admin enfants** (4h/mois) → Lui gère un RDV entièrement (appel + suivi)
3. **Coordination school** (2h/mois) → Lui responsable de 1 enfant permissions/communication

**Toi peux réduire** :
- Mental load "contrôle" (deleguer confiance)
- Décisions hyper-triviales (Lui choisit snack du jour)

### 📝 Conversation starter
*"Regardons ce rapport ensemble. [Lui], tes yeux voient 50-50, mais la réalité est 28-72. Pas d'accusation — je veux te montrer où je suis écrasée et comment on peut vraiment partager."*
```

#### Risques

| Risque | Mitigation |
|--------|-----------|
| **Defensiveness** (Lui se sent accusé) | Frame comme "découverte mutuelle", pas jugement. Tone TRÈS neutre. |
| **Data accuracy** (Hard to track tâches invisibles) | Semi-manual approach: surveys + spot-checks, pas tracking obsessif |
| **Over-quantification** (Amour ≠ maths) | Dashboard incitatif but non-contractuel. Goal = conversation, pas enforcement |

#### Score faisabilité & impact

| Métrique | Score | Justification |
|----------|-------|---------------|
| **Faisabilité technique** | **6/10** | Tracking invisible = dur; requires human input |
| **Impact utilisateur** | **8/10** | Conversation-starter puissant; data-driven equity discussion |
| **Priorité MVP** | **#4-5** | Moyen-terme, excellent pour retention/satisfaction couple |

---

## IRRITANT #6 : Coordination RDV médicaux (32 mentions)

### Description détaillée du problème

**Verbatim clé** : *"Tous les RDV enfants : pédiatre, orthophoniste, dentiste... c'est moi qui gère."*

Parent doit :
1. Anticiper quand RDV est dû (tous les 12 mois? 6 mois?)
2. Chercher praticien disponible (sites health-system chaotiques)
3. Prendre RDV (appel? online?)
4. Noter dans calendrier
5. Relancer enfant la veille
6. Préparer documents (carnet vaccins, antécédents)
7. Aller au RDV
8. Garder trace résultats/suivis

**Friction spécifique** : Chaque praticien a un système différent (Doctolib, appel, email, site perso). Enfants (surtout ados) oublient RDV.

---

### Opportunité IA #6.1 : "Medical Coordination Hub"

#### Solution IA concrète

**Concept** : Système centralisé qui gère cycle complet RDV :

1. **Auto-schedule detection** : "Pédiatre dernier RDV 12 mois ago" → créer reminder "Il est temps"
2. **Unified booking** : Parser tous les praticiens de la région, consolider dispo (Doctolib + non-Doctolib)
3. **Auto-appointment** : Si possible, IA peut prendre RDV directement (Doctolib API) vs demander parent
4. **Preparation checklist** : "Carnet vaccins à apporter" → IA vérifie 24h avant, envoie notification
5. **Follow-up** : Après RDV, prompt parent "Résultats à noter?" → structurer infos enfant

#### Capacité IA requise

| Capacité | Description | Faisabilité |
|----------|-------------|------------|
| **Medical history reasoning** | Savoir quand chaque type RDV est dû | 8/10 |
| **Multi-system aggregation** | Connecter Doctolib + sites perso + appel hôpitaux | 6/10 |
| **Doctolib API** | Auto-booking si plugin disponible | 8/10 |
| **Preparation inference** | Savoir quoi prévoir pour quel type RDV | 8/10 |
| **Follow-up structuring** | Parser résultats RDV, noter antécédents | 7/10 |

#### Niveau d'autonomie recommandé

**Niveau 2-3 (Draft → Execute)** :
- Niveau 2 : IA finds appointments, parent confirms before booking
- Niveau 3 : IA auto-books Doctolib (if available), parent supervises

#### Données nécessaires

| Source | Type |
|--------|------|
| **Child health record** | Ages, RDV history, conditions, allergies |
| **Doctolib account** | API access for auto-booking |
| **Regional praticiens** | Database of pediatricians, dentists, etc. (Doctolib API + web scrape) |
| **Past appointments** | To learn frequency (annual checkup?) |

#### Output attendu

```markdown
## Suivi Médical — Enfants Eva & Tom

### 🚨 À faire MAINTENANT

**Eva — Pédiatre**: Dernier RDV juillet 2025 (8 mois ago)
- Statut: **À programmer** (annuel recommandé)
- Praticiens disponibles:
  - Dr. Benoit Fournier (Doctolib) — Dispo 27 fév 14h30 ✅
  - Dr. Sylvie Lefevre (Appel direct) — Dispo 1er mars
- **Action suggérée**: Doctolib pour Dr. Fournier 27 fév (mercredi ok pour toi?)
- À apporter: Carnet vaccins, allergies doc (il y a eu eczéma)

**Tom — Dentiste**: Dernier RDV janvier 2024 (13 mois ago) ⚠️⚠️ OVERDUE
- Statut: **Urgent**
- Praticiens:
  - Dr. Martine Dufour (Doctolib) — Dispo 3 mars 15h
  - Clinique Smile&Co (Appel) — Dispo 1er mars 16h
- À apporter: Antécédent appareil dentaire

### 📅 RDV programmés (2-3 mois avanc)

| Enfant | Praticien | Date | Heure | Status | Docs |
|--------|-----------|------|------|--------|------|
| Eva | Pédiatre Dr. Fournier | 27 fév | 14h30 | À confirmer | Carnet vaccins ✅ |
| Tom | Orthophoniste Dr. Stein | 24 fév | 10h | Confirmé | Dossier audio ✅ |

### ✅ Historique suivi (last 12 months)

| Enfant | Type | Praticien | Date | Notes |
|--------|------|-----------|------|-------|
| **Eva** | Pédiatre | Dr. Benoit F. | Juil 2025 | Tout OK, allergie saisonnière signalée |
| **Tom** | Ortho | Dr. Stein | Déc 2025 | Suivi dyslexie, progrès + |
| **Tom** | Optométriste | Dr. Rousseau | Sep 2025 | Lunettes OK, contrôle dans 1an |

### 📋 À-faire préparation

**Pour RDV jeudi 24 fév (Orthophoniste Tom):**
- [ ] Imprimer dossier suivi (IA l'a attaché)
- [ ] Rappeler Tom jeudi matin
- [ ] Départ 9h45 pour arriver 10h (15 min route)
```

#### Exemplesi de prompts

**User prompt 1** :
> *"Tom dent fait mal depuis 2 jours. Peux-tu chercher denti URGENTE ce week?"*

**IA response** :
> *"Cherche. Clinique Smile&Co dispo samedi matin 10h. Confirmer?"*

**User prompt 2** :
> *"Ajoute nouvelle allergie: Tom ne peut pas faire vaccin ROR, trop réactif."*

**IA response** :
> *"Noté. Pédiatre prochain contrôle sera alertée. Document allergie updated."*

#### Risques

| Risque | Mitigation |
|--------|-----------|
| **RGPD : données médicales enfants** | End-to-end encryption, retention 18 mois max, audit log, CNIL compliant |
| **API fragmentation** | Commencer avec Doctolib (80% praticiens), expand progressivement |
| **Wrong RDV timing** (IA calcule 12 mois but should be 6) | Parent can adjust; IA learns |

#### Score faisabilité & impact

| Métrique | Score | Justification |
|----------|-------|---------------|
| **Faisabilité technique** | **7/10** | Doctolib API bien documentée, data structuring standard |
| **Impact utilisateur** | **9/10** | Élimine friction major (15-20h/an par enfant) |
| **Priorité MVP** | **#1-2** | Très haut ROI, addresses pain point précis |

---

## IRRITANT #7 : Listes tâches invisibles (35 mentions)

### Description détaillée du problème

**Verbatim clé** : *"Mon mari ne 'voit' pas ce qui manque. Je dois tout lui dire explicitement."*

Différent d'irritant #2 car pas aussi spécifiquement sur "fallait demander" — c'est que les tâches ne sont pas visibles du tout pour le partenaire. Il ne sait pas qu'il y a une tâche à faire.

---

### Opportunité IA #7.1 : "Shared Task Visibility + Smart Delegation"

(Voir également Irritant #2.1)

Cette opportunité est largement couverte par #2.1 (Task Visibility Engine). Pour MVP, combiner #2.1 + #7.1 dans un single feature: **Tâches visibles + auto-recommandations délégation**.

---

## IRRITANT #8 : Gestion activités extra-scolaires (28 mentions)

### Description détaillée du problème

**Verbatim clé** : *"Inscrire, payer, se souvenir des horaires, organiser le covoiturage."*

Parent doit :
1. Inscrire enfants aux activités (appel école, site, etc.)
2. Payer (chèque, virement, paiement en ligne)
3. Noter horaires (mercredi 17h foot, jeudi 16h30 danse)
4. Organiser transport (Moi? Partenaire? Covoiturage?)
5. Rappeler enfant la veille (surtout ados)
6. Coordonner avec équipement (kit foot? chaussettes ballet?)

---

### Opportunité IA #8.1 : "Activity Management" + Carpooling Coordinator

#### Solution IA concrète

**Concept** : Intégration centralisant inscription + logistique + covoiturage :

1. **Activity discovery** : IA scrape activités locales (foot, danse, musique, codecademy) + horaires
2. **Family preference learning** : Apprendre ce que les enfants aiment
3. **Payment integration** : Automatiser paiements (si parent autorise)
4. **Carpooling solver** : Suggérer carpool avec parents école (logistique optimisée)
5. **Calendar integration** : Auto-ajouter à calendrier famille
6. **Reminders** : Équipement, horaires, changements

#### Capacité IA requise

| Capacité | Description | Faisabilité |
|----------|-------------|------------|
| **Local activity discovery** | Web-scrape activités région | 7/10 |
| **Child preference** | Apprendre ce qu'enfants aiment | 7/10 |
| **Logistics optimization** | Carpooling solver | 6/10 |
| **Payment automation** | API payment gateways | 7/10 |
| **Conflict detection** | "Foot 17h + danse 16h30 = conflit" | 8/10 |

#### Niveau d'autonomie recommandé

**Niveau 2-3** :
- Niveau 2 : IA finds activities, parent confirms + books
- Niveau 3 : IA auto-books payment (if authorized)

#### Données nécessaires

| Source | Type |
|--------|------|
| **School/community activity lists** | Scrape site école, mairie |
| **Child interest surveys** | "What do you want to do?" |
| **Family transport availability** | Who can drive when |
| **Payment methods** | Bank, card, etc. |
| **Calendar** | Existing activities to detect conflicts |

#### Output attendu

```markdown
## Activités Enfants — Suggestions & Calendrier

### 🎯 Suggestions pour Eva (8 ans, intérêt: sport + art)

**Option 1: Football** (matches her interest)
- Club: FC Decathlon, mercredi 17h-18h30
- Coût: €80/trimestre
- Lieu: À 12 min (drive) de maison
- Pros: Amies (Léa y va), populaire école
- Cons: Clashes with reading club thursday

**Option 2: Danse Créative**
- Association Mouvements, samedi 10h-11h
- Coût: €60/trimestre
- Lieu: À 8 min
- Pros: Créatif, amis differents groupe
- Cons: Samedi morning (toi dors?)

**Option 3: Coding (CodeCademy Club)**
- Lieu: À l'école, jeudi 16h30-17h30
- Coût: Gratuit (ecole subventionne)
- Pros: Gratuit, amis école, skill futur
- Cons: Jeudi busy day (aussi ortho tom)

### 🧩 Collision calendar détectée
**Si Eva foot mercredi 17h** + **Tom ortho mercredi 16h**:
- Tom finish 16h45 → Eva activité 17h = 15min margin
- Risk: Eva late to foot
- Solutions: 
  1. Tom walks home seul (too young? Ask)
  2. Partenaire pickup Tom, toi mène Eva foot
  3. Delay activation (late arrival acceptable?)

### 🚗 Carpooling options (si Eva football)

| Parent | Location | Drive? | Covoiturer? |
|--------|----------|--------|------------|
| Éva family (toi) | A 12min | Toi ou Lui | Oui |
| Léa family (voisins) | A 8min | Oui | Oui |
| Clara family | A 15min | Oui | Maybe |

**Suggestion**: Léa's mom drives Eva + Léa alternating weeks (you pick up mercredi 18h30). Saves 24min your week.

### 💳 Payment setup

Ticking football registration would auto-trigger payment (trim start 1er mars):
- Amount: €80
- Method: Card on file ✅ or bank transfer
- [Confirm inscription] [Find different activity]
```

#### Risques

| Risque | Mitigation |
|--------|-----------|
| **Payment authority** (child data for activities) | Explicit parent consent; RGPD compliant |
| **Carpooling trust** (sharing family location/contact) | Opt-in, anonymized until parent approves, no data storage outside family |
| **Activity discovery accuracy** (outdated info on web) | Manual verify before enrollment; flag old sources |

#### Score faisabilité & impact

| Métrique | Score | Justification |
|----------|-------|---------------|
| **Faisabilité technique** | **7/10** | Activity discovery + carpooling solver doable |
| **Impact utilisateur** | **8/10** | Reduces logistics burden ~5-8h/month |
| **Priorité MVP** | **#4-5** | Moyen-term, good secondary feature |

---

## IRRITANT #9 : Anticipation saisons/transitions (22 mentions)

### Description détaillée du problème

**Verbatim clé** : *"Changement vêtements saison, école nouvelle, vacances... tout ça, c'est moi."*

Parent doit anticiper:
- Passage vêtements hiver → printemps (quand?)
- Fournitures scolaires (renouvellement avant rentrée)
- Vacances (gîte, transports, packing)
- Transitions école (nouvelle classe, nouveau prof, changement emploi du temps)

**Friction** : Pas prévisible (ce n'est pas "dans le calendrier"), donc facile d'oublier.

---

### Opportunité IA #9.1 : "Seasonal + Transition Anticipation"

#### Solution IA concrète

**Concept** : IA basée sur calendrier scolaire + météo + patterns historiques, suggère transitions à venir :

1. **School calendar parsing** : Quand rentrée? Vacances? Changement classe?
2. **Weather-based triggers** : 15°C avg = temps shorts + tee (trigger "check if kids have...")
3. **Clothing inventory check** : "Eva needs new shoes size 35" (kids grow ~1 size/year, predictable)
4. **Supply list generation** : Parse école supply list, check what you have
5. **Vacation planning assist** : "2 semaines vacances Easter → suggest gîte booking now (6 semaines advance)?"

#### Capacité IA requise

| Capacité | Description | Faisabilité |
|----------|-------------|------------|
| **Calendar parsing** | ICS/school calendar import | 9/10 |
| **Weather reasoning** | Detect seasonal shifts | 8/10 |
| **Clothing size growth** | Predict when kids outgrow sizes | 7/10 |
| **Supply list scraping** | Auto-download école supply lists | 6/10 |
| **Vacation timeline** | Calculate "6 weeks before" for gîte booking | 9/10 |

#### Niveau d'autonomie recommandé

**Niveau 1 (Suggest)** :
- IA notifies of upcoming transitions
- Parent acts (buy, book, prepare)

#### Données nécessaires

| Source | Type |
|--------|------|
| **School calendar** | ICS of vacations + term dates |
| **Kids sizes history** | Track clothes bought (to learn growth) |
| **Weather API** | Local weather forecasts + historical trends |
| **School supply list** | PDF or web link from school |

#### Output attendu

```markdown
## Anticipation Saisons & Transitions — Mars 2026

### 🌤️ Transition Printemps (détectée)

**Quand** : ~ 20-25 février
**Signaux** : Météo moyenne montée 12→18°C, jours allongés

**À faire**
- [ ] Sortir vêtements printemps enfants (short, tee-shirt légers)
- [ ] Vérifier chaussures: Tom (pointure 32 → 33?), Eva (35 → 36?)
- [ ] Ranger vêtements hiver (placard)
- Timing: **Faites ce we si possible**, avant prochain froid (météo instable mars)

---

### 👕 Vêtements : Renouvellement prévu

**Tom (7 ans)**
- Pointure chaussures: 32 (acheté sept 2025)
- Croissance estimée: +0.7 taille/an → Prêt 33 fin février ✅
- **Action**: Acheter chaussures printemps (sport + école) ce mois-ci (avant rupture stock tailles)
- Budget estimé: €45-60

**Eva (8 ans)**
- Pointure: 35 (acheté nov 2025)
- Croissance: +0.8 taille/an → Prêt 36 fin février
- **Action**: Acheter chaussures + 2-3 pantalons coton printemps
- Budget: €80-100

---

### 📚 Rentrée Printemps (Transition classe)

**Date** : 2 mars (lundi)

**Changements** :
- Eva: Passe de CM1 à CM2 (même école)
- Tom: Reste CE1, nouveau prof (Mme Dubois → Mr Martin)

**À anticiper**:
- [ ] Faire liste fournitures **Eva CM2** (Check école website)
- [ ] Confirmer fournitures Tom (peu changent en cours d'année)
- [ ] Nouveau prof Tom: Envoyer mail présentation? (vérifier style de Mr Martin)

**Timeline**: Fournitures achetées D'ICI 1er mars. Fournitures liste CM2 prêtes 1-2 semaine après rentrée.

---

### 🎒 Vacances Pâques — Planification

**Dates**: 6-20 avril (2 semaines)

**Deadline booking**:
- Gîtes populaires: Réserver MAINTENANT (6-8 semaines advance)
- Vols si besoin: Réserver 6-8 semaines avant
- Activités: Book 3-4 semaines avant

**Suggestions**:
1. **Gîte** : Budget €600-900/semaine pour famille 4? Préférences (piscine? plage? montagne? calme?)?
2. **Transport** : Voiture (8h drive?) vs TGV vs vol domestique?
3. **Activities**: Enfants (8 & 7) → Parc de loisirs? Randonnée? Plage?

**Next step**: Décider destination ce week, booking gîte lundi.

---

### 📦 Stocks à vérifier (Monthly checkpoint)

- [ ] Papier toilette (warn: consommation élevée famille, buy 6-pack à l'avance)
- [ ] Produits hygiène enfants (shampoo, savon)
- [ ] Lait + fromage (régulier)
```

#### Risques

| Risque | Mitigation |
|--------|-----------|
| **Over-notification** (too many seasonal reminders) | 1 alert/month max, grouped, not intrusive |
| **Wrong sizing prediction** (growth varies) | User corrects; IA learns from actual purchases |
| **School calendar changes** (last-minute modifications) | Refresh weekly, flag changes to parent |

#### Score faisabilité & impact

| Métrique | Score | Justification |
|----------|-------|---------------|
| **Faisabilité technique** | **7/10** | Calendar + weather APIs standard |
| **Impact utilisateur** | **6/10** | Reduces surprise transition chaos; good quality-of-life improvement |
| **Priorité MVP** | **#5-6** | Lower urgency, but nice-to-have |

---

## IRRITANT #10 : Charge émotionnelle non-reconnue (25 mentions)

### Description détaillée du problème

**Verbatim clé** : *"Je suis aussi gestionnaire des émotions de tout le monde."*

Parent non seulement gère tâches pratiques, mais aussi :
- Écouter les problèmes enfants
- Consoler après mauvaise journée
- Gérer conflits fratrie
- Soutenir enfant anxieux / déprimé
- Montrer intérêt travail scolaire
- Reconnaître efforts enfants
- Gérer atmosphère familiale

**Impact** : C'est du travail invisible non-reconnu. Partenaire ne "voit" pas cette charge.

---

### Opportunité IA #10.1 : "Emotional Check-in + Family Mood Dashboard"

#### Solution IA concrète

**Concept** : IA facilite emotional check-ins et rend visible l'emotional labor :

1. **Daily emotion tracking** : "How is Tom feeling today?" (simple 😊/😐/😔 pour enfants)
2. **Insight extraction** : Si pattern (Eva always sad mercredi) → alert parent + suggest intervention
3. **Parent emotional support** : "Tu as eu une dure journée, prendre 15min pour toi?" (self-care reminder)
4. **Family mood dashboard** : "Cette semaine: 70% positive, 20% neutral, 10% difficult. Patterns: Tom struggles mercredi."
5. **Couple conversation prompts** : "Tu as géré beaucoup d'émotions cette semaine. Partenaire au courant?"

#### Capacité IA requise

| Capacité | Description | Faisabilité |
|----------|-------------|------------|
| **Sentiment parsing** | Extract emotion from child/parent input | 8/10 |
| **Pattern detection** | "Mercredi = hard day pattern?" | 7/10 |
| **Intervention suggestion** | "Tom seems anxious Wednesday → check if foot pressure" | 6/10 |
| **Self-care prompt** | Recommend rest, breaks, social time for parent | 7/10 |
| **Visualization** | Dashboard mood trends (not medical, just awareness) | 8/10 |

#### Niveau d'autonomie recommandé

**Niveau 1 (Suggest/Inform)** :
- IA collects emotion data (from user input, not surveillance)
- IA shows patterns + suggests conversations
- Non-prescriptive

#### Données nécessaires

| Source | Type |
|--------|------|
| **Daily mood check-ins** | Parent + kids report mood briefly (1 minute daily) |
| **Parent workload log** | "How much emotional labor did you do today?" (optional) |
| **Child event context** | Link mood to events (bad math test? friend conflict?) |

#### Output attendu

```markdown
## Emotional Wellbeing — Famille Report (16-22 février 2026)

### 📊 Family Mood Summary

**This week's emotional state**:
- 🟢 Positive (calm, happy): 65% (Mon, Thu, Fri)
- 🟡 Neutral (stable, ok): 20% (Tue morning, Wed before foot)
- 🔴 Difficult (stressed, sad, anxious): 15% (Tue pm, Wed afternoon)

**Trend**: Normal, stable week. No red flags.

---

### 👧 Tom (7 ans) — Emotional patterns

**Mood this week**: Generally 😊, 1 difficult moment

| Day | Mood | Context | Notes |
|-----|------|---------|-------|
| Mon | 😊 | Recess fun | |
| Tue | 😊 morning | Normal start | |
| Tue | 😔 evening | Math test not great | You: "Sat with him, reviewed. Better confidence after." |
| Wed | 😊 | Football day (excitement) | |
| Thu | 😊 | Playdate after school | |
| Fri | 😊 | Weekend anticipation | |

**Pattern**: Tom shows slight anxiety around academic challenges, needs reassurance. Physical activity (foot) very positive for mood. Overall, very stable boy.

---

### 👱 Eva (8 ans) — Emotional patterns

**Mood this week**: Mixed, some anxiety signals

| Day | Mood | Context | Notes |
|-----|------|---------|-------|
| Mon | 😊 | Friend time at lunch | |
| Tue | 😊 | Normal | |
| Wed | 😐 | "Tired" + "Worried about math quiz Friday" | You: consoled, studied together evening |
| Thu | 😊 | Quiz over, relief | |
| Fri | 😊 | Weekend happy | |

**Pattern**: Eva shows performance anxiety before exams/quizzes. Responds well to prep + reassurance. No ongoing concerns.

---

### 💔 Parental Emotional Labor (TOI) — This week

**Emotional tasks completed**:
- Listening: 4 hours (Tom math worry, Eva friendship drama, both bedtime chats)
- Consoling: 2 hours (Tom test anxiety, Eva friend excluded incident)
- Conflict resolution: 1 hour (Siblings fought about toy, you mediated)
- Encouragement/celebration: 0.5 hours (Math test results, foot game)
- **Total emotional labor: ~7.5 hours**

**Comparison**: Partenaire emotional labor ~1 hour (game time + one bedtime story).

**Observation**: You are primary emotional manager. Partenaire can increase: He's good with physical play (foot, games) — suggest he do more evening quality time with kids (builds his emotional connection + reduces your load).

---

### 🔔 Insights & Suggestions

**What's working well**:
- ✅ You're attuned to both kids' emotional needs
- ✅ Kids feel safe expressing emotions
- ✅ You're responsive to anxiety/sadness

**Area to explore**:
- ⚠️ Your own emotional load is HIGH (7.5h + managing couple emotions)
- 💡 Suggestion: Partenaire steps up emotional support. Try: "Lui takes Monday/Wed bedtime routines (emotional check-in), you do other nights"
- 💡 Self-care: You haven't had solo time this week. Schedule 1h solo time next week (walk, coffee, read)

---

### 📝 Conversation starter for couple

*"I've been tracking emotional labor this week. I did 7.5h; you did 1h. Not accusation — I want us both engaging emotionally with kids AND I need breaks. Can you own Monday + Wednesday bedtime (emotions + tasks)?"*
```

#### Risques

| Risque | Mitigation |
|--------|-----------|
| **Privacy** (emotional data is sensitive) | No storage of detailed content, only patterns/mood. Encryption. No sharing without explicit consent. |
| **Medical misunderstanding** (IA suggests therapy but not qualified) | Frame as "awareness tool", not medical. Flag if serious patterns (depression, etc.) → recommend human therapist, not IA. |
| **Surveillance feel** (daily mood tracking might feel invasive) | Opt-in, parent controls frequency (daily vs weekly) |

#### Score faisabilité & impact

| Métrique | Score | Justification |
|----------|-------|---------------|
| **Faisabilité technique** | **7/10** | Sentiment analysis + dashboarding standard |
| **Impact utilisateur** | **7/10** | Raises awareness, facilitates couple conversation, reduces isolation feeling |
| **Priorité MVP** | **#6-7** | Nice-to-have, builds retention/emotional connection to product |

---

## IRRITANT #11-20 : Résumé des irritants restants

Pour raison de brièveté, voici un résumé des 10 irritants restants :

| Irritant | Mention count | Opportunité IA Proposée | Autonomie | Score Impact | Priorité |
|----------|--------------|------------------------|-----------|-------------|----------|
| **#11: Culpabilité persistante** | 33 | Positive affirmation + pattern recognition ("Tu fais bien") | Level 1 | 6/10 | #8-9 |
| **#12: Decision fatigue** | 27 | Decision support (suggest repas, activités, achats) | Level 1-2 | 7/10 | #7-8 |
| **#13: Admin scolaire** | 20 | Document management hub (permissions, cahier parent, emails école) | Level 2 | 6/10 | #8-9 |
| **#14: Logistique quotidienne** | 19 | Smart packing lists + departure checklist (auto-generated) | Level 1 | 5/10 | #9-10 |
| **#15: Notification fatigue** | 18 | Smart notification throttling (1 daily digest vs 47 alerts) | Level 1 | 7/10 | #3-4 (quick win) |
| **#16: Admin santé (vaccins, etc.)** | 17 | Medical records hub + vaccine tracking | Level 2-3 | 8/10 | #2-3 |
| **#17: Stress couple** | 24 | Couple communication prompts + shared perspective tool | Level 1 | 8/10 | #5-6 |
| **#18: Unforeseen logistics** | 15 | Flexible to-do system with IA priority-reordering | Level 1-2 | 5/10 | #9-10 |
| **#19: Lack of recognition** | 26 | Impact visualization + impact statement for partenaire | Level 1 | 6/10 | #7-8 |
| **#20: Time management** | 14 | Time blocking assistant (calendar optimization) | Level 1-2 | 5/10 | #10 |

---

## SECTION 2 : CONTRAT D'AUTONOMIE IA

### Définition : Niveaux d'autonomie

| Niveau | Autonomie | Décisions IA | Contrôle Parent | Exemples |
|--------|-----------|-------------|-----------------|----------|
| **0** | Aucune | IA ne propose rien | Parent fait tout | Status quo (pas d'IA) |
| **1** | Suggest | IA propose, parent décide + exécute | Parent valide tout | "Suggestion repas" → parent décide |
| **2** | Draft | IA prépare, parent valide | Parent vérifie avant action | IA crée liste courses → parent modifie → go |
| **3** | Execute | IA agit, parent supervise | Parent peut override après | IA prend RDV Doctolib → parent confirme apres |
| **4** | Autonome | IA gère complètement | Parent notifié seulement | Renouvellement ordonnance aut = IA fait, parent reçoit notif |

### Principes fondamentaux

1. **Consentement explicite par niveau** : Parent doit opter-in à chaque niveau (pas d'escalade silencieuse)
2. **RGPD-first** : Données enfants cryptées end-to-end; IA ne stocke rien sans consent
3. **Transparency** : Parent voit TOUJOURS ce que l'IA a fait / propose
4. **Rollback facile** : À tout moment, parent peut revenir à niveau inférieur ou step-by-step verify
5. **Graduated trust** : MVP = Level 1-2 uniquement. Levels 3-4 après 4+ semaines usage + user feedback

### Matrice décisions : Qui fait quoi?

#### Décisions 100% Humaines (Toujours Niveau 0-1)

| Décision | Pourquoi | Exemple |
|----------|---------|---------|
| **Éducation** (choix école, méthode discipline) | Valeurs parentales | "Maman je veux pas à cette école" → parent décide |
| **Santé grave** (chirurgie, médication majeure) | Médical/éthique | IA peut informer, parent + médecin décident |
| **Argent** (budget majeur, achats importants) | Financial autonomy | IA peut suggérer, parent approuve |
| **Sécurité enfants** (permissions sorties, contacts) | Safety-critical | IA peut alerter, parent décide |
| **Couple** (gestion conflits couple) | Relationship-critical | IA peut suggérer conversation, couple discute |

#### Décisions Collaborative Level 1-2 (Suggest/Draft)

| Décision | Autonomie | Format |
|----------|-----------|--------|
| **Repas** | Level 1 (Suggest) | IA propose 5 menus, parent choisit |
| **Courses** | Level 2 (Draft) | IA liste, parent modifie |
| **RDV médicaux** | Level 2 (Draft) | IA trouve dispo, parent confirme |
| **Activités enfants** | Level 2 (Draft) | IA suggère, parent inscrit |
| **Tâches** | Level 1-2 | IA propose, parent valide ou delegate |

#### Décisions potentiellement Level 3 (Execute — après 4+ semaines & consent)

| Décision | Conditions | Rollback |
|----------|-----------|----------|
| **RDV Doctolib auto-booking** | Doctolib API + parent opt-in | Parent peut cancel 24h avant |
| **Repas auto-decision** | Si patterns établis + parent confirme | Parent peut veto day-before |
| **Payment activités** | Parent stored payment method + explicit amount limits | Monthly limit cap, receipt email |
| **Notification auto-send** (partenaire) | Parent authorizes, templates pre-approved | Parent can edit before send |

#### Décisions NOT for Level 4 (Autonome) — Hors MVP & v1

| Décision | Raison | Timeline |
|----------|--------|----------|
| **Auto-prescription renewal** | Too medically critical, AI can hallucinate | v2+ après regulatory clarity |
| **Child data storage** | RGPD risk, needs regulatory framework | v2+ après EU AI Act enforcement |
| **Financial transactions** | Payment friction, fraud risk | v2+ après trust building |
| **School communication** (sending emails école) | Potential miscommunication, needs parent review | v2+ after user feedback |

### Framework : Progression vers autonomie

**Goal** : Parent gains trust over 4-8 weeks through graduated autonomy.

**Week 1-2 (Level 0-1 only)**
- IA suggests only
- Parent validates everything manually
- Goal: Parent sees IA is accurate

**Week 3-4 (Level 1-2)**
- IA drafts (e.g., list courses ready to modify)
- Parent modifies, then acts
- Goal: Parent trusts IA's groundwork

**Week 5-8 (Level 2-3, opt-in)**
- Parent can authorize specific actions (e.g., "auto-book Doctolib")
- IA executes, parent supervises
- Goal: Parent confident IA makes right decisions

**Month 3+ (Level 3-4, opt-in)**
- Parent can allow full autonomy on specific tasks
- IA operates; parent receives post-action notifications
- Goal: Parent has significant time back

### Mécanismes de confiance & correction

#### 1. Transparency Log
Chaque action IA est loggée dans "IA Activity" panel :
```
📋 IA Actions (Last 7 days)
- Suggested 5 meals for week ✅ (user accepted 4/5)
- Found 3 Doctolib appointments ✅ (user booked 1)
- Sent task reminder to partner ✅ (partner confirmed)
- Modified shopping list ✅ (user changed 2 items)
```

#### 2. Confidence Scoring
Chaque suggestion/action a un score de confiance :
```
Meal suggestion: Pasta bolognaise
Confidence: 87% (based on: family likes pasta 80%, budget ok 95%, time available 90%)
If confidence < 60%, IA flags as "uncertain, please review"
```

#### 3. Feedback Loop
Parent can rate "Was this suggestion useful?"
```
IA learns: "Mom always says 'no' to fish" → stop suggesting fish
IA learns: "Family loves Italian → increase Italian suggestions"
```

#### 4. Rollback & Veto
Parent can easily undo or veto:
```
IA booked RDV Doctolib
[Undo (within 24h)] [Keep] [Next time, ask first]
```

#### 5. Weekly Audit
Every Sunday: "Here's what I did this week. Accurate?"
```
Tasks completed: 23
Tasks IA suggested you avoid: 2
Decisions you overrode: 4
Overall accuracy: 91%
[Looks good] [Adjust settings]
```

### Escalation & Communication Rules

#### When IA Should Ask Parent Permission First

- Any action affecting partenaire behavior (send notification to him)
- Payment transactions > €20
- Scheduling medical appointments (different from just finding dispo)
- Modifying school-related documents/communication
- Any decision touching child privacy

#### When IA Can Act Autonomously (if authorized)

- Suggestion/notification to parent only
- Drafting lists or plans (non-binding)
- Calculations (budget, time, etc.)
- Pattern detection (alerting to trends)

#### When Parent Must Act (Never AI)

- Approving major healthcare decisions
- Resolving couple conflicts
- Setting family values/rules
- Handling sensitive child emotional issues
- Final say on any child-related decision

---

## SECTION 3 : STACK IA NECESSAIRE

### Capacités NLP requises

| Capacité | Use Case | Model Required | Faisabilité |
|----------|----------|-----------------|------------|
| **Event extraction** | Parse emails/SMS for RDV, permissions | NER + regex patterns | 9/10 (easy) |
| **Intent classification** | "User asks for X → parse intent" | Standard classifiers | 9/10 (easy) |
| **Text generation** | Meal suggestions, notifications | LLM (Claude, GPT-4) | 9/10 (mature) |
| **Multi-source reasoning** | Combine calendar + email + SMS + inventory | Retrieval-augmented LLM | 8/10 (good) |
| **Planning/sequencing** | "Do X before Y" logic | LLM with chain-of-thought | 8/10 (good) |
| **Personalization** | Learn family preferences over time | Fine-tuning or prompt engineering | 7/10 (medium) |
| **Sentiment analysis** | Detect family mood from input | Pre-trained sentiment models | 8/10 (good) |
| **Medical domain reasoning** | RDV frequency, vaccine schedules | Domain LLM or rules-based | 7/10 (good) |
| **Constraint solving** | Calendar conflicts, carpooling optimization | Solver + heuristics | 6/10 (harder) |
| **Error detection** | "Did I infer RDV wrong?" → flag uncertainty | Confidence scoring | 7/10 (medium) |

### APIs & Intégrations existantes

| API/Service | Purpose | Integration Complexity | Availability |
|-------------|---------|----------------------|--------------|
| **Google Calendar API** | Read/write family calendar | Medium (auth, rate limits) | ✅ Available |
| **Gmail API** | Parse RDV emails, school messages | Medium (permissions, privacy) | ✅ Available |
| **Doctolib API** | Book RDV medical, read availability | Medium (provider dependent) | ✅ Available (FR-specific) |
| **SMS parsing** | Parse appointment reminders, school SMS | Hard (requires phone integration) | ⚠️ Complex (device-dependent) |
| **School calendar ICS** | Read école holidays, term dates | Easy (if school provides) | ⚠️ Variable (school dependent) |
| **Marmiton / Yummly API** | Recipe suggestions, nutrition data | Medium (if API exists; may need web-scrape) | ⚠️ Limited (scraping fallback) |
| **Google Shopping** | Price comparison for groceries | Medium (API access variable) | ⚠️ Limited |
| **Stripe/PayPal** | Payment automation for activities | Medium (PCI compliance) | ✅ Available |
| **SMS provider** (Twilio/Vonage) | Send notifications to partenaire | Easy | ✅ Available |
| **Weather API** | Seasonal transition detection | Easy | ✅ Available (OpenWeather, etc.) |
| **Google Maps** | Carpooling distance, drive times | Easy | ✅ Available |

### Modèles IA recommandés

#### Primary Model (LLM)

**Recommendation** : Claude 3.5 Sonnet (Anthropic)
- Reasoning capability for multi-step planning
- Good at family/cultural context (less biased than GPT-4 for parenting advice)
- Cost reasonable for frequent inference
- EU/GDPR-friendly (no data storage for inference)

Alternative: GPT-4o (OpenAI) — slightly better for visual data (invoice parsing, etc.)

#### Secondary Models (Specialized)

| Task | Model | Rationale |
|------|-------|-----------|
| **Sentiment analysis** | Pre-trained Huggingface (distilBERT) | Fast, lightweight for daily mood |
| **Named entity recognition** | spaCy (FR model) | Extract dates, names, locations from emails |
| **Text classification** | FastText or Huggingface small model | Intent classification (meal? RDV? permission?) |
| **Recommendation** | Collaborative filtering (learned from user behavior) | Personalized meal/activity suggestions |

#### Vision Model (Optional, v1+)

For photo-based inventory (fridge, closet):
- Claude 3.5 Vision or GPT-4o Vision
- Lightweight option: Deployed fine-tuned vision model on-device

### Architecture High-Level

```
┌─────────────────────────────────────────────────┐
│                  User Interface                   │
│  (Mobile app, web, Slack integration)            │
└──────────────────┬──────────────────────────────┘
                   │
       ┌───────────┴────────────┬──────────────┐
       │                        │              │
   ┌───▼────┐          ┌────────▼──┐    ┌─────▼──┐
   │ Claude │          │ Specialized│    │Browser │
   │ Sonnet │          │   Models   │    │Parser  │
   │ (LLM)  │          │ (sentiment)│    │(email) │
   └───┬────┘          └────┬───────┘    └──┬─────┘
       │                    │                 │
       └────────┬───────────┴─────────────────┘
                │
        ┌───────▼────────┐
        │   Data Layer   │
        │ (cache, logs)  │
        └───┬────────────┘
            │
    ┌───────┴────────────────┬────────────────┐
    │                        │                │
 ┌──▼──┐  ┌────────┐  ┌────────┐  ┌──────────▼─┐
 │GDPR │  │Google  │  │Doctolib│  │ Partenaire │
 │File │  │Calendar│  │ API    │  │ Notifications
 │Store│  │+ Gmail │  │        │  │ (SMS/Slack)
 └─────┘  └────────┘  └────────┘  └────────────┘
```

#### Key decisions:

1. **Data storage** : RGPD-compliant, encrypted at rest. No data sent to LLM cloud (use Claude API with no logging).
2. **Real-time parsing** : Email/SMS parsed on device or secure server; never stored in cleartext.
3. **Offline capability** : Core suggestion engine can run locally (via local LLM deployment like Ollama + Sonnet if needed).
4. **Extensibility** : Plugin architecture for new APIs (new school system? new activity provider? → add integration).

### Données d'entrainement requises vs disponibles

| Data Type | Required? | Source | Available? | Privacy Risk |
|-----------|-----------|--------|-----------|--------------|
| **Family calendars** (Google) | Yes (core feature) | User grants permission | ✅ Yes | Low (user-owned data) |
| **Email** (RDV parsing) | Yes (critical) | Gmail API | ✅ Yes | Medium (sensitive content) |
| **Child profiles** (ages, schools) | Yes | Manual entry | ✅ Yes | Low (user-entered) |
| **Medical history** | Ideal (for health anticipation) | Manual entry + Doctolib | ⚠️ Partial | High (medical data) |
| **Family preferences** | Ideal (for personalization) | User feedback + history | ✅ Gradually | Low |
| **Parenting advice corpus** | Nice-to-have | Academic + parenting books | ✅ Yes | N/A (already published) |
| **Regional activity DB** | Ideal (for activity discovery) | Web scraping + APIs | ⚠️ Partial | Low (public data) |

**Training approach** :
- **No fine-tuning on user data** (privacy + compliance). Use zero-shot/few-shot instead.
- **Learned personalization** via prompt engineering: Store user preferences in system prompt (e.g., "This family is vegetarian, budget-conscious").
- **Contextual few-shot** : Include 1-2 examples of past suggestions user liked, to guide new suggestions.

---

## SECTION 4 : PRIORITISATION MVP

### Matrice Effort × Impact

```
┌─────────────────────────────────────────────────────┐
│ EFFORT (months)                                     │
│ High │                                              │
│      │  #4-Partenaire #9-Emotional #6-Seasonal    │
│      │  Coach        Wellness    Transitions       │
│ Med  │  #8-Activities #7-Tasks             #5-Equity
│      │  #2-Task Visibility                 Dashboard
│      │                                              │
│ Low  │  #3-Meal      #15-Notif   #1-Anticipation  │
│      │  Planning     Filtering   View              │
│      │  #10-Logistics            #6-Medical       │
│      └─────────────────────────────────────────────┤
│        Low        Medium         High (Impact) →   │
└─────────────────────────────────────────────────────┘
```

### Top 5 Opportunités MVP v0 (Quick Wins)

**Critères** : Impact élevé + effort faible + faisabilité 7-8/10+

| Rang | Feature | Impact | Effort | Timeline | Key Deliverable |
|------|---------|--------|--------|----------|-----------------|
| **#1** | **Anticipation View** | 9/10 | Medium (4-6w) | v0.1 (Feb-Mar) | 2-week ahead dashboard (cal + RDV + repas + courses) |
| **#2** | **Meal Planning + Grocery** | 8/10 | Medium (4-5w) | v0.2 (Mar) | Menu suggestions (parent validates) + auto grocery list |
| **#3** | **Notification Filtering** | 7/10 | Low (1-2w) | v0.1 | 1 daily digest vs 47 alerts (quick win, high satisfaction) |
| **#4** | **Medical RDV Hub** | 9/10 | Medium (5-6w) | v0.3 (Mar-Apr) | RDV tracking + Doctolib integration (Level 2: find + parent books) |
| **#5** | **Task Visibility** | 8/10 | Medium (4-5w) | v0.2 (Mar) | Implicit task detection + partenaire notifications (Level 1-2) |

**Non dans MVP** (trop risque, trop complexe, RGPD unclear) :
- ❌ Emotional wellness dashboard (v1+, needs validation)
- ❌ Carpooling optimizer (too many moving parts, v1+)
- ❌ Auto-payment activities (payment friction, compliance, v1+)
- ❌ Equity dashboard (requires extensive behavioral data, v1+)

### Top 5 Opportunités v1 (High-impact, Medium-effort)

**Timeline** : Apr-May 2026

| Rang | Feature | Impact | Effort | Rationale |
|------|---------|--------|--------|-----------|
| **#6** | **Equity Dashboard** (couple visibility) | 8/10 | Medium-High | Builds on user behavior data from MVP; solves couple friction |
| **#7** | **Partenaire Coach** (pro-active suggestions) | 7/10 | Medium | Requires learned patterns from #5 (Task Visibility); increases engagement |
| **#8** | **Activity Management** (discovery + booking) | 8/10 | Medium-High | Regional activity DB + Stripe integration; good secondary feature |
| **#9** | **Seasonal Transitions** (clothing, school prep) | 6/10 | Low-Medium | Build on Anticipation View; nice QoL improvement |
| **#10** | **Decision Support** (budget, snacks, etc.) | 5/10 | Low | Lightweight feature; reduces decision fatigue |

### Feature Roadmap Timeline

```
FEB 2026         MAR 2026          APR 2026            MAY 2026
├─v0.1────────────v0.2──────────────v0.3──────────────v0.4
│ • Anticipation  • Meal planning   • Medical hub      • Refinements
│ • Notif filter  • Task visibility • Partenaire coach • Seasonal prep
│ • Auth + onboard• Partenaire noti │ • Equity board  │
│                 │                 │                 │
└─────────────────────────────────────────────────────
                    └─ v1.0 soft launch (Apr 15)
                       (France pilot, 100 families)
```

---

## SECTION 5 : SCÉNARIOS USAGE DÉTAILLÉS

### Scénario #1 : Anticipation View (Killer Feature)

**Contexte** : Jeudi soir, Sophie (mère, 38 ans, 2 enfants) ouvre app avant coucher. Elle est mentalement chargée.

**Trigger** : Push notification : "Semaine 24-29 fév : 3 RDV + 4 activités. Voir anticipation?"

**Interaction**

```
1. Sophie click notif → Anticipation View appears

📋 Your Week Ahead (Feb 24-29)
┌─────────────────────────────────────────┐
│ 🔴 WEEK LOAD: BUSY (3-4 RDV + activities)
│
│ MO 24 FEB: Pediatrician 10h (Eva)
│ WE 26 FEB: Football 18h (Tom)
│ FR 28 FEB: Ophthalmologist 15h (Eva)
│
│ 📚 School + Activities 
│ LUN-VEN: Normal school
│ WE: Football Tom
│ SA 1st MARCH: Birthday gift (Eva's friend)
│
│ 🍳 Meals to plan
│ Monday-Friday: [5 meals needed]
│ [Menu suggestions] [Or customize]
│
│ 📦 Groceries missing
│ [View smart list] [Edit]
└─────────────────────────────────────────┘

2. Sophie clicks "Menu suggestions"
   ↓ IA offers:
   - Monday: Pasta bolognaise (rapide, 20min)
   - Tuesday: Fish + vegetables (budget ok)
   - Wednesday: Quick pizzas (foot evening)
   - Thursday: Leftover pasta + salad
   - Friday: Homemade pizza (weekend wind-down)

3. Sophie:
   - Approves 4/5 (changes Tuesday to risotto — Tom's favorite)
   - Clicks [Confirm Menus]
   - Grocery list auto-updates

4. Result:
   ✅ Sophie saved 30 minutes planning
   ✅ Menus clear through Friday
   ✅ Grocery list ready for shopping Saturday
   ✅ RDV in calendar + reminders set
   
5. Next morning:
   - Push 8am: "3 RDV this week, here's what to prepare"
   - Notification: "Carnet vaccins pour lundi pédiatre"
   - Notification: "Mardi = risotto riz. Check you have rice?"

📊 RESULT
- Mental load: -40% (was thinking about repas + RDV + permissions = now consolidated view)
- Time saved: 30 min planning, 20 min prep-checking
- Confidence: +90% (Sophie knows full week ahead, can plan around it)
```

**Mesure de succès**

- ✅ Sophie uses Anticipation View ≥ 3x/week
- ✅ RDV (pediatrician) reminder was effective (she didn't forget)
- ✅ Menus suggestions adoption ≥ 60% (4-5 out of her suggestions approved)
- ✅ Mental load decrease self-reported ≥ 30% (survey)
- ✅ Couple conversation: "I feel less overwhelmed managing the week"

---

### Scénario #2 : Task Visibility + Partenaire Notifications

**Contexte** : Wednesday evening. Tom has football at 18h. Sophie wants partenaire to prepare Tom's kit (not have to ask).

**Trigger** : App detects "Football WE 26 18h" in calendar.

**Interaction**

```
1. IA reasoning:
   - Event: "Football WE 26 18h"
   - Implicit tasks: 
     * Wash football jersey (due TUE or WE morning)
     * Prepare boots, socks, water bottle
     * Remind Tom evening before

2. IA generates task list for Sophie:
   
   📋 Implicit Tasks for this week
   ├─ VISIBILITY (for you to validate):
   │  ├─ [ ] Wash Tom's football jersey (TUE)
   │  ├─ [ ] Check Tom has clean socks
   │  └─ [ ] Prepare water bottle
   │
   └─ TO SEND TO [Partenaire]:
      "Tom has football WED 18h. Can you handle:"
      ├─ Prepare his kit TUE evening (jersey washed, boots ready)?
      └─ Remind him WED morning?"

3. Sophie reviews. Task list looks accurate.
   Click [Send to Partenaire]

4. Partenaire receives SMS:
   
   "Hey\! Tom's football WED 18h. 
    Can you wash his jersey tonight + prepare kit? Takes 15min.
    (App suggestion, not order 😊)"
   
   [Accept] [Ask to reschedule] [Already done]

5. Partenaire responds: [Accept]
   ✅ Task confirmed. App sends reminders to partenaire:
   - TUE 19h: "Tom's football kit ready? (jersey, boots, socks)"
   - WED 7am: "Remind Tom about football today 18h"

6. Result:
   ✅ Sophie didn't have to ask (invisible task made visible)
   ✅ Partenaire received clear, kind request (not nagging)
   ✅ Task completion tracked
   ✅ Couple friction reduced (proactive, not reactive)

📊 RESULT
- # tasks Sophie had to ask about: 0 (was 5-7 before)
- Partenaire engagement: +70% (he felt trusted, not managed)
- Couple satisfaction: "He took initiative\!" (rare, powerful moment)
```

**Mesure de succès**

- ✅ Partenaire acceptance rate of tasks ≥ 70%
- ✅ Task completion rate ≥ 80% (partenaire did what he accepted)
- ✅ Sophie instances of "had to ask again" decrease ≥ 50%
- ✅ Couple perception of equity improves (quarterly survey)

---

### Scénario #3 : Meal Planning + Smart Grocery

**Contexte** : Saturday morning. Sophie typically spends 2 hours planning menus + shopping. She wants to reclaim time.

**Trigger** : Saturday 9am, Sophie opens app or receives push: "Planning menus for week 2-8 March?"

**Interaction**

```
1. Sophie clicks [Plan Week]

2. IA asks quick questions (40 sec total):
   - Budget: €120/week? [Yes] [No: €100] [€150]
   - Dietary: Any restrictions? [Vegetarian TUE-THU] [Nut-free (Tom)] [None]
   - Time: Busy days? [Yes: TUE (work late), WED (foot)]
   - Preferences: What does fam love? [Italian] [Asian] [Mediterranean]

3. IA generates proposal:
   
   📋 Menus + Grocery (Week 2-8 March)
   
   MONDAY: Pasta carbonara (20min, classic)
   TUESDAY: Slow-cooker couscous (prep 10min morning, cook 6h)
   WEDNESDAY: Pizzas (rapide\! 30min start-to-table)
   THURSDAY: Quiche veggie (veggie day) + salad
   FRIDAY: Risotto mushrooms (30min, cozy)
   SATURDAY: Leftover bowls (repurpose WE)
   SUNDAY: Roast chicken (slow-roasted, family time)
   
   Budget: €118 ✅ (within target)
   Time busy days: ✅ (TUE slow-cooker, WED quick)
   
   ---
   
   🛒 SMART GROCERY LIST
   
   Organized by store layout (Casino):
   
   PRODUCE (€22)
   - Onions x2
   - Mushrooms 400g (risotto)
   - Salad mix
   - Tomatoes
   - Spinach (quiche)
   - Carrots
   
   MEAT/DAIRY (€45)
   - Chicken whole 1.5kg (roast)
   - Pasta (fresh) 500g
   - Eggs x12
   - Cream 200g (carbonara + quiche)
   - Cheese (grating) 250g
   
   PANTRY (€30)
   - Couscous 500g
   - Risotto rice 500g
   - Flour (pizza) 1kg
   - Broth (mushroom)
   - Olive oil
   
   FROZEN/SAVED (€21)
   - Peas (veggie x2 meals)
   - Shrimp option (if splurge Friday)
   
   NOTES:
   - Check you have: butter, salt, spices
   - Buy on TUESDAY (WED pizzas will need flour fresh)
   - Casino closest = 8 min drive

4. Sophie reviews list. Looks good.
   [Confirm] [Edit]
   
   She changes: Add chickpeas (Thursday couscous, not quiche)

5. List updates. Sophie clicks [Print] (or mobile list) → off to store

6. At store:
   - Follows list layout → efficient shopping
   - Finishes in 45 min (vs usual 2h wasted on decisions)
   - Doesn't impulse-buy (list-guided)

7. Home. Week is planned + groceries ready.
   - Monday: 15min pasta
   - Tuesday: Slow-cooker (minimal effort)
   - Wednesday: Kid-friendly pizza activity
   - No "what's for dinner?" stress all week

📊 RESULT
- Time saved: 75 min (planning + shopping)
- Decision fatigue: Eliminated
- Food waste: Reduced (planned meals use all produce)
- Kids: "Can we make pizza?" (engagement, fun)
- Partenaire: Can help cook (recipe clear, ingredients ready)

BONUS: If partenaire helps cook 2 nights (TUE + THU), couple time + reduced load.
```

**Mesure de succès**

- ✅ Time to plan + shop: <1 hour (vs 2h baseline)
- ✅ Meal suggestion acceptance: ≥ 70%
- ✅ Food waste reduction: ≥ 30%
- ✅ Repeat usage: ≥ 80% of weeks
- ✅ Partenaire participation in cooking: +50% (clear recipes lower friction)

---

### Scénario #4 : Medical RDV Coordination Hub

**Contexte** : Monday. Eva needs pediatrician checkup (overdue 8 months). Sophie dreads calling, waiting on hold.

**Trigger** : IA notification: "Eva's pédiatre checkup is 8 months overdue. Shall I find appointments?"

**Interaction**

```
1. Sophie clicks [Yes, find appointments]

2. IA searches:
   - Doctolib API (80% doctors)
   - Phonebook for non-Doctolib doctors
   - Sophie's preferred doctor (if exists) or closest

3. IA returns results (within 30 sec):
   
   📋 Available Appointments — Dr. Benoit Fournier (Regular doctor)
   
   FEB 27 (WED): 14h30 ✅ (midweek, fits schedule)
   FEB 27 (WED): 16h00 ✅
   MAR 3 (TUE): 10h00 ✅
   MAR 10 (TUE): 09h30 ✅
   
   🏥 Alternative: Dr. Sylvie Lefevre (clinic 3km away)
   - MAR 1 (SAT): 09h00 (weekend, farther)
   
4. Sophie sees options. Prefers Benoit, WED 14h30 fits (not conflict with TOM's foot 18h).
   Clicks [Book FEB 27, 14h30 with Dr. Benoit]

5. IA books via Doctolib API automatically ✅
   OR if manual booking needed: IA calls Sophie with link (soft approach)

6. Confirmation:
   
   ✅ RDV CONFIRMED
   Dr. Benoit Fournier, Pediatrician
   Wednesday, February 27 @ 14:30
   
   📋 Preparation checklist:
   - [ ] Bring vaccination record (carnet vaccins) — you have paper copy ✅
   - [ ] List any concerns (growth, allergies, behavior)
   - [ ] Insurance card
   
   ⏰ Reminders set:
   - TUE 19h: "Eva pédiatre tomorrow 14h30"
   - WED 07h: "Today: pédiatre 14h30, carnet vaccins packed?"
   - WED 14h: "Leaving for appointment in 30min"

7. After RDV:
   Sophie returns. IA prompt:
   "How did it go? Any results/notes to save?"
   
   Sophie types (or voice): "Eva all healthy, grows well, mild eczema noted."
   ✅ Saved to Eva's medical record
   ✅ Next checkup: Feb 2027 (auto-reminder in 11 months)

📊 RESULT
- Time Sophie saved: 45 min (no calling, no hold)
- Stress: Gone (IA did the work)
- Appointment secured: Guaranteed (automation)
- Record-keeping: Automatic (no losing paper notes)
- Next RDV: Proactively tracked (won't forget again)

BONUS SCENARIO (later):
- Tom's dentist (OVERDUE): IA notifies "Tom's dental checkup 13 months overdue, URGENT"
- Sophie: "Find appointment ASAP"
- IA: "Clinic Smile&Co has SAT morning 10h. Book?"
- Sophie: [Confirm]
- Tom's dental: Booked in 2 min, no stress.
```

**Mesure de succès**

- ✅ Time to book RDV: <5 min (vs 30+ min baseline with calls)
- ✅ RDV booking success rate: ≥ 95%
- ✅ Missed RDV rate: 0 (was ~10% before)
- ✅ Stress self-reported: -70% (medical admin no longer dreaded)
- ✅ Medical record accuracy: ≥ 90% (results saved)

---

### Scénario #5 : Equity Dashboard — Couple Conversation

**Contexte** : March 15 (after 3 weeks MVP usage). Quarterly couple review. Sophie is still frustrated ("Je fais toujours plus").

**Trigger** : Sunday evening. App notification: "Monthly equity review ready. [View]"

**Interaction**

```
1. Sophie clicks [View Equity Review] → detailed report appears:

📊 YOUR HOUSEHOLD: FEBRUARY 2026 EQUITY REVIEW
   (Tallied from calendar, task logs, app usage)

┌────────────────────────────────────────────────┐
│ EFFORT DISTRIBUTION                            │
│                                                │
│ You: ████████████████░ 72% (190 hours)       │
│ Him: ████░            28% (75 hours)         │
│                                                │
│ ⚠️ Gap: 97 hours unfair burden (YOUR excess) │
└────────────────────────────────────────────────┘

BREAKDOWN:
┌─────────────────┬──────┬──────┬──────────┐
│ Task Category   │ You  │ Him  │ Ideal    │
├─────────────────┼──────┼──────┼──────────┤
│ VISIBLE TASKS   │ 60h  │ 15h  │ 37.5h ea │
│ (Cooking,clean) │ 80%  │ 20%  │          │
├─────────────────┼──────┼──────┼──────────┤
│ INVISIBLE TASKS │ 80h  │ 5h   │ 42.5h ea │
│ (Planning,coord)│ 94%  │ 6%   │          │
├─────────────────┼──────┼──────┼──────────┤
│ KIDS DIRECT     │ 40h  │ 35h  │ 37.5h ea │
│ (Bath,homework) │ 53%  │ 47%  │          │
├─────────────────┼──────┼──────┼──────────┤
│ COUPLE/HOUSE    │ 10h  │ 20h  │ 15h ea   │
│ (Finances,maint)│ 33%  │ 67%  │          │
└─────────────────┴──────┴──────┴──────────┘

KEY INSIGHT:
⚠️ THE REAL PROBLEM: INVISIBLE WORK
   - Cooking/cleaning: You do 3x more (visible, gets acknowledged)
   - Planning/coordination: You do 15x more (invisible, NOT acknowledged)
   
   His perception: "We share kids 50-50" ✓ ACCURATE
   His perception: "We share household 50-50" ❌ INACCURATE (you 80%, him 20%)

SENTIMENT DATA:
┌──────────────────────────────┐
│ You perceive:    "70% load"  │
│ You actually do: "72% load"  │ ✅ Perception accurate
├──────────────────────────────┤
│ Him perceives:   "50-50"     │
│ Him actually do: "28% load"  │ ❌ Perception 22% OFF
│                              │    (doesn't see his under-contribution)
└──────────────────────────────┘

---

WHAT CHANGED vs JANUARY?
Jan 2026 (before app):
   You: 80% | Him: 20% (rough estimate, felt like)
Feb 2026 (with app):
   You: 72% | Him: 28% (measured via app)
   
   IMPROVEMENT: You went from "80% mental load" to "72%"
   = 8% reduction in burden
   = ~20 hours reclaimed in February alone
   
   Why? Anticipation View + Partenaire Notifications reduced:
   - Your decision-making (IA suggestions)
   - His forgetfulness (IA reminders)

---

💬 RECOMMENDED CONVERSATION (tonight):

"Babe, I want to show you something. This app has been tracking what we actually do household-wise.
 
 YOU: You perceive 50-50. But you're actually doing 28% (kids are 47%, that's great).
 
 ME: I perceived 70% load; I actually do 72%.
 
 But THE INVISIBLE WORK (planning, coordinating, anticipating) is 94-6 for me. 
 That's where I'm exhausted — it's the thinking, not the doing.
 
 The app has helped 8% already just by making task visible + sending you reminders.
 
 What if we intentionally redivide the 'invisible work'?
 You could:
 - Decide menus 2x/week (you choose what we eat THU + FRI)
 - Own one child's admin (healthcare, school, activities)
 - Anticipate something: 'Hey, Tom needs new shoes size 33' (without me asking)
 
 Then I'd feel like we're actual partners, not me managing your tasks + kids."

2. Him reads report. Likely reactions:
   
   BEST CASE: "Oh wow, I didn't realize. You're right, the invisible stuff is heavy.
              Let's redesign. I'll own meals WED-FRI and Eva's medical stuff."
   
   DEFENSIVE: "That app is wrong, I do more than 28%."
             → Ask: "What did you do in Feb you think app missed?" (maybe it did)
             → Or: "Okay, let's manually count for March and compare."
   
   DISMISSIVE: "It's not about 50-50, we do what needs doing."
              → Reality check: "But I feel burnt out and you don't. That gap is real."

3. Result depends on couple dynamics:
   
   IF receptive: Start gradual task handoff
      Week 1: He owns menus TUE/WED (decides what, you execute)
      Week 2: He books Eva's next RDV himself
      Week 3: He anticipates something (reminds you, "Tom shoes size 33 soon")
      
      Over 4 weeks: Mental load gap shrinks 72-28 → 60-40 (still unequal, but progress)

   IF defensive: Couple therapy or mediator (product can't solve relationship conflict)

📊 RESULT (if conversation productive)
- ✅ Data transparency: "We finally have shared truth"
- ✅ Behavior change: Partenaire increases invisible work ownership
- ✅ Couple satisfaction: +30% (from feeling "understood")
- ✅ Mental load actual reduction: 5-10% additional (on top of app's 8%)
- ✅ Retention: Sophie feels "heard," stays active in app

BONUS: App can track equity progress over time.
        "Mar 2026: You 72 → 68% | Him 28 → 32% (+4% progress toward balance)"
```

**Mesure de succès**

- ✅ Couple initiates conversation about invisible work
- ✅ Partenaire understanding improves (acknowledges his under-contribution to planning)
- ✅ Concrete behavior changes: Partenaire owns ≥2 invisible tasks
- ✅ Couple satisfaction improves ≥20%
- ✅ Mental load distribution moves toward 50-50 (even if never perfect)

---

## SECTION 6 : RÉSUMÉ EXÉCUTIF & RECOMMANDATIONS

### Tableau de bord : Top Irritants → Top Opportunités IA

| Irritant | Fréquence | Opportunité MVP | Impact | Effort | Priorité | Délai |
|----------|-----------|-----------------|--------|--------|----------|-------|
| **#1 Anticipation constante** | 45 | Anticipation View | 9/10 | Med | **#1** | v0.1 (fév-mar) |
| **#3 Planification repas+courses** | 38 | Meal Planning + Grocery | 8/10 | Med | **#1-2** | v0.1-2 (fév-mar) |
| **#6 Coordination RDV méd** | 32 | Medical RDV Hub | 9/10 | Med | **#1-2** | v0.3 (mar-avr) |
| **#2 "Fallait demander"** | 42 | Task Visibility + Partenaire Coach | 8/10 | Med | **#2-3** | v0.2 (mar) |
| **#15 Notification fatigue** | 18 | Notification Filtering | 7/10 | Low | **#3-4** | v0.1 (rapid) |
| **#5 Équité illusoire** | 31 | Equity Dashboard | 8/10 | High | **#4-5** | v1.0 (avr-mai) |
| **#10 Charge émotionnelle** | 25 | Emotional Wellness | 7/10 | High | **#5-6** | v1.0+ (mai) |

### Stratégie MVP (v0 : Feb-Apr 2026)

**Objectif** : 100 utilisateurs pilotes (France), réduire charge mentale visible ≥30%, valider modèle économique.

**Périmètre minimum** :
1. ✅ Anticipation View (2-week ahead consolidated)
2. ✅ Meal Planning + Smart Grocery
3. ✅ Task Visibility + Basic Partenaire Notifications
4. ✅ Notification Filtering (1 daily digest)
5. ✅ Medical RDV Hub (Doctolib integration)
6. ✅ Onboarding + Family Profile Setup

**Hors MVP (v1+)** :
- ❌ Equity Dashboard (needs 4+ weeks data)
- ❌ Partenaire Coach (behavioral patterns)
- ❌ Emotional Wellness (validation needed)
- ❌ Seasonal Transitions (nice-to-have)
- ❌ Activity Management (secondary feature)

### Tech Stack Recommandé

| Composant | Choice | Rationale |
|-----------|--------|-----------|
| **LLM** | Claude 3.5 Sonnet | Reasoning, GDPR-safe, EU-friendly |
| **Calendar API** | Google Calendar (OAuth) | 80% market penetration, reliable |
| **Medical booking** | Doctolib API | 80% French doctors on Doctolib |
| **Email parsing** | Gmail API + NER (spaCy) | Privacy-safe (not storing emails) |
| **Database** | PostgreSQL + encryption | RGPD compliant |
| **Frontend** | React/React Native + Expo | iOS + Android + web |
| **Backend** | Node.js + Hono/tRPC | Type-safe, fast |
| **Notifications** | Twilio SMS + in-app | Reliable, GDPR-compliant |

### Risques critiques & mitigations

| Risque | Probabilité | Impact | Mitigation |
|--------|------------|--------|-----------|
| **RGPD violations** (child data leak) | Medium | Critical | Encryption E2E, no third-party sharing, CNIL audit |
| **IA hallucinations** (wrong RDV info) | Medium | High | Parent validation (Level 1-2), confidence scoring |
| **User adoption** (too much friction onboard) | High | High | 5-min setup, 1-click Google login, progressive disclosure |
| **Partenaire resentment** (feels microgemed) | Medium | High | Psychology-first messaging, opt-in, no blame |
| **Data fragmentation** (Google ≠ Doctolib ≠ School) | High | Medium | Aggregation layer, fallback manual input |
| **Payment friction** (activity booking) | Low (v0) | Medium | Skip in MVP; add v1 with Stripe |

### Unité économique (CAC & LTV)

**Assumption pour MVP** (France, family market):

- **Monthly price** : €9.99/family
- **CAC** (customer acquisition) : €25-40 (organic + affiliate)
- **Payback period** : 3-5 months
- **LTV** (lifetime value) : €120-200 (assuming 12-month retention 50%, increasing to 70% v1+)
- **LTV:CAC ratio** : 3-8x (healthy, target ≥3x)

**Monétisation** :
- Primary: Freemium (anticipation + 5 free meal plans/month) → Premium €9.99/mo
- Secondary: B2B2C partnership (French health insurance, family apps, daycares)
- Tertiary: Data insights (anonymized, for parenting brands — future, v2+)

### Métriques de succès (Pilot 100 users, 12 weeks)

| Métrique | Target | Success Criteria |
|----------|--------|-----------------|
| **Activation** (user opens app ≥1x/week) | ≥70% | Healthy, shows habit formation |
| **Feature adoption** | Anticipation 80%, Meals 60%, Tasks 50% | MVP hits targets |
| **Retention** (month 3) | ≥60% | Standard for family apps |
| **NPS** (Net Promoter Score) | ≥50 | Very good (willing to recommend) |
| **Mental load reduction** (self-reported) | ≥30% | Core value delivered |
| **Couple satisfaction** (quarterly survey) | +20% | Relationship improves |
| **Time saved** (weekly) | ≥3 hours | Tangible impact |
| **Partenaire engagement** | ≥50% of families | Couple participation critical |

### Prochaines étapes (Immédiat)

**Week 1 (Feb 23-Mar 1)**
- [ ] Validate Google Calendar + Gmail API permissions (GDPR review)
- [ ] Doctolib partnership outreach (API access)
- [ ] Finalize UI wireframes (Anticipation View + Meals)
- [ ] Start backend build (calendar aggregation layer)

**Week 2-4 (Mar 1-22)**
- [ ] Alpha build (Anticipation View + Meal Planning)
- [ ] Internal testing + iteration
- [ ] Onboarding flow design
- [ ] Family profile schema

**Week 5-8 (Mar 22-Apr 19)**
- [ ] Beta soft launch (20-30 testers, friend group)
- [ ] Iterate on feedback
- [ ] Add Medical Hub + Task Visibility
- [ ] Partenaire notification strategy (psychological research)

**Week 9-12 (Apr 19-May 17)**
- [ ] Pilot launch (100 families, France)
- [ ] Data collection + analytics
- [ ] Roadmap v1 finalized
- [ ] Funding pitch (if seeking capital)

---

## Conclusion

La charge mentale parentale est un problème **réel, chiffré, et souffert**. Les solutions existantes (Cozi, TimeTree) **échouent** car elles reproduisent le status quo (plus d'entrade de données) sans résoudre l'anticipation/l'invisibilité.

L'IA offre une opportunité unique :
1. **Agrégation** (calendrier + email + SMS → une vue)
2. **Anticipation** (détecter les besoins futurs)
3. **Délégation** (rendre tâches visibles, responsabiliser le partenaire)
4. **Transparence** (visualiser l'équité, faciliter conversation couple)

**MVP focused** sur les **5 opportunités à haut impact** (Anticipation View, Meal Planning, Task Visibility, Medical Hub, Notifications) peut **réduire la charge mentale de 30-40%** en **3 mois**, avec **product-market fit** clair et **rétention 60%+**.

Le marché (TAM €1.7-4.7B, croissance 20% annuel) existe. Les utilisateurs **supplient** pour cette solution. **First-mover advantage** en Europe/France dans le segment AI-first parental coordination.

**Call to action** : Commencer construction MVP immédiatement (Feb-Mar 2026). Valider avec 100 utilisateurs pilotes (Mar-Apr). Scale si métriques positives (May+).

---

## Annexes

### Annexe A : Sources complètes
- Recherches existantes : 00-framing.md, 01-market.md, 02-competitors.md, 03-user-voice.md
- APIs validées : Google Calendar, Gmail, Doctolib, Twilio
- Frameworks utilisés : JTBD (Christensen), Buyer Personas (Revella), Psychology (Cialdini), Lean Startup (Ries)

### Annexe B : Glossaire IA

| Terme | Définition | Contexte |
|-------|-----------|----------|
| **Event extraction** | Parser email/SMS pour extraire dates/rendez-vous | RDV médicaux, permissions école |
| **Multi-source reasoning** | Combiner données calendar + email + SMS | Anticipation complète |
| **Confidence scoring** | IA attribue % confiance à ses suggestions | Valider avant action (Level 2) |
| **Personalization** | Apprendre préférences famille progressivement | Suggestions menus adaptées |
| **Graduated autonomy** | Progression Level 1 → 3 sur 4+ semaines | Trust-building mère-IA |

### Annexe C : Templates Onboarding

**Day 1 setup (5 minutes)**
```
1. Email signup / Google login
2. "How many kids, how old?" (profile setup)
3. "Grant Google Calendar permission" (1 click OAuth)
4. "Grant Gmail permission" (RDV emails parsing)
5. Done\! First Anticipation View generates.
```

**Day 3 : First Meal Suggestion**
```
"You received meal suggestions for this week.
 Do you like pasta? Which of these 5 menus appeal to you?"
 [Approve 3] [Skip] [Customize]
 
 Grocery list auto-generated.
```

**Day 7 : Task Visibility**
```
"We detected these implicit tasks for Tom's football.
 Should we notify your partner?
 [Yes, send gentle reminder] [No, I'll handle it] [Ask me later]"
```

---

**END OF REPORT**

