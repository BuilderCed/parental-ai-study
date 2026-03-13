# Glossaire — Etude IA & Charge Mentale Parentale

> Base de connaissance consultable | Version 1.0 | 23 fevrier 2026
> References : 00-framing.md, 01-market.md, 02-competitors.md, 03-user-voice.md, 04-personas.md

---

| Terme | Definition | Reference |
|-------|-----------|-----------|
| **AI Act** | Reglementation europeenne sur l'intelligence artificielle (entree en vigueur 2025-2027). Classe les systemes IA par niveau de risque (inacceptable, eleve, limite, minimal). Impact direct sur les apps IA traitant donnees enfants. | 00-framing.md §3.2 |
| **Algorithme SweetSpot** | Algorithme proprietaire de Huckleberry (ML-based) qui predit les fenetres de sommeil optimales pour les nourrissons. Exemple de moat par donnee specialisee. | 02-competitors.md §12 |
| **Anticipation** | Composante de la charge mentale consistant a penser en avance aux besoins futurs (RDV, vetements de saison, fournitures scolaires, anniversaires). Represente ~30% de la charge invisible. | 00-framing.md §1 |
| **App fatigue** | Syndrome d'epuisement face a la multiplication des applications. Parents utilisent 5-7 apps famille, veulent consolidation. Barriere a l'adoption de nouveaux outils. | 00-framing.md §3.2 |
| **ARPU** | Average Revenue Per User. Revenu moyen par utilisateur. Indicateur cle pour evaluer la sante financiere d'un produit SaaS ou app. | 02-competitors.md tendances |
| **Async / Synchrone** | Fonctionnalites asynchrones = utilisables sans que tous les membres soient presents simultanement (calendrier, listes). Gagnent vs synchrones (appels video). | 00-framing.md §3.2 |
| **B2B2C** | Business-to-Business-to-Consumer. Modele de distribution passant par une entreprise intermediaire (pediatre, ecole, assurance) pour atteindre le consommateur final. LTV superieur au B2C direct. | 00-framing.md §6.1 |
| **B2C** | Business-to-Consumer. Vente directe au consommateur via app stores. CAC $10-20/famille, churn risque. | 02-competitors.md §tendances |
| **Brain fog parental** | Fatigue cognitive intense observee vers 19h chez les parents portant la majorite de la charge mentale. Incapacite a prendre des decisions de qualite en fin de journee. | 04-personas.md §Sophie |
| **CAC** | Customer Acquisition Cost. Cout d'acquisition d'un client. Benchmark apps parentales : $10-20 par famille (B2C). B2B2C = CAC faible mais cycle vente long. | 02-competitors.md §tendances |
| **CAF** | Caisse d'Allocations Familiales. Organisme francais versant aides familles (subvention creche, allocations, aide parents isoles). Genere une charge administrative specifique (declarations, re-evaluations). | 04-personas.md §differences-culturelles |
| **CAGR** | Compound Annual Growth Rate. Taux de croissance annuel compose. Marche parenting apps : 20-22% (2024-2032). Europe : 18-22%, soit 2x plus rapide que USA. | 00-framing.md §3.1 |
| **Charge emotionnelle** | Composante de la charge mentale consistant a gerer les etats emotionnels des membres de la famille (consoler, motiver, gerer conflits). Partiellement non-delegable a l'IA. | 00-framing.md §1 |
| **Charge mentale** | Travail cognitif et emotionnel invisible de gestion du quotidien familial. Inclut anticipation, coordination, decision, suivi, charge emotionnelle. Portee a 71% par les meres (vs 29% peres). | 00-framing.md §1 |
| **Churn** | Taux de desabonnement mensuel. Benchmark apps parentales : 70% abandon Cozi a 3 mois. Objectif MVP : <5% mensuel. | 00-framing.md §3.1, 02-competitors.md §tendances |
| **Contrat d'autonomie** | Cadre definissant les niveaux d'autonomie accordes a l'IA dans le produit. Recommandation MVP : niveaux 1-2 (suggest/draft) ; niveau 3 (execute) apres confiance etablie ; niveau 4 hors scope. | 00-framing.md §2.3 |
| **Conversion rate** | Taux de conversion freemium vers offre payante. Benchmark apps parentales : 5-25%. Kinedu : ~20-25%. Cozi : ~5%. | 02-competitors.md §tendances |
| **CSP+** | Categories Socio-Professionnelles superieures (cadres, professions intellectuelles superieures). Cible principale etude : Sophie (€65-85k/an), Karim (€75-95k/an). Forte WTP. | 04-personas.md §Sophie, §Karim |
| **D7 / D30** | Day 7 / Day 30 retention. Pourcentage d'utilisateurs actifs au jour 7 / 30 apres inscription. Objectifs MVP : D7 >40%, D30 >25%. | 02-competitors.md §recommandations |
| **DAU** | Daily Active Users. Utilisateurs actifs quotidiens. Cozi ~50k, FamilyWall ~150k estimes. | 02-competitors.md §Cozi, §FamilyWall |
| **Decision fatigue** | Epuisement decisionnel lie au nombre excessif de micro-decisions quotidiennes (menus, vetements, activites). Affecte la qualite des decisions en fin de journee. | 04-personas.md §Sophie |
| **DPIA** | Data Protection Impact Assessment. Analyse d'impact relative a la protection des donnees (obligatoire RGPD pour traitements a risque eleve). Requis pour apps traitant donnees d'enfants. | 00-framing.md §7 |
| **Ecart de perception** | Gap entre la perception masculine (partage equitable) et la realite (asymetrie). 65% des peres pensent le partage equitable alors que 71% des meres portent la charge. | 00-framing.md §1 |
| **Feature parity** | Situation ou deux produits offrent les memes fonctionnalites sans differentiation. FamCal vs Cozi = feature parity, pas de moat. | 02-competitors.md §FamCal |
| **Freemium** | Modele economique avec tier gratuit fonctionnel + tier payant premium. Dominant dans les apps parentales (70% des acteurs Tier 1-2). | 02-competitors.md §resume |
| **GAP (produit)** | Besoin du marche non satisfait par les acteurs existants. Gap majeur identifie : aucun acteur ne combine coordination + anticipation IA + visibilite charge mentale + equite couple. | 00-framing.md §3.3 |
| **Geofencing** | Declenchement automatique d'actions basees sur la localisation geographique (ex: alerte quand enfant quitte l'ecole). Utilise par ClanPlan, Bark, Aura. | 02-competitors.md §ClanPlan |
| **IA-first** | Architecture produit ou l'IA est au coeur de la valeur (non bolt-on). Tier 4 emergent : TinyPal, Ollie, May. Retention superieure aux apps traditionnelles. | 02-competitors.md §tendances |
| **JTBD** | Jobs To Be Done. Framework d'analyse centree sur la mission que le client "recrute" un produit pour accomplir. Ex: "Quand la semaine est chargee, je veux anticiper pour ne rien oublier." | 04-personas.md §framework |
| **Laicite** | Principe de separation Etat-religion en France. Impacte les familles diaspora (ex: Aminata) devant naviguer entre ecole laique et pratiques culturelles/religieuses. | 04-personas.md §differences-culturelles |
| **LTV** | Lifetime Value. Revenu total genere par un client sur toute la duree de la relation. B2B2C (sante, ecoles) = LTV $5-15K/an vs B2C = LTV $40-120/an. | 00-framing.md §6.1 |
| **Maple** | Concurrent Tier 1 (Canada). Family organizer avec IA basique. Prix : gratuit + $9.99/mo. Present dans la matrice comparative features. | 02-competitors.md §matrice |
| **Moat** | Avantage concurrentiel defensible a moyen terme. Types identifies : donnees specialisees (Huckleberry), habitudes (Cozi), integrations (FamilyWall), expertise domaine (May+pediatres). | 00-framing.md §3.2 |
| **MVP** | Minimum Viable Product. Produit minimum viable. Contrat d'autonomie recommande : niveaux 1-2. Cibles MVP : Sophie + Karim + Nadia. Timeline : 4 sprints (~30 jours). | 00-framing.md §2.3, §5 |
| **NPS** | Net Promoter Score. Indice de recommandation client (-100 a +100). >40 = bon. Objectifs : Sophie 45+, Nadia 55+, Karim 35+. Industrie : 20-30%. | 02-competitors.md §recommandations |
| **Niveau autonomie IA (0-4)** | Echelle de delegation a l'IA : 0=manuel, 1=suggest, 2=draft, 3=execute, 4=autonome. MVP cible niveaux 1-2. Niveau 4 exclu (risque RGPD + confiance). | 00-framing.md §2.3 |
| **PMI** | Protection Maternelle et Infantile. Service public francais offrant bilans de sante gratuits pour enfants 0-3 ans. Integrer au calendrier app = avantage differentiant FR. | 04-personas.md §differences-culturelles |
| **Remittances** | Transferts d'argent des diaspora vers famille dans le pays d'origine. Aminata : €300/mois au Senegal. Genere charge financiere et emotionnelle specifique. | 04-personas.md §Aminata |
| **RGPD** | Reglement General sur la Protection des Donnees. Reglementation europeenne (2018). Contraintes specifiques pour donnees enfants (<16 ans). Avantage competitif pour startups EU privacy-native (fenetre 12-18 mois). | 00-framing.md §3.2 |
| **SAM** | Serviceable Addressable Market. Part du TAM accessible compte tenu de la geographie, du segment et des canaux de distribution. Europe : 29% du TAM global (~$308-489M). | 00-framing.md §3.1 |
| **Scale-up** | Entreprise en phase de croissance rapide. Par convention : $10M-100M ARR. Cozi, FamilyWall, Kinedu = scale-ups matures. | 02-competitors.md §statuts |
| **Series A/B/C** | Rounds de financement de capital-risque. A = premier tour majeur (~$5-15M). B = acceleration (~$15-50M). C = expansion ($50M+). May (FR) : Serie A €7M. | 02-competitors.md §May |
| **SOM** | Serviceable Obtainable Market. Part realistement capturable. France estimee : $25-60M (2024). Objectif annee 1 : 1-3% du SOM francais. | 00-framing.md §3.1 |
| **TAM** | Total Addressable Market. Taille totale du marche adressable. TAM global parenting apps : $1.7-4.7B (2024). TAM AI in childcare : $4.7B → $35.2B (2034). | 00-framing.md §3.1 |
| **Taches invisibles** | Taches de gestion familiale non observables directement (anticipation, coordination, suivi). Representent ~80% du poids reel de la charge mentale. | 00-framing.md §2.2 |
| **Taches visibles** | Taches de gestion familiale observables (menage, cuisine, transport, hygiene). Representent ~20% du poids reel de la charge mentale. | 00-framing.md §2.1 |
| **Unicorn** | Entreprise valorisee $1B+. Notion (workspace) = unicorn ($10B+). Aucun acteur parenting apps n'est unicorn en 2024. | 02-competitors.md §Notion |
| **WTP** | Willingness To Pay. Disposition a payer. Sophie : €9.99-19.99/mois. Karim : €7.99-14.99/mois. Nadia : €3.99-9.99/mois. Aminata : €6.99-12.99/mois. | 04-personas.md §WTP par persona |

---

> 50 termes documentes | Mise a jour : 23 fevrier 2026
