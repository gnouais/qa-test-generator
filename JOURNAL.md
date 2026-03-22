# 🧪 QA Test Generator — Journal de bord (Plan 90 jours)

---

## Infos projet
- **Début du plan** : 15/03/2026
- **Objectif 90 jours** : 100-500 utilisateurs réels + retours terrain exploitables
- **URL app** : https://app-test-generator.streamlit.app
- **Repo** : https://github.com/TesteurGenAI/qa-test-generator

---

## Phase 1 — Jours 1 à 30 : Prototype

### Jour 1 (15-16/03/2026) — ✅ FAIT
- [x] Prompt QA qui génère cas de test, edge cases, risques
- [x] App Streamlit déployée sur Streamlit Cloud
- [x] API Gemini 2.5 Flash connectée (secret Streamlit)
- [x] Clé API masquée — zéro config pour les testeurs
- [x] Lien envoyé à 8 testeurs
- [x] Retours projet précédent : 8/8 n'avaient pas testé (trop de friction)
- [x] 4 testeurs ont testé la v1 et donné des retours
- [x] Itération v2 : ajout champ "Contexte applicatif" + prompt amélioré pour des cas de test exécutables
- [x] Message envoyé à Luis pour retester la v2
- [x] .gitignore ajouté
- [x] Journal de bord créé

### Jour 2 (17/03/2026) — ✅ FAIT
- [x] 11 testeurs au total — 10 retours exploitables
- [x] Post LinkedIn publié (carrousel + CTA "commente QA")
- [x] Prompt corrigé : plus de données inventées — [À DÉFINIR PAR LE TESTEUR] quand pas de contexte
- [x] Export CSV compatible Jira/Xray ajouté
- [x] Fix boutons d'export : persistent après téléchargement (session_state)
- [x] Luis a retesté la v2 — validé, nouvelle suggestion sur les données
- [x] Import CSV dans Jira testé et validé
- [x] Fichier de configuration Jira sauvegardé pour imports futurs
- [x] Troncature des champs à 255 caractères (limite Jira champs texte court)
- [x] Newsletter LinkedIn "Le Testeur Augmenté" configurée

### Jour 3 (18/03/2026) — ✅ FAIT
- [x] Post LinkedIn : 2 407 impressions, 48 réactions, 18 commentaires, 5 republications
- [x] 9 personnes ont commenté "QA" — tous contactés en DM avec le lien
- [x] Nouveau contact : Elodie Juino — intéressée, veut une démo après sa recette
- [x] Export Gherkin / BDD ajouté — fichier .feature téléchargeable
- [x] Preview Gherkin intégré dans l'app (onglet avec coloration syntaxique)
- [x] 4 formats d'export disponibles : Markdown, TXT, CSV Jira, Gherkin
- [x] 5 itérations produit livrées en 3 jours
- [x] Messages envoyés à Lyne et Aymen pour retester le Gherkin

### Jour 4 (19-20/03/2026) — ✅ FAIT
- [x] Newsletter #1 publiée : "Les testeurs passent encore 2h à écrire des cas de test. J'ai réduit ça à 30 secondes avec l'IA"
- [x] 928 abonnés à la newsletter en 24h
- [x] Karima SORIANO (Test Manager Bforbank) — lead enterprise chaud
- [x] Luis reteste v4-v5 : retour critique — [À DÉFINIR PAR LE TESTEUR] improductif, veut un dialogue interactif IA/testeur
- [x] Bouton "Voir une démo — pré-remplir avec un exemple" ajouté
- [x] Optimisation performance : CSV et Gherkin générés à la demande (pas automatiquement)
- [x] Temps de génération ramené à ~30 secondes (1 seul appel API au lieu de 3)
- [x] Design épuré : icônes SVG émeraude, suppression des emojis
- [x] Post LinkedIn #2 préparé (hallucinations IA dans les tests)
- [x] Lyne engagée — va retester le Gherkin

### Leçons apprises
- La friction tue l'adoption : Ollama + API tokens + install = personne ne teste
- Zéro installation = condition non négociable
- "Pas eu le temps" = "trop compliqué pour que je fasse l'effort"
- Le contexte applicatif change tout : sans contexte, les cas de test sont génériques et inexécutables (retour Luis)
- Les retours terrain sont plus utiles que la réflexion solo — itérer en < 24h crée de la confiance
- Bug Diawando = restriction géo API Gemini (Guinée-Conakry), pas un bug de code
- L'export CSV Jira est la feature la plus demandée (3 testeurs indépendamment)
- Les LLM inventent des données si on ne leur interdit pas explicitement — il faut des règles très strictes dans le prompt
- Streamlit : les boutons disparaissent au rerun — utiliser session_state pour persister les résultats
- Jira : les champs custom texte court sont limités à 255 caractères et ne supportent pas les retours à la ligne
- Le CTA "commente QA" sur LinkedIn génère des leads qualifiés — 9 commentaires QA en 24h
- Montrer aux testeurs que leur feedback devient une feature en 24h crée un cycle vertueux de confiance
- 928 abonnés newsletter en 24h — le marché QA + IA a une demande forte
- Engagement LinkedIn ≠ utilisation réelle — les gens s'abonnent mais ne testent pas forcément
- 3 appels API séquentiels = 1min30 — inacceptable. Générer à la demande, pas automatiquement
- Le [À DÉFINIR PAR LE TESTEUR] est une demi-solution — Luis veut un dialogue interactif (prochaine évolution majeure)

