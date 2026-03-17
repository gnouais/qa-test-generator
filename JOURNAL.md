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

### Leçons apprises
- La friction tue l'adoption : Ollama + API tokens + install = personne ne teste
- Zéro installation = condition non négociable
- "Pas eu le temps" = "trop compliqué pour que je fasse l'effort"
- Le contexte applicatif change tout : sans contexte, les cas de test sont génériques et inexécutables (retour Luis)
- Les retours terrain sont plus utiles que la réflexion solo — itérer en < 24h crée de la confiance
- Bug Diawando = restriction géo API Gemini (Guinée-Conakry), pas un bug de code

### En attente
- [ ] Retour de Luis sur la v2 (contexte applicatif)
- [ ] Relancer les 4 testeurs restants (dans 48h)
- [ ] Retour de Diawando avec VPN

---

## Retours testeurs

### Testeur 1 — Luis Cavalheiro
- **A testé ?** : Oui (v1)
- **Date** : 16/03/2026
- **Retour :**

> Je sais que c'est un prototype mais je vois 2 grandes limitations :
> 1. Comment passer le contexte de la User Story
> 2. Comment generer les données de test
> Pour les quelques cas que j'ai essayé, je ne vois pas un user delta etre capable d'executer les cas de tests sans une bonne connaissance de l'application. Pour moi, un bon cas de test doit contenir suffisamment d'information que "mr tout le monde" peut l'executer sans poser de question...

- **Action prise** : Ajout champ contexte applicatif + prompt amélioré (v2). Message envoyé pour retester.

- **A testé ?** : Oui (v2)
- **Date** : 17/03/2026
- **Retour :**
  
> Salut Amadou,
> C'est beaucoup mieux.
> Maintenant d'un point de vue pratique l'appli devrait demander au user de spécifier les données quand celles ci ne sont pas définies au lieu des générer des fausses données



### Testeur 2 — Moez Ben Khaled
- **A testé ?** : Oui (v1)
- **Date** : 16/03/2026
- **Retour :**

> J'ai testé l'outil cet aprem et c'est vraiment top.
> Juste une question : Des fois les PO rédigent mal les tests d'acceptation et c'est très important pour la synchro Squash/Jira et l'automatisation par exemple, y a t'il un moyen d'évoluer l'outil pour la création des TA avec les cas de test stp?

- **Action prise** : Noté pour Phase 2 — génération de tests d'acceptance (TA).

### Testeur 3 — Romain De Page
- **A testé ?** : Oui (v1)
- **Date** : 16/03/2026
- **Retour :**

> J'ai testé ton outil il est vraiment bien. Tu l'as fait avec quoi?
> Oui niquel j'ai bien eu les case de tests et je les ai même exportés en .txt pour voir c'est vraiment bien

- **Action prise** : Aucune — retour positif, export fonctionne.

### Testeur 4 — Diawando DIAWARA
- **A testé ?** : Partiellement
- **Date** : 16/03/2026
- **Retour :**

> Je constate que les cas de tests ne sont pas générés après soumission de la user story.
> Je vais activer mon vpn et reprendre.

- **Action prise** : Restriction géographique API Gemini (Guinée-Conakry). En attente retour avec VPN.


### Testeur 5 — Ken Defossez
- **A testé ?** : OUI
- **Date** : 17/03/2026
- **Retour :**

> Hello Amadou merci pour le partage. Je n'ai pas encire testé la team d'agents CrewAI, c'est sur ma todo.
>Je viens de tester ton outil QA version web, congratz ! Je dois justement travailler sur quelque chose de similaire chez mon client, ca m'intéresse de savoir qu'est-ce qu'il y a sous le capot 🙂
>Petit retour après mon premier test de l'outil, il m'a parlé de PixelConnect sans que j'y fasse référence 🤪 Mais sinon la disjonction des cas de test et risques pour ma US est top ! 👍

>Mes inputs 

> * US: En tant qu’utilisateur,
> je veux pouvoir me connecter à mon compte avec mon identifiant et mon mot de passe,
> afin d’accéder à mon profil, mes messages et mon fil d’actualité.

> *Contexte applicatif : L’application est une plateforme mobile et web de partage de photos et de vidéos permettant aux utilisateurs de publier du contenu, d’interagir avec d’autres > utilisateurs et de consulter un fil d’actualité personnalisé.
> Pour accéder aux fonctionnalités personnalisées (profil, publications, messages privés, notifications, etc.), l’utilisateur doit posséder un compte et s’authentifier via un écran de > connexion.

- **Action prise** : N/A


### Testeur 6 — AYMEN ISMAIL
- **A testé ?** : OUI
- **Date** : 17/03/2026
- **Retour :**

> Salut Amadou, 
> je te remercie pour ton partage!
> je viens de tester ton outil QA et franchement chapeau ;)
> Ton appli fonctionne parfaitement et j'ai pu transformer les cas de test générés en format csv pour les intégrer directement dans JIRA/XRAY.
> Ca pourra être une idée pour évoluer ton appli en ajoutant d'autres façons d'exporter les cas de test : en langage gherkin ou manuel sous forme de steps, sous fichier csv directement exploitable dans JIRA/WRAY ;)
> Cordialement
> Aymen

