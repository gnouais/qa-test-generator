# 🧪 QA Test Generator — Journal de bord (Plan 90 jours)

---

## Infos projet
- **Début du plan** : 15/03/2026
- **Objectif 90 jours** : 100-500 utilisateurs réels + retours terrain exploitables
- **Fin Phase 1** : 14/04/2026 (Jour 30)
- **URL app** : https://app-test-generator.streamlit.app
- **Repo** : https://github.com/TesteurGenAI/qa-test-generator

---

## Phase 1 — Jours 1 à 30 : Prototype (15/03 → 14/04/2026)

### Jours 1-2 (15-16/03) — ✅ FAIT
- [x] Prototype déployé sur Streamlit Cloud
- [x] API Gemini 2.5 Flash + clé masquée
- [x] 4 testeurs v1 + itération v2 (contexte applicatif)

### Jour 3 (17/03) — ✅ FAIT
- [x] 11 testeurs, post LinkedIn carrousel (2407 impressions)
- [x] Export CSV Jira/Xray + import validé
- [x] Prompt strict (plus de données inventées)

### Jour 4 (18/03) — ✅ FAIT
- [x] Export Gherkin/BDD + 4 formats d'export
- [x] 9 leads LinkedIn contactés en DM

### Jours 5-6 (19-20/03) — ✅ FAIT
- [x] Newsletter #1 → 928 abonnés en 24h
- [x] Mode guidé conceptualisé (retour Luis v4-v5)
- [x] Performance optimisée (CSV/Gherkin à la demande)
- [x] Design épuré (icônes SVG émeraude)

### Jours 7-8 (21-23/03) — ✅ FAIT
- [x] Vidéo démo publiée sur LinkedIn
- [x] MODE GUIDÉ LIVRÉ — dialogue interactif IA/testeur
- [x] Post LinkedIn #2 vidéo publié
- [x] Post #3 (hallucinations) + Newsletter #2 rédigés
- [x] Smartesting/Lynqa a contacté — décliné
- [x] Testeur 13 (Rezika) : "similaire à Copilot mais bien d'avoir un outil spécialisé"

### Jour 9 (23/03) — ✅ FAIT
- [x] 6 nouveaux retours en une journée
- [x] Mode guidé validé par Aissata et Jordan
- [x] Aissata : cas d'usage réel — 600 tests manuels, 197 US à venir, sous-staffée
- [x] Jordan : "bluffant", "nouveau mode très complet"
- [x] Said Amouri : "très utile, outil d'accélération"
- [x] Jean-Yves Garcin : "vraiment top", veut tester malgré filtre anti-IA
- [x] Karima teste aujourd'hui depuis son PC pro (Bforbank)
- [x] Romain : bug bouton démo identifié
- [x] Lyne : retours UX — navigation, responsive mobile, cohérence langue FR/EN

### Leçons apprises
- La friction tue l'adoption
- Le contexte applicatif change tout (retour Luis)
- Les retours terrain > la réflexion solo
- L'export CSV Jira est la feature la plus demandée
- Les LLM inventent des données si on ne l'interdit pas
- 928 abonnés newsletter en 24h — demande forte
- Engagement LinkedIn ≠ utilisation réelle
- Le mode guidé est le vrai différenciateur vs Copilot/ChatGPT (validé par Aissata, Jordan)
- Aissata = cas d'usage parfait pour le pitch (600 tests manuels, sous-staffée)
- Les proxys entreprise peuvent bloquer l'accès (Karima, Jean-Yves)
- Streamlit n'est pas responsive mobile (retour Lyne)
- Le mélange FR/EN dans le Gherkin perturbe certains testeurs (retour Lyne)