### En attente
- [ ] Publier le post LinkedIn #2 (hallucinations IA)
- [ ] Retour de Lyne sur le Gherkin
- [ ] Retour de Karima (Bforbank) — relancer dans 1 semaine
- [ ] Retour de Diawando avec VPN
- [ ] Retour d'Elodie après sa recette (relancer dans 2 semaines)
- [ ] Faire la vidéo démo 30 secondes
- [ ] Convertir les 928 abonnés newsletter en utilisateurs actifs

---

## Retours testeurs

### Testeur 1 — Luis Cavalheiro
- **A testé ?** : Oui (v1 + v2 + v4-v5)
- **Date** : 16-19/03/2026
- **Retour v1 :**

> Je sais que c'est un prototype mais je vois 2 grandes limitations :
> 1. Comment passer le contexte de la User Story
> 2. Comment generer les données de test

- **Retour v2 :**

> C'est beaucoup mieux. Maintenant l'appli devrait demander au user de spécifier les données quand celles ci ne sont pas définies au lieu des générer des fausses données

- **Retour v4-v5 :**

> C'est pas mieux :( Des steps comme celui-ci sont une perte de temps: Laisser le champ [NOM DU CHAMP EMAIL – À DÉFINIR PAR LE TESTEUR] vide.
> J'imaginais plus un dialogue entre l'IA et le testeur pour obtenir des informations manquante autours des données. Ajouter "À DÉFINIR PAR LE TESTEUR" est tres improductif sont l'IA génère des centaines de tests...
> L'idée est d'accélérer la génération des tests mais des tests prêts à être exécutés

- **Actions prises** : v2 contexte, v3 prompt strict, v4-v5 — Luis demande un dialogue interactif IA/testeur. Noté au backlog comme évolution majeure.

### Testeur 2 — Moez Ben Khaled
- **A testé ?** : Oui (v1)
- **Date** : 16/03/2026
- **Retour :**

> J'ai testé l'outil cet aprem et c'est vraiment top.
> Y a t'il un moyen d'évoluer l'outil pour la création des TA avec les cas de test ?

- **Action prise** : Noté pour backlog — génération de tests d'acceptance (TA)

### Testeur 3 — Romain De Page
- **A testé ?** : Oui (v1)
- **Date** : 16/03/2026
- **Retour :**

> J'ai testé ton outil il est vraiment bien. J'ai même exporté en .txt, c'est vraiment bien.

- **Action prise** : Aucune — retour positif

### Testeur 4 — Diawando DIAWARA
- **A testé ?** : Partiellement
- **Date** : 16/03/2026
- **Retour :**

> Les cas de tests ne sont pas générés. Je vais activer mon vpn.

- **Action prise** : Restriction géo API Gemini (Guinée-Conakry). En attente.

### Testeur 5 — Ken Defossez
- **A testé ?** : Oui
- **Date** : 17-18/03/2026
- **Retour :**

> Congratz ! Bug PixelConnect. Sinon la disjonction des cas de test et risques est top !
> On nous demande des initiatives AI, la tienne est particulièrement intéressante et aboutie.

- **Action prise** : Bug corrigé. Signal B2B fort.

### Testeur 6 — Aymen Ismail
- **A testé ?** : Oui
- **Date** : 17/03/2026
- **Retour :**

> Appli fonctionne parfaitement. Export CSV pour JIRA/XRAY. Ajouter gherkin et CSV exploitable.

- **Action prise** : CSV ajouté (Jour 2). Gherkin ajouté (Jour 3).

### Testeur 7 — Tasnim Ferchichi
- **A testé ?** : Oui
- **Date** : 17/03/2026
- **Retour :**

> Assez cohérent avec contexte. Faire une matrice de test serait bien.

- **Action prise** : Matrice de test au backlog.

### Testeur 8 — Kalidou BA
- **A testé ?** : Oui
- **Date** : 17/03/2026
- **Retour :**

> Super APP. Possible de linker APK ou URL pour générer automatiquement ?

- **Action prise** : Vision long terme.

### Testeur 9 — Nicolas Trzcinski
- **A testé ?** : Oui
- **Date** : 17/03/2026
- **Retour :**

> Intéressant ! Je travaille sur un projet similaire connecté Jira/Xray. Collaboration future ?

- **Action prise** : Déclinée pour l'instant.

### Testeur 10 — Lyne Voctabah
- **A testé ?** : Oui
- **Date** : 17-20/03/2026
- **Retour :**

> Sauvegarde les user stories ? Gain de temps, simple, bien détaillé. Approche BDD ?

- **Action prise** : Historique au backlog. Gherkin ajouté. Reteste en cours.

### Testeur 11 — Elodie Juino
- **A testé ?** : Non (pas encore)
- **Date** : 18/03/2026
- **Retour :**

