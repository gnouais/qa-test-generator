# 🧪 QA Test Generator — Journal de bord (Plan 90 jours)

---

## Infos projet
- **Début du plan** : 15/03/2026
- **Objectif 90 jours** : 100-500 utilisateurs réels + retours terrain exploitables
- **URL app** : https://app-test-generator.streamlit.app
- **Repo** : https://github.com/TesteurGenAI/qa-test-generator

---

## Phase 1 — Jours 1 à 30 : Prototype

### Jour 1 — ✅ FAIT
- [x] Prompt QA qui génère cas de test, edge cases, risques
- [x] App Streamlit déployée sur Streamlit Cloud
- [x] API Gemini 2.5 Flash connectée (secret Streamlit)
- [x] Lien envoyé à 8 testeurs
- [x] Retours projet précédent : 8/8 n'avaient pas testé (trop de friction)

### Leçons apprises
- La friction tue l'adoption : Ollama + API tokens + install = personne ne teste
- Zéro installation = condition non négociable
- "Pas eu le temps" = "trop compliqué pour que je fasse l'effort"

### En attente
- [ ] Retours des 8 testeurs (relancer dans 48h si pas de réponse)
- [ ] Analyser les retours et décider des prochaines actions

---

## Retours testeurs

### Testeur 1 — Luis Cavalheiro
- **A testé ?** : Oui
- **Date** : [16/03/2026]
- **Retour :**

> Bonjour,
> Je sais que c'est un prototype mais je vois 2 grandes limitations, à moins que ce soit moi qui n'ait pas vu les options:
> 1. Comment passer le contexte de la User Story
> 2. Comment generer les données de test
> Pour les quelques cas que j'ai essayé, je ne vois pas un user delta etre capable d'executer les cas de tests sans une bonne connaissance de l'application. Pour moi, un bon cas de test doit contenir suffisamment d'information que "mr tout le monde" peut l'executer sans poser de question...
> Je pense comme toi que dans le futur la generation IA va remplacer le MBT mais les algos ne sont pas encore assez puissant.

### Testeur 2 - Moez Ben Khaled
- **A testé ?** : Oui
- **Date** : [16/03/2026]
- **Retour :**

> Hello,
> J'ai testé l'outil cet aprem et c'est vraiment top.
> Juste une question et par expérience : Des fois les PO rédigent mal les tests d'acceptation et c'est très important pour la synchro Squash/Jira et l'automatisation par exemple, y a t'il un moyen > d'évoluer l'outil pour la création des TA avec les cas de test stp?
> Merci pour ta confiance mon frère.

### Testeur 3 - Romain De Page
- **A testé ?** : Oui
- **Date** : [16/03/2026]
- **Retour :**

> J’ai testé ton outil il est vraiment bien. Tu l’as fait avec quoi?
> Oui niquel j’ai bien eu les case de tests et je les ai même exportés en .txt pour voir c’est vraiment bien 


### Testeur 4 - Diawando DIAWARA  
- **A testé ?** : Oui
- **Date** : [16/03/2026]
- **Retour :**

> Je constate que les cas de tests ne sont pas générés après soumission de la user storie
> Vous devez avoir reçu le mail. Voici le lien vers le fichier : https://we.tl/t-UVoZ1l86JP
> Je vais activer mon vpn et reprendre. Je précise qu’avec la user story en exemple ça marche bien


## Métriques

| Métrique | Objectif Phase 1 | Actuel |
|----------|-----------------|--------|
| Prototype utilisable | ✅ | ✅ |
| Testeurs contactés | 10+ | 8 |
| Testeurs qui ont testé | 5+ | 4 |
| Retours exploitables | 3+ | 3 |

---

## Décisions prises
1. **Stack** : Streamlit + Gemini 2.5 Flash (pas Ollama)
2. **Architecture** : 1 seul appel LLM (pas 3 agents)
3. **Go-to-market** : Option A — PLG, self-service, 19-49€/mois
4. **Priorité** : Retours terrain AVANT nouvelles features

---

## Phase 2 — Jours 30 à 60 : Validation marché
*(à compléter quand Phase 1 terminée)*

## Phase 3 — Jours 60 à 90 : Produit
*(à compléter quand Phase 2 terminée)*