### En attente
- [ ] Fixer bug bouton démo (Romain)
- [ ] Répondre aux testeurs (Lyne, Jordan, Aissata, Said, Jean-Yves, Karima)
- [ ] Contacter Aissata pour creuser son cas d'usage
- [ ] Publier post LinkedIn #3 (hallucinations IA)
- [ ] Publier newsletter #2
- [ ] Retour de Luis sur le mode guidé
- [ ] Retour de Karima après test PC pro
- [ ] Retour de Diawando avec VPN
- [ ] Retour d'Elodie — relancer début avril

---

## Retours testeurs

### Testeur 1 — Luis Cavalheiro
- **Retour v1 :** Manque de contexte
- **Retour v2 :** L'IA invente des données
- **Retour v4-v5 :** [À DÉFINIR PAR LE TESTEUR] improductif → demande dialogue interactif
- **Actions** : Mode guidé livré (Jour 8). En attente retour.

### Testeur 2 — Moez Ben Khaled
- **Retour :** "top", demande TA → backlog

### Testeur 3 — Romain De Page
- **Retour v1 :** "vraiment bien", export .txt fonctionne
- **Retour Jour 9 :** Bug — si on efface la démo pré-remplie, le bouton ne fonctionne plus sans rafraîchir
- **Action** : Bug à fixer

### Testeur 4 — Diawando DIAWARA
- **Retour :** Restriction géo API Gemini. En attente VPN.

### Testeur 5 — Ken Defossez
- **Retour :** Bug PixelConnect corrigé. Signal B2B : "on nous demande des initiatives AI"

### Testeur 6 — Aymen Ismail
- **Retour :** Demande CSV Jira et Gherkin → les deux livrés

### Testeur 7 — Tasnim Ferchichi
- **Retour :** "cohérent avec contexte", demande matrice de test → backlog

### Testeur 8 — Kalidou BA
- **Retour :** "super APP", demande analyse par URL/APK → vision long terme

### Testeur 9 — Nicolas Trzcinski
- **Retour :** Projet similaire, propose collaboration → déclinée

### Testeur 10 — Lyne Voctabah
- **Retour Jour 9 :**
  - Navigation : pas de retour page d'accueil depuis les résultats
  - Responsive : ne fonctionne pas sur mobile (faut coulisser)
  - Langue : mélange FR/EN dans le Gherkin, demande cohérence
  - Structure claire, code lisible
- **Action** : Navigation et responsive = limitations Streamlit. Cohérence langue → backlog.

### Testeur 11 — Elodie Juino
- **Retour :** "après notre recette" → relancer début avril

### Testeur 12 — Karima SORIANO
- **Retour Jour 9 :** "Je l'ai envoyé vers ma boîte pro pour l'essayer aujourd'hui. Nos US ne sont pas simples, il y a du back et du front (mobile) donc beaucoup d'écrans Figma."
- **Action** : En attente retour test PC pro. Lead enterprise Bforbank.

### Testeur 13 — Rezika D
- **Retour :** "ça marche très bien, similaire à Copilot mais bien d'avoir un outil spécialisé"

### Testeur 14 — Jordan SORVAS
- **Date** : 23/03/2026
- **Retour :**
  - "C'est super complet comme outil"
  - "Les edge cases, la génération en Markdown ou CSV, Excel"
  - "Franchement c'est bluffant"
  - "Et le nouveau mode est très complet"
  - "Un très grand bravo"
- **Action** : Mode guidé validé.

### Testeur 15 — Aissata SISSOKO PIOCT
- **Date** : 23/03/2026
- **Retour :**
  - "c'est top, j'apprécie le mode guidé où l'IA pose des questions"
  - "les cas de tests proposés sont cohérents avec ceux que j'avais rédigé même sur les cas limites"
  - "je travaille sur un logiciel complexe de comptabilité notariale, sous-staffée, seule là où il faut 2 personnes"
  - "J'ai rédigé 600 tests manuellement sur 85 US. Sur le lot 3 (197 US) je pourrai peut-être m'aider de l'IA"
  - Intéressée aussi par la formation
- **Action** : CAS D'USAGE CLÉ. Contacter pour creuser. Lead formation.