> Compatible client lourd ? Avec plaisir après notre recette. Ton outil m'aidera sûrement.

- **Action prise** : Relancer dans 2 semaines.

### Testeur 12 — Karima SORIANO
- **A testé ?** : Non (pas encore)
- **Date** : 20/03/2026
- **Retour :**

> Intéressée, l'IA hallucine parfois quand les critères d'acceptance ne sont pas clairs. Faut tester sur une vraie US depuis le PC pro si le proxy ne bloque pas.

- **Action prise** : Lead enterprise (Bforbank). Relancer dans 1 semaine.


### Testeur 13 — Rezika D
- **A testé ?** : Oui
- **Date** : 22/03/2026
- **Retour :**

> Merci beaucoup, je viens de faire un test, et franchement je trouve que ça marche très bien,
> la liste des cas de tests est complète y a les cas passants et non passants, il faut quand même bien vérifier derrière si tout est ok,
> après j'ai déjà essayé de faire la même chose sur copilote pa ex et j'ai eu presque le même résultat en terme de cas de tests
> mais c'est bien d'voir un agent IA spécialement fait pour les tests

### Leads LinkedIn (post carrousel — 18/03/2026)
- Lewis Dieu Ne Dort BABE YAKA — Senior QA Engineer — DM envoyé
- Ali KAR — Ingénieur Testing Agile ISTQB — DM envoyé
- Ahlem Ayari — Étudiante ISITCOM — DM envoyé
- Abdoulahi DIABY — Consultant QA SAP — DM envoyé
- Ala Eddine Benna — Testeur logiciel ISTQB — DM envoyé
- Abdelkrim BOUHRAOUA — QA Testeur ISTQB — DM envoyé
- Abdessamad Nacih — Ingénieur QA — DM envoyé

---

## Métriques

| Métrique | Objectif Phase 1 | Actuel |
|----------|-----------------|--------|
| Prototype utilisable | ✅ | ✅ |
| Testeurs confirmés | 10+ | 12 ✅ |
| Leads LinkedIn (DM envoyés) | - | 7 nouveaux |
| Testeurs qui ont testé | 5+ | 10 ✅ |
| Retours exploitables | 3+ | 11 ✅ |
| Itérations produit | - | 7 (contexte, prompt, CSV, fix boutons, Gherkin, démo, perf) |
| Formats d'export | - | 4 (Markdown, TXT, CSV Jira, Gherkin) |
| Post LinkedIn carrousel | 1 | 1 ✅ (2407 impressions, 48 réactions, 18 commentaires) |
| Newsletter publiée | 1 | 1 ✅ |
| Abonnés newsletter | - | 928 |
| Import Jira validé | - | ✅ |
| Temps de génération | 30s | ~30s ✅ |

---

## Décisions prises
1. **Stack** : Streamlit + Gemini 2.5 Flash (pas Ollama)
2. **Architecture** : 1 appel LLM principal, CSV et Gherkin à la demande
3. **Go-to-market** : Option A — PLG, self-service, 19-49€/mois
4. **Priorité** : Retours terrain AVANT nouvelles features
5. **Champ contexte applicatif** : ajouté suite retour Luis
6. **Prompt strict** : ne jamais inventer de données — [À DÉFINIR PAR LE TESTEUR]
7. **Export CSV Jira/Xray** : ajouté suite retours Aymen, Nicolas, Moez
8. **Export Gherkin/BDD** : ajouté suite retours Aymen, Lyne
9. **Collaboration Nicolas** : déclinée pour l'instant, reste solo
10. **Repo GitHub public** : nécessaire pour Streamlit Cloud gratuit
11. **Formation** : en mode maintenance, focus sur le produit QA Test Generator
12. **Newsletter** : "Le Testeur Augmenté" — hebdomadaire — #1 publié
13. **Performance** : CSV et Gherkin générés à la demande, pas automatiquement
14. **Bouton démo** : pré-remplissage d'exemple pour convertir les visiteurs

## Backlog (demandé par les testeurs)
- [x] Corriger le prompt — ne pas inventer de données (Luis v2)
- [x] Export CSV compatible Jira/Xray (Aymen, Nicolas, Moez)
- [x] Import Jira testé + fichier de config sauvegardé
- [x] Export Gherkin / BDD (Aymen, Lyne)
- [x] Bouton démo pré-rempli
- [x] Optimisation performance (1 appel API au lieu de 3)
- [ ] **Dialogue interactif IA/testeur pour compléter les données manquantes (Luis v4-v5)** — ÉVOLUTION MAJEURE
- [ ] Historique / sauvegarde des générations (Lyne)
- [ ] Génération de tests d'acceptance / TA (Moez)
- [ ] Matrice de test (Tasnim)
- [ ] Vidéo démo 30 secondes
- [ ] Analyse d'app par URL/APK (Kalidou) — vision long terme
- [ ] Gestion des restrictions géographiques API (Diawando)

---

## Phase 2 — Jours 30 à 60 : Validation marché
*(à compléter quand Phase 1 terminée)*

## Phase 3 — Jours 60 à 90 : Produit
*(à compléter quand Phase 2 terminée)*
