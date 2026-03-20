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
- [x] Preview Gherkin intégré dans l'app (expander avec coloration syntaxique)
- [x] 4 formats d'export disponibles : Markdown, TXT, CSV Jira, Gherkin
- [x] 5 itérations produit livrées en 3 jours
- [x] Messages envoyés à Lyne et Aymen pour retester le Gherkin

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

### En attente
- [ ] Retours des 9 nouveaux leads LinkedIn
- [ ] Retour de Lyne et Aymen sur le Gherkin
- [ ] Retour de Diawando avec VPN
- [ ] Retour d'Elodie après sa recette (relancer dans 2 semaines)
- [ ] Premier numéro de la newsletter "Le Testeur Augmenté"

---

## Retours testeurs

### Testeur 1 — Luis Cavalheiro
- **A testé ?** : Oui (v1 + v2)
- **Date** : 16-17/03/2026
- **Retour v1 :**

> Je sais que c'est un prototype mais je vois 2 grandes limitations :
> 1. Comment passer le contexte de la User Story
> 2. Comment generer les données de test
> Pour les quelques cas que j'ai essayé, je ne vois pas un user delta etre capable d'executer les cas de tests sans une bonne connaissance de l'application. Pour moi, un bon cas de test doit contenir suffisamment d'information que "mr tout le monde" peut l'executer sans poser de question...

- **Retour v2 :**

> C'est beaucoup mieux. Maintenant d'un point de vue pratique l'appli devrait demander au user de spécifier les données quand celles ci ne sont pas définies au lieu des générer des fausses données

- **Actions prises** : Ajout champ contexte (v2), puis correction prompt pour ne plus inventer de données (v3)

- **A testé ?** : Oui (V4-v5)
- **Date** : 19/03/2026
- **Retour v4-v5 :**


- **Retour v4-v5  :**

Luis Cavalheiro     11:06
> C'est pas mieux :(
> Des steps comme celui-ci sont une perte de temps:
> Laisser le champ [NOM DU CHAMP EMAIL – À DÉFINIR PAR LE TESTEUR] vide.

> J'imaginais plus un dialogue entre l'IA et le testeur pour obtenir des informations manquante autours des données. Ajouter "À DÉFINIR PAR LE TESTEUR" est tres improductif > > sont l'IA génère des centaines de tests...
> Amadou FOFANA a envoyé les messages suivants à 11:21
> Amadou FOFANA     11:21
> Hello Luis,
> Merci pour ton précieux feed-back. 
> Voir le profil de Amadou Amadou FOFANA
> Amadou FOFANA     11:29
> Tu as tout à fait raison.
> En fait, ton retour met le doigt sur la vraie évolution utile du produit.

> L’objectif ne devrait pas être de sortir des champs “à définir par le testeur”, mais plutôt de détecter automatiquement les informations manquantes et de proposer un > échange interactif dans l’app pour les compléter avant la génération finale. 😉👍🏾✨✨ Bien vu. 

> Autrement dit, au lieu de laisser des blancs dans les tests, l’IA devrait jouer son rôle de copilote et poser les bonnes questions au testeur au bon moment.

> Merci Luis, c’est un très bon retour produit.

> Je vais le prendre en compte
> Luis Cavalheiro a envoyé les messages suivants à 11:31
> Voir le profil de Luis Luis Cavalheiro
> Luis Cavalheiro     11:31
> tout à fait.
> L'idéé est d'accélérer l génération des tests mais des tests  pret à etre executé


### Testeur 2 — Moez Ben Khaled
- **A testé ?** : Oui (v1)
- **Date** : 16/03/2026
- **Retour :**

> J'ai testé l'outil cet aprem et c'est vraiment top.
> Juste une question : Des fois les PO rédigent mal les tests d'acceptation et c'est très important pour la synchro Squash/Jira et l'automatisation par exemple, y a t'il un moyen d'évoluer l'outil pour la création des TA avec les cas de test stp?

- **Action prise** : Noté pour backlog — génération de tests d'acceptance (TA)

### Testeur 3 — Romain De Page
- **A testé ?** : Oui (v1)
- **Date** : 16/03/2026
- **Retour :**

> J'ai testé ton outil il est vraiment bien. Tu l'as fait avec quoi?
> Oui niquel j'ai bien eu les case de tests et je les ai même exportés en .txt pour voir c'est vraiment bien