### Testeur 16 — Said Amouri
- **Date** : 23/03/2026
- **Retour :** "j'ai vu la démo bravo. Très utile. Outil d'accélération c'est sûr. Je vais essayer avec un contexte client"
- **Action** : En attente retour avec contexte client.

### Testeur 17 — Jean-Yves Garcin
- **Date** : 23/03/2026
- **Retour :**
  - "l'outil semble vraiment top"
  - "Je vais voir si notre filtre anti AI me permet de l'utiliser"
  - "À voir pour générer des sessions tres amigos"
- **Action** : En attente. Signal intéressant sur les "tres amigos" (collaboration PO/dev/QA).

---

## Métriques

| Métrique | Objectif Phase 1 | Actuel | Jour |
|----------|-----------------|--------|------|
| Prototype utilisable | ✅ | ✅ | J2 |
| Testeurs confirmés | 10+ | 17 ✅ | J9 |
| Testeurs qui ont testé | 5+ | 15 ✅ | J9 |
| Retours exploitables | 3+ | 16 ✅ | J9 |
| Itérations produit | - | 8 | J8 |
| Formats d'export | - | 4 | J4 |
| Modes de génération | - | 2 (Guidé + Direct) | J8 |
| Posts LinkedIn | 3 | 3 | J8 |
| Newsletter publiée | 1 | 1 ✅ | J6 |
| Abonnés newsletter | - | 928 | J6 |
| Vidéo démo | - | ✅ | J8 |
| Mode guidé validé | - | ✅ (Aissata, Jordan) | J9 |
| Jours écoulés / 30 | - | 9/30 (30%) | - |
| Utilisateurs actifs | 100-500 | ~25 | J9 |

---

## Décisions prises
1. **Stack** : Streamlit + Gemini 2.5 Flash
2. **Architecture** : 1 appel LLM principal, CSV et Gherkin à la demande
3. **Go-to-market** : PLG, self-service, 19-49€/mois
4. **Priorité** : Retours terrain AVANT nouvelles features
5. **Contexte applicatif** : v2 (retour Luis)
6. **Prompt strict** : v3
7. **Export CSV Jira/Xray** : retours Aymen, Nicolas, Moez
8. **Export Gherkin/BDD** : retours Aymen, Lyne
9. **Mode guidé** : v8 — dialogue interactif (retour Luis) — VALIDÉ par Aissata et Jordan
10. **Collaboration Nicolas** : déclinée
11. **Smartesting/Lynqa** : contact décliné
12. **Formation** : mode maintenance
13. **Newsletter** : "Le Testeur Augmenté" — hebdomadaire
14. **Migration Next.js** : prévue Phase 2

## Backlog
- [x] Prompt strict (Luis v2)
- [x] Export CSV Jira/Xray
- [x] Export Gherkin / BDD
- [x] Bouton démo pré-rempli
- [x] Optimisation performance
- [x] Vidéo démo
- [x] Mode guidé — dialogue interactif (Luis v4-v5)
- [ ] **Bug bouton démo — ne se réactive pas après effacement (Romain)** — À FIXER
- [ ] Cohérence langue FR/EN dans le Gherkin (Lyne)
- [ ] Historique / sauvegarde des générations (Lyne)
- [ ] Génération de tests d'acceptance / TA (Moez)
- [ ] Matrice de test (Tasnim)
- [ ] Sessions "tres amigos" (Jean-Yves) — à explorer
- [ ] Analyse d'app par URL/APK (Kalidou) — vision long terme
- [ ] Gestion restrictions géo API (Diawando)
- [ ] Migration Next.js + responsive mobile (Phase 2)

---

## Phase 2 — Jours 31 à 60 : Validation marché (15/04 → 14/05/2026)
*(à compléter quand Phase 1 terminée)*

## Phase 3 — Jours 61 à 90 : Produit (15/05 → 13/06/2026)
*(à compléter quand Phase 2 terminée)*
