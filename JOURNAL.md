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
- [x] Export CSV compatible Jira/Xray ajouté (colonnes : Test Case ID, Résumé, Description, Preconditions, Test Steps, Expected Result, Priorité)
- [x] Fix boutons d'export : persistent après téléchargement (session_state)
- [x] Luis a retesté la v2 — validé, nouvelle suggestion sur les données

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

### En attente
- [ ] Tester l'import du CSV dans Jira
- [ ] Nouveaux retours via le post LinkedIn
- [ ] Retour de Diawando avec VPN

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
- **Date** : 17/03/2026
- **Retour :**

> Je viens de tester ton outil QA version web, congratz ! Je dois justement travailler sur quelque chose de similaire chez mon client, ca m'intéresse de savoir qu'est-ce qu'il y a sous le capot.
> Petit retour après mon premier test de l'outil, il m'a parlé de PixelConnect sans que j'y fasse référence. Mais sinon la disjonction des cas de test et risques pour ma US est top !

- **Action prise** : Bug PixelConnect = le LLM inventait un nom d'app. Corrigé dans le prompt v3.

### Testeur 6 — Aymen Ismail
- **A testé ?** : Oui
- **Date** : 17/03/2026
- **Retour :**

> Ton appli fonctionne parfaitement et j'ai pu transformer les cas de test générés en format csv pour les intégrer directement dans JIRA/XRAY.
> Ca pourra être une idée pour évoluer ton appli en ajoutant d'autres façons d'exporter les cas de test : en langage gherkin ou manuel sous forme de steps, sous fichier csv directement exploitable dans JIRA/XRAY.

- **Action prise** : Export CSV Jira/Xray ajouté. Export Gherkin noté au backlog.

### Testeur 7 — Tasnim Ferchichi
- **A testé ?** : Oui
- **Date** : 17/03/2026
- **Retour :**

> Comme précisé sur le site il faut bien entendu donner des infos concernant le contexte sinon ça a l'air assez cohérent !
> Pour vérifier les premiers tests, peut être qu'il serait bien de faire une matrice de test et avec les résultats de streamlit, cocher/vérifier si effectivement ça match bien.

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

> Intéressant ton appli ! Je travaille également sur un projet web du même genre, connecté à Jira/Xray. Tu utilises un LLM en local ou une API Claude / OpenAI etc ?
> Hâte de voir comme tu avances, qui sait on pourrait collaborer dans le futur sur un même projet.

- **Action prise** : Collaboration déclinée pour l'instant. Reste solo.

### Testeur 10 — Lyne Voctabah
- **A testé ?** : Oui
- **Date** : 17/03/2026
- **Retour :**

> Est-ce que le lien sauvegarde les user stories ?
> En tout cas, je trouve que l'outil fait vraiment gagner du temps sur la rédaction.
> Les cas de test sont bien détaillés et faciles à comprendre.
> J'aime aussi le fait que ce soit hyper simple : tu colles directement ta user story, sans formulaire à remplir, sans création de compte ni vérification type captcha.

- **Action prise** : Historique/sauvegarde noté au backlog.

---

## Métriques

| Métrique | Objectif Phase 1 | Actuel |
|----------|-----------------|--------|
| Prototype utilisable | ✅ | ✅ |
| Testeurs contactés | 10+ | 11+ ✅ |
| Testeurs qui ont testé | 5+ | 10 ✅ |
| Retours exploitables | 3+ | 10 ✅ |
| Itérations basées sur feedback | - | 3 (v2 contexte, v3 prompt, v4 CSV) |
| Post LinkedIn publié | 1 | 1 ✅ |

---

## Décisions prises
1. **Stack** : Streamlit + Gemini 2.5 Flash (pas Ollama)
2. **Architecture** : 1 seul appel LLM (pas 3 agents) + 1 appel pour conversion CSV
3. **Go-to-market** : Option A — PLG, self-service, 19-49€/mois
4. **Priorité** : Retours terrain AVANT nouvelles features
5. **Champ contexte applicatif** : ajouté suite retour Luis — améliore drastiquement la qualité des tests générés
6. **Prompt strict** : ne jamais inventer de données — [À DÉFINIR PAR LE TESTEUR] quand pas de contexte
7. **Export CSV Jira/Xray** : ajouté suite retours Aymen, Nicolas, Moez
8. **Collaboration Nicolas** : déclinée pour l'instant, reste solo
9. **Repo GitHub public** : nécessaire pour Streamlit Cloud gratuit, code non sensible

## Backlog (demandé par les testeurs, pas encore planifié)
- [x] Corriger le prompt — ne pas inventer de données (Luis v2)
- [x] Export CSV compatible Jira/Xray (Aymen, Nicolas, Moez)
- [ ] Export Gherkin / BDD (Aymen)
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