- **Action prise** : N/A

### Testeur 8 — Tasnim Ferchichi
- **A testé ?** : OUI
- **Date** : 17/03/2026
- **Retour :**

> hello Amadou !
> je viens de faire un premier test
> comme préciser sur le site il faut bien entendu donner des infos concernant le contexte sinon ça a l'air assez cohérent !

> Pour vérifier les premiers tests, peut etre qu'il serait bien de faire une matrice de test
> et avec les résultats de streamlit, cocher/vérifier si effectivement ça match bien, si ça complete avec d'autre cas etc...

> en tout cas c'est bien sympa d'avoir de plus en plus d'outils ! plein de choses à tester 🦾

- **Action prise** : N/A


### Testeur 9 — Kalidou BA
- **A testé ?** : OUI
- **Date** : 17/03/2026
- **Retour :**

> Bonjour Amadou,
> c'est vraiment un super APP et il va beaucoup nous aider avec les cas de tests. 
> est-ce possible de linker soit l'APK ou le lien web et dès qu'on clique sur les fonctionnalités l'application génére les cas de tests Principal et alternatif
> Comme par exemple quand on est saisit une requete SQL et le résultat s'affiche

- **Action prise** : N/A

### Testeur 10 — Nicolas TRZCINSKI  
- **A testé ?** : OUI
- **Date** : 17/03/2026
- **Retour :**

> Hello @Amadou FOFANA,
> Intéressant ton appli ! Je travaille également sur un projet web du même genre, connecté à Jira/Xray. C’est encore en développement, mais ça avance bien pour l'instant c'est
> uniquement en local. Je dois le présenter à mes responsables début avril.
> Tu utilises un LLM en local ou une API Claude / OpenAI etc ?
> Pour l'instant je suis sur de l'API Anthropic.
> Hâte de voir comme tu avances, je te tiendrai au courant de mes avancées également, qui sait on pourrait collaborer dans le futur sur un même projet 😉

https://www.linkedin.com/dms/prv/image/v2/D4E06AQFoMyL_ij3-xg/messaging-image-720/B4EZz7xVs_HgAY-/0/1773750542006?m=AQKokwmhY7Zy5gAAAZz8Gu9sxbrfY3YhcZKqM-TyCh1DlKeiCWKKaoddcA&ne=1&v=beta&t=um5ya5Q7O2a5Copbj568VsN0zbvHYsMAUfuveGXJbao<img width="757" height="852" alt="image" src="https://github.com/user-attachments/assets/b5bd2cd2-51bb-4e22-81a1-3ac507cc0e34" />


> pour la petite histoire ça fait à peu près 1 an et demi que je travaille sur des scripts python de génération de test etc puis un jour je me suis dit mais pourquoi pas créer le couteau suisse QA avec une vraie interface et pas quelque chose uniquement exécutable dans un terminal et uniquement dédié aux plus geeks d'entre nous 😁


- **Action prise** : N/A




### Testeur 11 — Lyne VOCTABAH
- **A testé ?** : OUI
- **Date** : 17/03/2026
- **Retour :**

> Est-ce que le lien sauvegarde les user stories ?
> En tout cas, je trouve que l’outil fait vraiment gagner du temps sur la rédaction 🙌👏
> Les cas de test sont bien détaillés et faciles à comprendre.
> J’aime aussi le fait que ce soit hyper simple : tu colles directement ta user story, sans formulaire à remplir, sans création de compte ni vérification type captcha.
- **Action prise** : N/A
  

- 
### Testeurs X (à venir)
- **A testé ?** : Non
- **Relance prévue** : 18/03/2026

---

## Métriques

| Métrique | Objectif Phase 1 | Actuel |
|----------|-----------------|--------|
| Prototype utilisable | ✅ | ✅ |
| Testeurs contactés | 10+ | 11 |
| Testeurs qui ont testé | 5+ |11 |
| Retours exploitables | 3+ | 10 ✅ |
| Itérations basées sur feedback | - | 1 (v2 contexte) |

---

## Décisions prises
1. **Stack** : Streamlit + Gemini 2.5 Flash (pas Ollama)
2. **Architecture** : 1 seul appel LLM (pas 3 agents)
3. **Go-to-market** : Option A — PLG, self-service, 19-49€/mois
4. **Priorité** : Retours terrain AVANT nouvelles features
5. **Champ contexte applicatif** : ajouté suite retour Luis — améliore drastiquement la qualité des tests générés
6. **Tests d'acceptance (TA)** : demandé par Moez — reporté à Phase 2

## Backlog (demandé par les testeurs, pas encore planifié)
- [ ] Génération de tests d'acceptance / TA (Moez)
- [ ] Gestion des restrictions géographiques API (Diawando)

---

## Phase 2 — Jours 30 à 60 : Validation marché
*(à compléter quand Phase 1 terminée)*

## Phase 3 — Jours 60 à 90 : Produit
*(à compléter quand Phase 2 terminée)*
