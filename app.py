import streamlit as st
import google.generativeai as genai
import json
import time
import csv
import io
import re

# --- SVG Icons (Emerald, 20px, inline) ---
ICON_CHECK = '<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#059669" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 12l2 2 4-4"/><circle cx="12" cy="12" r="10"/></svg>'
ICON_ZAP = '<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#059669" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg>'
ICON_CLIPBOARD = '<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#059669" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"/><rect x="8" y="2" width="8" height="4" rx="1" ry="1"/></svg>'
ICON_DOWNLOAD = '<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#059669" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>'
ICON_SHIELD = '<svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#059669" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>'
ICON_PLAY = '<svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#059669" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="5 3 19 12 5 21 5 3"/></svg>'

# --- Demo Data ---
DEMO_USER_STORY = """En tant qu'utilisateur,
je veux pouvoir réinitialiser mon mot de passe via email,
afin de récupérer l'accès à mon compte."""

DEMO_CONTEXT = """App : MonBanquier.fr
Type : application bancaire web
URL : https://app.monbanquier.fr
Page de connexion : /login
Page mot de passe oublié : /forgot-password
Bouton : "Mot de passe oublié ?" sur la page /login
Bouton : "Envoyer le lien" sur la page /forgot-password
Champs : Email (obligatoire), Nouveau mot de passe, Confirmer le mot de passe
Rôles : Client, Conseiller, Admin
Règles mot de passe : min 8 caractères, 1 majuscule, 1 chiffre, 1 caractère spécial
Email expéditeur : noreply@monbanquier.fr
Durée de validité du lien : 30 minutes
Message de succès : "Un email de réinitialisation vous a été envoyé."
Message d'erreur : "Adresse email non reconnue." """

# --- Page Config ---
st.set_page_config(
    page_title="QA Test Generator",
    page_icon="✓",
    layout="wide"
)

# --- Custom CSS - Emerald Theme ---
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;600;700&family=DM+Sans:wght@400;500;600;700&display=swap');

.stApp { font-family: 'DM Sans', sans-serif; }