- **Action prise** : Aucune — retour positif, export fonctionne

### Testeur 4 — Diawando DIAWARA
- **A testé ?** : Partiellement
- **Date** : 16/03/2026
- **Retour :**

> Je constate que les cas de tests ne sont pas générés après soumission de la user story.
> Je vais activer mon vpn et reprendre.

- **Action prise** : Restriction géographique API Gemini (Guinée-Conakry). En attente retour avec VPN.

### Testeur 5 — Ken Defossez
- **A testé ?** : Oui
- **Date** : 17-18/03/2026
- **Retour :**

> Je viens de tester ton outil QA version web, congratz ! Petit retour : il m'a parlé de PixelConnect sans que j'y fasse référence. Mais sinon la disjonction des cas de test et risques pour ma US est top !

> Bonsoir Amadou j'ai une semaine chargée mais des que j'ai un moment je me remets dessus pour le challenger davantage. On nous demande des initiatives AI, la tienne est particulièrement intéressante et aboutie 👏

- **Action prise** : Bug PixelConnect corrigé (prompt v3). Signal B2B fort — "on nous demande des initiatives AI".

### Testeur 6 — Aymen Ismail
- **A testé ?** : Oui
- **Date** : 17/03/2026
- **Retour :**

> Ton appli fonctionne parfaitement et j'ai pu transformer les cas de test générés en format csv pour les intégrer directement dans JIRA/XRAY.
> Ca pourra être une idée pour évoluer ton appli en ajoutant d'autres façons d'exporter : en langage gherkin ou sous fichier csv directement exploitable dans JIRA/XRAY.

- **Action prise** : Export CSV Jira/Xray ajouté (Jour 2). Export Gherkin ajouté (Jour 3). Message envoyé pour retester.

### Testeur 7 — Tasnim Ferchichi
- **A testé ?** : Oui
- **Date** : 17/03/2026
- **Retour :**

> Comme précisé sur le site il faut bien entendu donner des infos concernant le contexte sinon ça a l'air assez cohérent !
> Pour vérifier les premiers tests, peut être qu'il serait bien de faire une matrice de test.

- **Action prise** : Matrice de test notée au backlog.

### Testeur 8 — Kalidou BA
- **A testé ?** : Oui
- **Date** : 17/03/2026
- **Retour :**

> C'est vraiment un super APP et il va beaucoup nous aider avec les cas de tests.
> Est-ce possible de linker soit l'APK ou le lien web et dès qu'on clique sur les fonctionnalités l'application génère les cas de tests ?

