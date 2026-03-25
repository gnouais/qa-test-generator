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

### Jours 10-11 (24-25/03) — ✅ FAIT
- [x] ~30 personnes contactées avec le lien de l'app
- [x] Retours exploitables : Anass (valide "[À DÉFINIR PAR LE TESTEUR]"), Sim (mode collaboratif), Karima (cas passants OK, non-passants à creuser), Sidi (langue FR/EN, bouton micro), Rida (mode guidé + export validés), Najat (lien Gherkin/auto), Ngoné (mode guidé validé), Sara Bencheikh (compare avec Gemini/Copilot, préfère l'outil)
- [x] Sara Bencheikh : "Vraiment rien à dire j'adore", compare favorablement avec Gemini et Copilot
- [x] Ken Defossez : a présenté l'outil à son responsable client chez Amadeus, veut intégrer Jira/Octane → 1er signal d'adoption enterprise
- [x] Karima : RDV visio proposé pour démo (créneaux vendredi 28/03 ou lundi 30/03)
- [x] Anass : valide la logique "[À DÉFINIR PAR LE TESTEUR]", confirme le potentiel malgré le front prototype
- [x] Bug langue confirmé par 2 testeurs (Lyne + Sidi) : US en anglais → tests en français
- [x] Ajustement prompts app.py : section fonctionnelle ~70% / edge cases ~30%
- [x] Réponse LinkedIn rédigée pour Julien Mer (structuration données en amont du LLM)

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
- Le mélange FR/EN dans le Gherkin perturbe certains testeurs (retour Lyne, Sidi)
- La comparaison directe avec Gemini/Copilot est favorable (Sara Bencheikh)
- Le taux de conversion contact → test réel est ~25-30% — normal pour du LinkedIn
- Les "je vais tester" sans relance à 48h ne convertissent presque jamais

### En attente
- [x] ~~Fixer bug bouton démo (Romain)~~ — FAIT et validé
- [ ] Retour de Karima après visio démo (créneaux proposés : 28/03 ou 30/03)
- [ ] Retour de Luis sur le mode guidé
- [ ] Retour de Diawando avec VPN
- [ ] Retour d'Elodie — relancer début avril
- [ ] Relancer les "je vais tester" à 48h : Marie-Eve, Ngoné, Andriamaroson Fabius, Oumar Sidibe, Racchana
- [ ] Contacter Aissata pour creuser son cas d'usage
- [ ] Publier post LinkedIn #3 (hallucinations IA)
- [ ] Publier newsletter #2
- [ ] Avancer sur le lead Ken Defossez (Amadeus/Jira/Octane)

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
- **Action** : ✅ Bug fixé et validé (Jour 11)

### Testeur 4 — Diawando DIAWARA
- **Retour :** Restriction géo API Gemini. En attente VPN.

### Testeur 5 — Ken Defossez
- **Retour :** Bug PixelConnect corrigé. Signal B2B : "on nous demande des initiatives AI"
- **Retour Jour 10-11 :** A présenté l'outil à son responsable client chez Amadeus. Veut intégrer Jira/Octane. Intéressé par la formation. → **1ER LEAD ENTERPRISE. PRIORITÉ.**

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
- **Retour Jour 10-11 :** Cas passants OK, moins convaincant sur les non-passants. Intéressée par l'analyse de qualité/complétude des US. RDV visio proposé (28/03 ou 30/03). Sera à ParisTestConf mardi 01/04.
- **Action** : Lead enterprise Bforbank. RDV visio à confirmer.

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

### Testeur 18 — Anass Aouissi
- **Date** : 24-25/03/2026
- **Retour :**
  - Suggestions front-end et design UX
  - Demande de masquer le prompt système visible
  - Valide la logique "[À DÉFINIR PAR LE TESTEUR]" comme approche pertinente
  - "Le potentiel de l'outil est déjà très prometteur même à ce stade de prototype"
- **Action** : Retour exploitable. Améliorations front prévues Phase 2 (migration Next.js).

### Testeur 19 — Sim Bienvenue Houl-boumi
- **Date** : 24/03/2026
- **Retour :** "Très intéressant pour organiser le travail d'équipe. Tu peux ajouter un mode collaboratif"
- **Action** : Mode collaboratif → backlog Phase 2.

### Testeur 20 — Sidi (nom complet à confirmer)
- **Date** : 24/03/2026
- **Retour :**
  - Outil très utile pour gagner du temps
  - Bug langue : US en anglais → tests générés en français (confirme le signal de Lyne)
  - Suggestion : bouton micro / voice-to-text
  - Suggestion : pré-remplir les réponses du mode guidé
- **Action** : ✅ Bug langue fixé (détection dans les 4 prompts). Bouton micro et pré-remplissage → backlog.

### Testeur 21 — Rida Belaqziz
- **Date** : 24/03/2026
- **Retour :** Très positif, valide le mode guidé et les formats d'export. Suggestion : aperçu éditable avant export.
- **Action** : Aperçu éditable → backlog Phase 2.

### Testeur 22 — Najat Challou
- **Date** : 24/03/2026
- **Retour :** Positif, souligne le lien Gherkin/automatisation. Demande si formations automatisation disponibles.
- **Action** : Lead formation potentiel.

### Testeur 23 — Ngoné SENE MANE
- **Date** : 24-25/03/2026
- **Retour :** Positif, valide le mode guidé. Utilise déjà Claude pour Gherkin sur Zephyr/Jira.
- **Action** : Profil intéressant — utilisatrice d'IA concurrente, peut comparer.

### Testeur 24 — Sara Bencheikh
- **Date** : 25/03/2026
- **Retour :**
  - "Vraiment rien à dire j'adore"
  - Compare directement avec Gemini et Copilot : "on a aussi des résultats mais là c'est top"
  - Valide la possibilité de télécharger les résultats et la génération des cas de tests
- **Action** : **MEILLEUR TÉMOIGNAGE UTILISATEUR.** À solliciter pour quote landing page / newsletter.

### Testeur 25 — Sonia Chehida
- **Date** : 25/03/2026
- **Retour :** "Très intéressant ton partage. J'utilise également l'IA pour la rédaction de mes cas de test ça va plus vite"
- **Action** : N'a pas testé l'outil, utilise déjà l'IA. À relancer pour tester.

### Testeur 26 — Jean-François Fresi
- **Date** : 25/03/2026
- **Retour :** "C'est top ! Bravo !"
- **Action** : Réaction positive mais pas de feedback actionnable. À relancer pour retour détaillé.

### Testeur 27 — Andriamaroson Fabius
- **Date** : 25/03/2026
- **Retour :** "Un très bon travail. Très curieux d'essayer ça. Je te donnerai un retour sur mon expérience."
- **Action** : Promesse de test. Relancer à 48h si pas de retour.

### Testeur 28 — Oumar Sidibe
- **Date** : 25/03/2026
- **Retour :** "Ok merci je vais check ça"
- **Action** : Promesse de test. Relancer à 48h si pas de retour.

### Testeur 29 — Racchana PHCAR
- **Date** : 25/03/2026
- **Retour :** En formation Playwright/Postman. "Yes je m'en doutais ! 🔥" (après précision que l'outil ne nécessite pas d'être technique)
- **Action** : Intéressée mais pas dispo immédiatement. Relancer dans 1 semaine.

### Testeur 30 — Marie-Eve Lafrance
- **Date** : 25/03/2026
- **Retour :** "Je vais aller regarder cela. Merci ! 😊"
- **Action** : Promesse de test. Relancer à 48h si pas de retour.

### Testeur 31 — Bineta SALL
- **Date** : 24/03/2026
- **Retour :** "Cet outil m'intéresse beaucoup, je me suis abonnée à ta newsletter. Je vais le tester très prochainement."
- **Action** : Promesse de test + abonnée newsletter. Relancer à 48h.

---

## Métriques

| Métrique | Objectif Phase 1 | Actuel | Jour |
|----------|-----------------|--------|------|
| Prototype utilisable | ✅ | ✅ | J2 |
| Testeurs confirmés | 10+ | 31 ✅ | J11 |
| Testeurs qui ont testé | 5+ | ~18 ✅ | J11 |
| Retours exploitables | 3+ | ~20 ✅ | J11 |
| Itérations produit | - | 10 | J11 |
| Formats d'export | - | 4 | J4 |
| Modes de génération | - | 2 (Guidé + Direct) | J8 |
| Posts LinkedIn | 3 | 3 | J8 |
| Newsletter publiée | 1 | 1 ✅ | J6 |
| Abonnés newsletter | - | 928 | J6 |
| Vidéo démo | - | ✅ | J8 |
| Mode guidé validé | - | ✅ (Aissata, Jordan, Sara, Rida, Ngoné) | J11 |
| Jours écoulés / 30 | - | 11/30 (37%) | - |
| Utilisateurs actifs | 100-500 | ~35 | J11 |
| Leads enterprise | - | 2 (Ken/Amadeus, Karima/Bforbank) | J11 |
| Taux conversion contact→test | - | ~25-30% | J11 |

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
9. **Mode guidé** : v8 — dialogue interactif (retour Luis) — VALIDÉ par Aissata, Jordan, Sara, Rida, Ngoné
10. **Collaboration Nicolas** : déclinée
11. **Smartesting/Lynqa** : contact décliné
12. **Formation** : mode maintenance
13. **Newsletter** : "Le Testeur Augmenté" — hebdomadaire
14. **Migration Next.js** : prévue Phase 2
15. **Répartition prompts** : ~70% cas fonctionnels / ~30% edge cases (Jour 10)

## Backlog
- [x] Prompt strict (Luis v2)
- [x] Export CSV Jira/Xray
- [x] Export Gherkin / BDD
- [x] Bouton démo pré-rempli
- [x] Optimisation performance
- [x] Vidéo démo
- [x] Mode guidé — dialogue interactif (Luis v4-v5)
- [x] Ajustement répartition prompts 70/30 (Jour 10)
- [x] Bug bouton démo — ne se réactive pas après effacement (Romain) — FIXÉ et validé (Jour 11)
- [x] Détection de langue — générer dans la langue de la US (Lyne, Sidi) — FIXÉ, règle dans les 4 prompts (Jour 11)
- [x] Cohérence langue FR/EN dans le Gherkin (Lyne) — couvert par le fix détection de langue
- [x] Masquer le prompt système visible côté front (Anass) — FIXÉ, instruction "NEVER introduce yourself" + troncature code (Jour 11)
- [ ] Aperçu éditable avant export (Rida)
- [ ] Mode collaboratif (Sim)
- [ ] Pré-remplissage réponses mode guidé (Sidi)
- [ ] Historique / sauvegarde des générations (Lyne)
- [ ] Génération de tests d'acceptance / TA (Moez)
- [ ] Matrice de test (Tasnim)
- [ ] Sessions "tres amigos" (Jean-Yves) — à explorer
- [ ] Analyse d'app par URL/APK (Kalidou) — vision long terme
- [ ] Bouton micro / voice-to-text (Sidi) — gadget, pas prioritaire
- [ ] Gestion restrictions géo API (Diawando)
- [ ] Migration Next.js + responsive mobile (Phase 2)

---

## Phase 2 — Jours 31 à 60 : Validation marché (15/04 → 14/05/2026)
*(à compléter quand Phase 1 terminée)*

## Phase 3 — Jours 61 à 90 : Produit (15/05 → 13/06/2026)
*(à compléter quand Phase 2 terminée)*