.main-header { text-align: center; padding: 2.5rem 0 1.5rem 0; }
.main-header h1 {
    font-family: 'JetBrains Mono', monospace;
    font-size: 2.4rem; font-weight: 700;
    background: linear-gradient(135deg, #059669, #10B981, #34D399);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    margin-bottom: 0.5rem;
}
.main-header .tagline { font-size: 1.15rem; color: #6b7280; margin-top: 0; margin-bottom: 1rem; }
.badge {
    display: inline-block; background: #ecfdf5; color: #059669;
    font-size: 0.7rem; font-weight: 700; padding: 0.3rem 0.9rem;
    border-radius: 999px; border: 1px solid #a7f3d0; margin-bottom: 0.8rem;
    letter-spacing: 1px; text-transform: uppercase;
}
.badge svg { vertical-align: -3px; margin-right: 4px; }
.welcome-stats { display: flex; justify-content: center; gap: 2.5rem; margin-top: 1.2rem; margin-bottom: 0.5rem; }
.stat-item { text-align: center; }
.stat-number { font-family: 'JetBrains Mono', monospace; font-size: 1.5rem; font-weight: 700; color: #059669; }
.stat-label { font-size: 0.78rem; color: #9ca3af; margin-top: 0.15rem; }

.section-title {
    font-family: 'JetBrains Mono', monospace; font-size: 0.95rem;
    font-weight: 600; color: #374151; letter-spacing: 0.3px; margin-bottom: 0.5rem;
}
.section-title svg { vertical-align: -4px; margin-right: 6px; }

section[data-testid="stSidebar"] { background-color: #f0fdf4; }
section[data-testid="stSidebar"] .stMarkdown h3 {
    color: #059669; font-family: 'JetBrains Mono', monospace; font-size: 0.9rem; letter-spacing: 0.3px;
}

.stButton > button[kind="primary"] {
    background: linear-gradient(135deg, #059669, #10B981) !important;
    color: white !important; border: none !important; font-weight: 600 !important;
    padding: 0.6rem 1.5rem !important; border-radius: 8px !important;
    font-size: 1rem !important; transition: all 0.2s ease !important;
}
.stButton > button[kind="primary"]:hover {
    background: linear-gradient(135deg, #047857, #059669) !important;
    transform: translateY(-1px) !important;
    box-shadow: 0 4px 12px rgba(5, 150, 105, 0.3) !important;
}

.stDownloadButton > button {
    border: 1px solid #d1fae5 !important; color: #059669 !important;
    font-weight: 600 !important; border-radius: 8px !important;
    transition: all 0.2s ease !important;
}
.stDownloadButton > button:hover {
    background-color: #ecfdf5 !important; border-color: #059669 !important;
}

.stTextArea textarea {
    border-radius: 8px !important; border: 1px solid #d1d5db !important;
    font-family: 'DM Sans', sans-serif !important;
}
.stTextArea textarea:focus {
    border-color: #10B981 !important;
    box-shadow: 0 0 0 2px rgba(16, 185, 129, 0.15) !important;
}

.footer {
    text-align: center; color: #9ca3af; font-size: 0.8rem;
    padding: 2rem 0 1rem 0; border-top: 1px solid #e5e7eb; margin-top: 3rem;
}
.footer svg { vertical-align: -3px; margin: 0 3px; }
</style>
""", unsafe_allow_html=True)

# --- System Prompt ---
SYSTEM_PROMPT = """Tu es un expert QA senior avec 15 ans d'expérience en test logiciel.

Tu génères des cas de test CONCRETS et EXÉCUTABLES. Un testeur junior qui ne connaît pas l'application doit pouvoir exécuter chaque cas de test sans poser de question.

=== RÈGLE ABSOLUE SUR LES DONNÉES ===

Si un contexte applicatif est fourni :
- Utilise UNIQUEMENT les informations données (noms de pages, boutons, URLs, rôles, règles métier)
- Ne complète pas, n'invente pas, n'extrapole pas au-delà de ce qui est fourni
- Si certaines données manquent malgré le contexte, marque-les [À DÉFINIR PAR LE TESTEUR]

Si AUCUN contexte applicatif n'est fourni :
- N'INVENTE AUCUN contexte. Pas de nom d'application fictif, pas d'URL inventée, pas de nom de bouton supposé, pas de nom de page imaginaire
- N'écris JAMAIS de section "Contexte Applicatif Inventé" ou "Contexte supposé" ou similaire
- Pour CHAQUE donnée non fournie, écris exactement : [À DÉFINIR PAR LE TESTEUR]
- Cela inclut : URLs, noms de boutons, noms de pages, messages d'erreur, emails, mots de passe, identifiants, durées de session, règles de validation

=== FIN RÈGLE ABSOLUE ===

RÈGLES DE RÉDACTION :
- Chaque étape doit être SPÉCIFIQUE et détaillée
- Chaque précondition doit décrire exactement comment atteindre l'état initial

À partir de la User Story (et du contexte applicatif si fourni), génère :

## 1. CAS DE TEST FONCTIONNELS
Pour chaque cas de test, fournis :
- **Titre** : nom court et clair
- **Préconditions** : état initial requis avec les étapes pour y arriver
- **Données de test** : valeurs fournies par le contexte OU [À DÉFINIR PAR LE TESTEUR] si non fournies
- **Étapes** : actions numérotées, spécifiques et détaillées
- **Résultat attendu** : ce qui doit se passer, avec les messages exacts si fournis dans le contexte, sinon [À DÉFINIR PAR LE TESTEUR]
- **Priorité** : Haute / Moyenne / Basse

## 2. CAS LIMITES (EDGE CASES)
Identifie les scénarios aux frontières :
- Valeurs limites (min, max, vide, null)
- Cas d'erreur et comportements inattendus
- Concurrence, timeout, données corrompues
- Pour chaque edge case : titre + données de test + description + résultat attendu

## 3. SUGGESTIONS DE RISQUES
Identifie les risques potentiels :
- Risques fonctionnels
- Risques de performance
- Risques de sécurité
- Risques d'intégration
- Pour chaque risque : titre + description + impact (Critique / Majeur / Mineur) + mitigation suggérée

RÈGLES GÉNÉRALES :
- Sois exhaustif mais pertinent — pas de cas de test inutiles
- Adapte le niveau de détail à la complexité de la User Story
- Utilise un langage clair, compréhensible par un testeur junior
- Réponds en français sauf pour les termes techniques standards
- Structure ta réponse en Markdown clair avec les 3 sections ci-dessus
"""

# --- CSV Conversion Prompt ---
CSV_CONVERSION_PROMPT = """Tu es un assistant qui convertit des cas de test en format JSON strict pour import Jira.

À partir des cas de test fournis, extrais UNIQUEMENT les cas de test fonctionnels et les cas limites (PAS les risques) et retourne un tableau JSON.

Chaque objet du tableau doit avoir exactement ces champs :
- "Test Case ID": identifiant unique (TC-001, TC-002, etc.)
- "Summary": le titre du cas de test
- "Description": description courte du cas de test
- "Preconditions": les préconditions, chaque précondition sur une ligne séparée avec un numéro
- "Test Steps": les étapes, CHAQUE ÉTAPE SUR UNE LIGNE SÉPARÉE avec un numéro
- "Expected Result": les résultats attendus, CHAQUE RÉSULTAT SUR UNE LIGNE SÉPARÉE avec un numéro
- "Priority": "Haute", "Moyenne" ou "Basse" (en français)

RÈGLES STRICTES :
- Retourne UNIQUEMENT le tableau JSON, rien d'autre
- Pas de backticks, pas de commentaires
- Le JSON doit être valide et parsable directement
- Supprime tout formatage Markdown dans les valeurs
"""

# --- Gherkin Conversion Prompt ---
GHERKIN_CONVERSION_PROMPT = """Tu es un expert QA qui convertit des cas de test en scénarios Gherkin (BDD).

À partir des cas de test fournis, génère des scénarios au format Gherkin strict.

FORMAT OBLIGATOIRE :

Feature: [Titre dérivé de la User Story]

  Scenario: [Titre du cas de test]
    Given [précondition 1]
    And [précondition 2]
    When [action utilisateur 1]
    And [action utilisateur 2]
    Then [résultat attendu 1]
    And [résultat attendu 2]

RÈGLES STRICTES :
- Mots-clés Gherkin en ANGLAIS, contenu en FRANÇAIS
- Chaque cas de test fonctionnel ET chaque cas limite devient un Scenario
- NE PAS inclure les risques
- Pour les scénarios avec plusieurs jeux de données, utilise Scenario Outline avec Examples
- Pas de formatage Markdown — du texte brut Gherkin uniquement
"""

# --- Header ---
st.markdown(f"""
<div class="main-header">
    <div class="badge">{ICON_ZAP} Propuls&eacute; par l'IA</div>
    <h1>QA Test Generator</h1>
    <p class="tagline">Transformez vos User Stories en cas de test complets en 30 secondes.</p>
    <div class="welcome-stats">
        <div class="stat-item">
            <div class="stat-number">4</div>
            <div class="stat-label">Formats d'export</div>
        </div>
        <div class="stat-item">
            <div class="stat-number">30s</div>
            <div class="stat-label">Temps de g&eacute;n&eacute;ration</div>
        </div>
        <div class="stat-item">
            <div class="stat-number">0</div>
            <div class="stat-label">Config requise</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# --- API Key (from secrets) ---
api_key = st.secrets.get("GEMINI_API_KEY", "")

with st.sidebar:
    st.markdown("### QA Test Generator")
    st.markdown("---")
    st.markdown("### Guide rapide")
    st.markdown("""
    1. Collez votre User Story
    2. *(Optionnel)* Ajoutez le contexte de votre app
    3. Cliquez sur **Générer**
    4. Exportez en Markdown, TXT, CSV Jira ou Gherkin
    """)

    st.markdown("---")
    st.markdown("### Exemple de User Story")
    st.code("""En tant qu'utilisateur,
je veux pouvoir réinitialiser
mon mot de passe via email,
afin de récupérer l'accès
à mon compte.""", language=None)

    st.markdown("---")
    st.markdown("### Exemple de contexte")
    st.code("""App : MonBanquier.fr
Type : app bancaire web
URL : https://app.monbanquier.fr
Pages : Login, Dashboard, Profil
Rôles : Client, Conseiller, Admin
Techno : React + API REST
Règles mot de passe : 
min 8 caractères, 1 majuscule, 
1 chiffre, 1 caractère spécial""", language=None)

    st.markdown("---")
    st.markdown("### Exports disponibles")
    st.markdown("Markdown · TXT · CSV Jira · Gherkin")

# --- Helper: Convert JSON to CSV ---
def json_to_jira_csv(test_cases_json):
    output = io.StringIO()
    fieldnames = ["Test Case ID", "Résumé", "Description", "Preconditions", "Test Steps", "Expected Result", "Priorité"]
    writer = csv.DictWriter(output, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
    writer.writeheader()
    for tc in test_cases_json:
        def format_steps(val):
            val = val or ""
            val = re.sub(r'(?<!\n)\s*(\d+)\.\s', lambda m: ('\n' + m.group(1) + '. ') if int(m.group(1)) > 1 else (m.group(1) + '. '), val)
            return val.strip()
        def trunc(val, limit=255):
            val = val or ""
            return val[:252] + "..." if len(val) > limit else val
        writer.writerow({
            "Test Case ID": tc.get("Test Case ID", ""),
            "Résumé": trunc(tc.get("Summary", "")),
            "Description": tc.get("Description", ""),
            "Preconditions": trunc(format_steps(tc.get("Preconditions", ""))),
            "Test Steps": trunc(format_steps(tc.get("Test Steps", ""))),
            "Expected Result": trunc(format_steps(tc.get("Expected Result", ""))),
            "Priorité": tc.get("Priority", "Moyenne"),
        })
    return output.getvalue()

# --- Initialize session state for demo ---
if 'demo_us' not in st.session_state:
    st.session_state['demo_us'] = ""
if 'demo_ctx' not in st.session_state:
    st.session_state['demo_ctx'] = ""

# --- Main Inputs ---
st.markdown(f'<p class="section-title">{ICON_CLIPBOARD} Votre User Story</p>', unsafe_allow_html=True)

# Try Example button
col_demo1, col_demo2, col_demo3 = st.columns([1, 1, 1])
with col_demo2:
    if st.button("Voir une démo — pré-remplir avec un exemple", use_container_width=True):
        st.session_state['demo_us'] = DEMO_USER_STORY
        st.session_state['demo_ctx'] = DEMO_CONTEXT

user_story = st.text_area(
    "User Story",
    height=150,
    value=st.session_state.get('demo_us', ''),
    placeholder="En tant que [rôle], je veux [action], afin de [bénéfice]...\n\nVous pouvez aussi coller des critères d'acceptance, des règles métier, ou toute description fonctionnelle.",
    label_visibility="collapsed"
)

with st.expander("Contexte applicatif (optionnel — recommandé pour des tests plus précis)", expanded=bool(st.session_state.get('demo_ctx', ''))):
    app_context = st.text_area(
        "Décrivez votre application",
        height=120,
        value=st.session_state.get('demo_ctx', ''),
        placeholder="Nom de l'app, type (web/mobile), URL, pages principales, rôles utilisateurs, règles métier, stack technique, contraintes spécifiques...\n\nPlus vous donnez de contexte, plus les cas de test seront précis et exécutables.",
        label_visibility="collapsed"
    )

# --- Generate Button ---
col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    generate = st.button("Générer les cas de test", use_container_width=True, type="primary")

# --- Generation Logic ---
if generate:
    # Clear demo state after generation
    st.session_state['demo_us'] = ""
    st.session_state['demo_ctx'] = ""

    if not api_key:
        st.error("Configuration API manquante. Contactez l'administrateur.")
    elif not user_story.strip():
        st.error("Collez une User Story pour commencer.")
    else:
        try:
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel(model_name="gemini-2.5-flash", system_instruction=SYSTEM_PROMPT)

            if app_context and app_context.strip():
                user_message = f"CONTEXTE APPLICATIF :\n{app_context}\n\n---\n\nUSER STORY À ANALYSER :\n{user_story}"
            else:
                user_message = f"AUCUN CONTEXTE APPLICATIF FOURNI. Tu DOIS utiliser [À DÉFINIR PAR LE TESTEUR] pour toute donnée spécifique à l'application. N'invente RIEN.\n\n---\n\nUSER STORY À ANALYSER :\n{user_story}"

            with st.spinner("Analyse et génération des tests..."):
                response = model.generate_content(user_message)
                result = response.text

            st.session_state['result'] = result
            st.session_state['user_story'] = user_story
            st.session_state['app_context'] = app_context if app_context else ""

            with st.spinner("Préparation de l'export CSV Jira..."):
                try:
                    csv_model = genai.GenerativeModel(model_name="gemini-2.5-flash", system_instruction=CSV_CONVERSION_PROMPT)
                    csv_response = csv_model.generate_content(f"Convertis ces cas de test en JSON :\n\n{result}")
                    raw_json = csv_response.text.strip()
                    if raw_json.startswith("```"): raw_json = raw_json.split("\n", 1)[1]
                    if raw_json.endswith("```"): raw_json = raw_json.rsplit("```", 1)[0]
                    raw_json = raw_json.strip()
                    test_cases = json.loads(raw_json)
                    st.session_state['csv_data'] = json_to_jira_csv(test_cases)
                    st.session_state['csv_count'] = len(test_cases)
                except Exception:
                    st.session_state['csv_data'] = None
                    st.session_state['csv_count'] = 0
                    st.warning(f"CSV error: {str(e)}")

            with st.spinner("Génération des scénarios Gherkin..."):
                try:
                    gherkin_model = genai.GenerativeModel(model_name="gemini-2.5-flash", system_instruction=GHERKIN_CONVERSION_PROMPT)
                    gherkin_response = gherkin_model.generate_content(f"Convertis ces cas de test en scénarios Gherkin :\n\n{result}")
                    gherkin_text = gherkin_response.text.strip()
                    if gherkin_text.startswith("```"): gherkin_text = gherkin_text.split("\n", 1)[1]
                    if gherkin_text.endswith("```"): gherkin_text = gherkin_text.rsplit("```", 1)[0]
                    st.session_state['gherkin_data'] = gherkin_text.strip()
                except Exception:
                    st.session_state['gherkin_data'] = None

        except Exception as e:
            st.error(f"Erreur : {str(e)}")

# --- Display results from session_state ---
if st.session_state.get('result'):
    result = st.session_state['result']
    us = st.session_state.get('user_story', '')
    ctx = st.session_state.get('app_context', '')

    st.markdown("---")

    tab_results, tab_gherkin = st.tabs(["Cas de test", "Gherkin / BDD"])

    with tab_results:
        st.markdown(result)

    with tab_gherkin:
        gherkin_data = st.session_state.get('gherkin_data')
        if gherkin_data:
            st.code(gherkin_data, language="gherkin")
        else:
            st.info("Gherkin non disponible pour cette génération.")

    st.markdown("---")
    st.markdown(f'<p class="section-title">{ICON_DOWNLOAD} Exporter les résultats</p>', unsafe_allow_html=True)

    col_exp1, col_exp2, col_exp3, col_exp4 = st.columns(4)

    with col_exp1:
        export_header = f"# QA Test Generator\n\n## User Story\n{us}"
        if ctx.strip(): export_header += f"\n\n## Contexte applicatif\n{ctx}"
        markdown_content = f"{export_header}\n\n---\n\n{result}"
        st.download_button(label="Markdown", data=markdown_content, file_name="test_cases.md", mime="text/markdown", use_container_width=True, key="dl_markdown")

    with col_exp2:
        txt_header = f"User Story:\n{us}"
        if ctx.strip(): txt_header += f"\n\nContexte applicatif:\n{ctx}"
        txt_content = f"{txt_header}\n\n---\n\n{result}"
        st.download_button(label="TXT", data=txt_content, file_name="test_cases.txt", mime="text/plain", use_container_width=True, key="dl_txt")

    with col_exp3:
        csv_data = st.session_state.get('csv_data')
        csv_count = st.session_state.get('csv_count', 0)
        if csv_data:
            st.download_button(label=f"CSV Jira ({csv_count})", data=csv_data, file_name="test_cases_jira.csv", mime="text/csv", use_container_width=True, key="dl_csv")
        else:
            st.warning("CSV indisponible")

    with col_exp4:
        gherkin_data = st.session_state.get('gherkin_data')
        if gherkin_data:
            st.download_button(label="Gherkin", data=gherkin_data, file_name="test_cases.feature", mime="text/plain", use_container_width=True, key="dl_gherkin")
        else:
            st.warning("Gherkin indisponible")

# --- Footer ---
st.markdown(f"""
<div class="footer">
    QA Test Generator {ICON_SHIELD} Propuls&eacute; par l'IA · Fait pour la communaut&eacute; QA<br>
    <span style="font-size: 0.7rem; color: #d1d5db;">Un outil par Amadou FOFANA — Le Testeur Augment&eacute;</span>
</div>
""", unsafe_allow_html=True)