- **Action prise** : Feature ambitieuse (analyse d'app par URL/APK) — notée pour vision long terme.

### Testeur 9 — Nicolas Trzcinski
- **A testé ?** : Oui
- **Date** : 17/03/2026
- **Retour :**

> Intéressant ton appli ! Je travaille également sur un projet web du même genre, connecté à Jira/Xray.
> Hâte de voir comme tu avances, qui sait on pourrait collaborer dans le futur sur un même projet.

- **Action prise** : Collaboration déclinée pour l'instant. Reste solo.

### Testeur 10 — Lyne Voctabah
- **A testé ?** : Oui
- **Date** : 17-18/03/2026
- **Retour :**

> Est-ce que le lien sauvegarde les user stories ?
> Je trouve que l'outil fait vraiment gagner du temps sur la rédaction. Les cas de test sont bien détaillés et faciles à comprendre. J'aime le fait que ce soit hyper simple.

> Je dirai utiliser l'approche BDD pour les cas de test ?

- **Action prise** : Historique noté au backlog. Export Gherkin/BDD ajouté (Jour 3). Message envoyé pour retester.

### Testeur 11 — Elodie Juino
- **A testé ?** : Non (pas encore)
- **Date** : 18/03/2026
- **Retour :**

> Merci, on est en client lourd, est ce compatible ?
> Ça sera avec plaisir après notre grand rech actuel. Ton outil m'aidera sûrement beaucoup.

- **Action prise** : Lead chaud. Relancer dans 2 semaines après sa recette.



### Karima SORIANO
- **A testé ?** : Non (pas encore)
- **Date** : 20/03/2026
- **Retour :**

> Je suis intéressée par cet outil qui génère les cas de tests,
> j’ai commencé à expérimenter un peu mais les résultats ne sont pas tous pertinents,
> l’Ia hallucine parfois quand le résultat n’est pas clairement explicite dans les critères d’acceptance
> Amadou FOFANA il faut que je l’essaye sur une vraie Us
> donc sur mon pc pro si ça fonctionne,
> et si le lien n’est pas bloqué par notre proxy

- **Action prise** : lead chaud enterprise. Relancer dans une semaine si elle n'a pas donné de retour.

### Leads LinkedIn (post carrousel — 18/03/2026)
- Lewis Dieu Ne Dort BABE YAKA — Senior QA Engineer — commenté "QA" — DM envoyé
- Ali KAR — Ingénieur Testing Agile ISTQB — commenté "QA" — DM envoyé
- Lyne VOCTABAH — commenté "QA" — déjà testeuse
- Kalidou BA — commenté "QA" — déjà testeur
- Ahlem Ayari — Étudiante ISITCOM — commenté "QA" — DM envoyé
- Abdoulahi DIABY — Consultant QA SAP — commenté "QA" — DM envoyé
- Ala Eddine Benna — Testeur logiciel ISTQB — commenté "QA" — DM envoyé
- Abdelkrim BOUHRAOUA — QA Testeur ISTQB — commenté "QA" — DM envoyé
- Abdessamad Nacih — Ingénieur QA — commenté "QA" — DM envoyé
- Elodie Juino — commenté "QA !" — déjà en contact DM
- Karima SORIANO - Test Manager/Lead Chapter QA chez Bforbank

---

## Métriques

| Métrique | Objectif Phase 1 | Actuel |
|----------|-----------------|--------|
| Prototype utilisable | ✅ | ✅ |
| Testeurs confirmés | 10+ | 11 ✅ |
| Leads LinkedIn (DM envoyés) | - | 7 nouveaux |
| Testeurs qui ont testé | 5+ | 10 ✅ |
| Retours exploitables | 3+ | 10 ✅ |
| Itérations produit | - | 5 (contexte, prompt, CSV, fix boutons, Gherkin) |
| Formats d'export | - | 4 (Markdown, TXT, CSV Jira, Gherkin) |
| Post LinkedIn | 1 | 1 ✅ (2407 impressions, 48 réactions, 18 commentaires) |
| Import Jira validé | - | ✅ |
| Newsletter configurée | - | ✅ ("Le Testeur Augmenté") |

---

## Décisions prises
1. **Stack** : Streamlit + Gemini 2.5 Flash (pas Ollama)
2. **Architecture** : 1 appel LLM principal + 1 appel CSV + 1 appel Gherkin
3. **Go-to-market** : Option A — PLG, self-service, 19-49€/mois
4. **Priorité** : Retours terrain AVANT nouvelles features
5. **Champ contexte applicatif** : ajouté suite retour Luis
6. **Prompt strict** : ne jamais inventer de données — [À DÉFINIR PAR LE TESTEUR]
7. **Export CSV Jira/Xray** : ajouté suite retours Aymen, Nicolas, Moez
8. **Export Gherkin/BDD** : ajouté suite retours Aymen, Lyne
9. **Collaboration Nicolas** : déclinée pour l'instant, reste solo
10. **Repo GitHub public** : nécessaire pour Streamlit Cloud gratuit
11. **Formation** : en mode maintenance, focus sur le produit QA Test Generator
12. **Newsletter** : "Le Testeur Augmenté" — hebdomadaire — premier numéro à écrire

## Backlog (demandé par les testeurs)
- [x] Corriger le prompt — ne pas inventer de données (Luis v2)
- [x] Export CSV compatible Jira/Xray (Aymen, Nicolas, Moez)
- [x] Import Jira testé + fichier de config sauvegardé
- [x] Export Gherkin / BDD (Aymen, Lyne)
- [ ] Historique / sauvegarde des générations (Lyne)
- [ ] Génération de tests d'acceptance / TA (Moez)
- [ ] Matrice de test (Tasnim)
- [ ] Analyse d'app par URL/APK (Kalidou) — vision long terme
- [ ] Gestion des restrictions géographiques API (Diawando)

---

## Phase 2 — Jours 30 à 60 : Validation marché
*(à compléter quand Phase 1 terminée)*

## Phase 3 — Jours 60 à 90 : Produit
*(à compléter quand Phase 2 terminée)*
