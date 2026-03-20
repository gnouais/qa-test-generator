import streamlit as st
import google.generativeai as genai
import json
import time
import csv
import io
import re

# --- SVG Icons (Emerald, 20px, inline) ---
ICON_ZAP = '<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#059669" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg>'
ICON_CLIPBOARD = '<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#059669" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"/><rect x="8" y="2" width="8" height="4" rx="1" ry="1"/></svg>'
ICON_DOWNLOAD = '<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#059669" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>'
ICON_SHIELD = '<svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#059669" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>'

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
st.set_page_config(page_title="QA Test Generator", page_icon="✓", layout="wide")

# --- Custom CSS ---
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;600;700&family=DM+Sans:wght@400;500;600;700&display=swap');
.stApp { font-family: 'DM Sans', sans-serif; }
.main-header { text-align: center; padding: 2.5rem 0 1.5rem 0; }
.main-header h1 {
    font-family: 'JetBrains Mono', monospace; font-size: 2.4rem; font-weight: 700;
    background: linear-gradient(135deg, #059669, #10B981, #34D399);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent; margin-bottom: 0.5rem;
}
.main-header .tagline { font-size: 1.15rem; color: #6b7280; margin-top: 0; margin-bottom: 1rem; }
.badge {
    display: inline-block; background: #ecfdf5; color: #059669; font-size: 0.7rem; font-weight: 700;
    padding: 0.3rem 0.9rem; border-radius: 999px; border: 1px solid #a7f3d0; margin-bottom: 0.8rem;
    letter-spacing: 1px; text-transform: uppercase;
}
.badge svg { vertical-align: -3px; margin-right: 4px; }
.welcome-stats { display: flex; justify-content: center; gap: 2.5rem; margin-top: 1.2rem; margin-bottom: 0.5rem; }
.stat-item { text-align: center; }
.stat-number { font-family: 'JetBrains Mono', monospace; font-size: 1.5rem; font-weight: 700; color: #059669; }
.stat-label { font-size: 0.78rem; color: #9ca3af; margin-top: 0.15rem; }
.section-title {
    font-family: 'JetBrains Mono', monospace; font-size: 0.95rem; font-weight: 600;
    color: #374151; letter-spacing: 0.3px; margin-bottom: 0.5rem;
}
.section-title svg { vertical-align: -4px; margin-right: 6px; }
section[data-testid="stSidebar"] { background-color: #f0fdf4; }
section[data-testid="stSidebar"] .stMarkdown h3 {
    color: #059669; font-family: 'JetBrains Mono', monospace; font-size: 0.9rem;
}
.stButton > button[kind="primary"] {
    background: linear-gradient(135deg, #059669, #10B981) !important; color: white !important;
    border: none !important; font-weight: 600 !important; padding: 0.6rem 1.5rem !important;
    border-radius: 8px !important; font-size: 1rem !important; transition: all 0.2s ease !important;
}
.stButton > button[kind="primary"]:hover {
    background: linear-gradient(135deg, #047857, #059669) !important;
    transform: translateY(-1px) !important; box-shadow: 0 4px 12px rgba(5, 150, 105, 0.3) !important;
}
.stDownloadButton > button {
    border: 1px solid #d1fae5 !important; color: #059669 !important; font-weight: 600 !important;
    border-radius: 8px !important; transition: all 0.2s ease !important;
}
.stDownloadButton > button:hover { background-color: #ecfdf5 !important; border-color: #059669 !important; }
.stTextArea textarea {
    border-radius: 8px !important; border: 1px solid #d1d5db !important; font-family: 'DM Sans', sans-serif !important;
}
.stTextArea textarea:focus { border-color: #10B981 !important; box-shadow: 0 0 0 2px rgba(16, 185, 129, 0.15) !important; }
.footer {
    text-align: center; color: #9ca3af; font-size: 0.8rem; padding: 2rem 0 1rem 0;
    border-top: 1px solid #e5e7eb; margin-top: 3rem;
}
.footer svg { vertical-align: -3px; margin: 0 3px; }
</style>
""", unsafe_allow_html=True)

# --- Prompts ---
SYSTEM_PROMPT = """Tu es un expert QA senior avec 15 ans d'expérience en test logiciel.

Tu génères des cas de test CONCRETS et EXÉCUTABLES. Un testeur junior qui ne connaît pas l'application doit pouvoir exécuter chaque cas de test sans poser de question.

=== RÈGLE ABSOLUE SUR LES DONNÉES ===

Si un contexte applicatif est fourni :
- Utilise UNIQUEMENT les informations données
- Ne complète pas, n'invente pas, n'extrapole pas
- Si certaines données manquent, marque-les [À DÉFINIR PAR LE TESTEUR]

Si AUCUN contexte applicatif n'est fourni :
- N'INVENTE AUCUN contexte
- Pour CHAQUE donnée non fournie, écris : [À DÉFINIR PAR LE TESTEUR]

=== FIN RÈGLE ABSOLUE ===

À partir de la User Story (et du contexte applicatif si fourni), génère :

## 1. CAS DE TEST FONCTIONNELS
Pour chaque cas de test : Titre, Préconditions, Données de test, Étapes numérotées, Résultat attendu, Priorité (Haute/Moyenne/Basse)

## 2. CAS LIMITES (EDGE CASES)
Valeurs limites, erreurs, concurrence, timeout. Pour chaque : titre + données + description + résultat attendu

## 3. SUGGESTIONS DE RISQUES
Risques fonctionnels, performance, sécurité, intégration. Pour chaque : titre + description + impact + mitigation

RÈGLES : exhaustif mais pertinent, langage clair, français sauf termes techniques, Markdown structuré.
"""

CSV_CONVERSION_PROMPT = """Convertis les cas de test en tableau JSON strict pour Jira.
Extrais les cas fonctionnels et limites (PAS les risques).
Champs : "Test Case ID" (TC-001...), "Summary", "Description", "Preconditions", "Test Steps", "Expected Result", "Priority" (Haute/Moyenne/Basse).
Retourne UNIQUEMENT le JSON. Pas de backticks. JSON valide uniquement. Pas de Markdown dans les valeurs."""

GHERKIN_CONVERSION_PROMPT = """Convertis les cas de test en Gherkin strict.
Feature/Scenario/Given/When/Then en anglais, contenu en français.
Chaque cas de test = un Scenario. Pas les risques.
Scenario Outline avec Examples pour les jeux de données multiples.
Texte brut uniquement, pas de Markdown."""

# --- Header ---
st.markdown(f"""
<div class="main-header">
    <div class="badge">{ICON_ZAP} Propuls&eacute; par l'IA</div>
    <h1>QA Test Generator</h1>
    <p class="tagline">Transformez vos User Stories en cas de test complets en 30 secondes.</p>
    <div class="welcome-stats">
        <div class="stat-item"><div class="stat-number">4</div><div class="stat-label">Formats d'export</div></div>
        <div class="stat-item"><div class="stat-number">30s</div><div class="stat-label">Temps de g&eacute;n&eacute;ration</div></div>
        <div class="stat-item"><div class="stat-number">0</div><div class="stat-label">Config requise</div></div>
    </div>
</div>
""", unsafe_allow_html=True)

# --- API Key ---
api_key = st.secrets.get("GEMINI_API_KEY", "")

# --- Sidebar ---
with st.sidebar:
    st.markdown("### QA Test Generator")
    st.markdown("---")
    st.markdown("### Guide rapide")
    st.markdown("1. Collez votre User Story\n2. *(Optionnel)* Ajoutez le contexte\n3. Cliquez **Générer**\n4. Exportez")
    st.markdown("---")
    st.markdown("### Exemple de User Story")
    st.code("En tant qu'utilisateur,\nje veux pouvoir réinitialiser\nmon mot de passe via email,\nafin de récupérer l'accès\nà mon compte.", language=None)
    st.markdown("---")
    st.markdown("### Exports disponibles")
    st.markdown("Markdown · TXT · CSV Jira · Gherkin")

# --- Helper: CSV ---
def json_to_jira_csv(test_cases_json):
    output = io.StringIO()
    fieldnames = ["Test Case ID", "Résumé", "Description", "Preconditions", "Test Steps", "Expected Result", "Priorité"]
    writer = csv.DictWriter(output, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
    writer.writeheader()
    for tc in test_cases_json:
        def fmt(val):
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
            "Preconditions": trunc(fmt(tc.get("Preconditions", ""))),
            "Test Steps": trunc(fmt(tc.get("Test Steps", ""))),
            "Expected Result": trunc(fmt(tc.get("Expected Result", ""))),
            "Priorité": tc.get("Priority", "Moyenne"),
        })
    return output.getvalue()

# --- Helper: Generate CSV on demand ---
def generate_csv(result):
    try:
        genai.configure(api_key=api_key)
        csv_model = genai.GenerativeModel(model_name="gemini-2.5-flash", system_instruction=CSV_CONVERSION_PROMPT)
        csv_response = csv_model.generate_content(f"Convertis ces cas de test en JSON :\n\n{result}")
        raw_json = csv_response.text.strip()
        if raw_json.startswith("```"): raw_json = raw_json.split("\n", 1)[1]
        if raw_json.endswith("```"): raw_json = raw_json.rsplit("```", 1)[0]
        raw_json = raw_json.strip()
        test_cases = json.loads(raw_json)
        return json_to_jira_csv(test_cases), len(test_cases)
    except Exception:
        return None, 0

# --- Helper: Generate Gherkin on demand ---
def generate_gherkin(result):
    try:
        genai.configure(api_key=api_key)
        gherkin_model = genai.GenerativeModel(model_name="gemini-2.5-flash", system_instruction=GHERKIN_CONVERSION_PROMPT)
        gherkin_response = gherkin_model.generate_content(f"Convertis ces cas de test en scénarios Gherkin :\n\n{result}")
        gherkin_text = gherkin_response.text.strip()
        if gherkin_text.startswith("```"): gherkin_text = gherkin_text.split("\n", 1)[1]
        if gherkin_text.endswith("```"): gherkin_text = gherkin_text.rsplit("```", 1)[0]
        return gherkin_text.strip()
    except Exception:
        return None

# --- Demo state ---
if 'demo_us' not in st.session_state:
    st.session_state['demo_us'] = ""
if 'demo_ctx' not in st.session_state:
    st.session_state['demo_ctx'] = ""

# --- Main Inputs ---
st.markdown(f'<p class="section-title">{ICON_CLIPBOARD} Votre User Story</p>', unsafe_allow_html=True)

col_demo1, col_demo2, col_demo3 = st.columns([1, 1, 1])
with col_demo2:
    if st.button("Voir une démo — pré-remplir avec un exemple", use_container_width=True):
        st.session_state['demo_us'] = DEMO_USER_STORY
        st.session_state['demo_ctx'] = DEMO_CONTEXT

user_story = st.text_area(
    "User Story", height=150, value=st.session_state.get('demo_us', ''),
    placeholder="En tant que [rôle], je veux [action], afin de [bénéfice]...",
    label_visibility="collapsed"
)

with st.expander("Contexte applicatif (optionnel — recommandé pour des tests plus précis)", expanded=bool(st.session_state.get('demo_ctx', ''))):
    app_context = st.text_area(
        "Contexte", height=120, value=st.session_state.get('demo_ctx', ''),
        placeholder="Nom de l'app, type, URL, pages, rôles, règles métier...",
        label_visibility="collapsed"
    )

# --- Generate Button ---
col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    generate = st.button("Générer les cas de test", use_container_width=True, type="primary")

# --- Generation Logic (1 seul appel API) ---
if generate:
    st.session_state['demo_us'] = ""
    st.session_state['demo_ctx'] = ""
    # Reset export caches
    st.session_state['csv_data'] = None
    st.session_state['csv_count'] = 0
    st.session_state['gherkin_data'] = None

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
                user_message = f"AUCUN CONTEXTE APPLICATIF FOURNI. Tu DOIS utiliser [À DÉFINIR PAR LE TESTEUR] pour toute donnée spécifique. N'invente RIEN.\n\n---\n\nUSER STORY À ANALYSER :\n{user_story}"

            with st.spinner("Analyse et génération des tests..."):
                response = model.generate_content(user_message)
                result = response.text

            st.session_state['result'] = result
            st.session_state['user_story'] = user_story
            st.session_state['app_context'] = app_context if app_context else ""

        except Exception as e:
            st.error(f"Erreur : {str(e)}")

# --- Display results ---
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
            st.info("Cliquez sur le bouton Gherkin dans les exports pour générer les scénarios BDD.")

    # --- Export Options ---
    st.markdown("---")
    st.markdown(f'<p class="section-title">{ICON_DOWNLOAD} Exporter les résultats</p>', unsafe_allow_html=True)

    col_exp1, col_exp2, col_exp3, col_exp4 = st.columns(4)

    # Markdown — toujours disponible
    with col_exp1:
        export_header = f"# QA Test Generator\n\n## User Story\n{us}"
        if ctx.strip(): export_header += f"\n\n## Contexte applicatif\n{ctx}"
        markdown_content = f"{export_header}\n\n---\n\n{result}"
        st.download_button(label="Markdown", data=markdown_content, file_name="test_cases.md", mime="text/markdown", use_container_width=True, key="dl_markdown")

    # TXT — toujours disponible
    with col_exp2:
        txt_header = f"User Story:\n{us}"
        if ctx.strip(): txt_header += f"\n\nContexte applicatif:\n{ctx}"
        txt_content = f"{txt_header}\n\n---\n\n{result}"
        st.download_button(label="TXT", data=txt_content, file_name="test_cases.txt", mime="text/plain", use_container_width=True, key="dl_txt")

    # CSV — généré à la demande
    with col_exp3:
        csv_data = st.session_state.get('csv_data')
        if csv_data:
            csv_count = st.session_state.get('csv_count', 0)
            st.download_button(label=f"CSV Jira ({csv_count})", data=csv_data, file_name="test_cases_jira.csv", mime="text/csv", use_container_width=True, key="dl_csv")
        else:
            if st.button("Générer CSV Jira", use_container_width=True, key="btn_csv"):
                with st.spinner("Conversion en CSV Jira..."):
                    csv_data, csv_count = generate_csv(result)
                    if csv_data:
                        st.session_state['csv_data'] = csv_data
                        st.session_state['csv_count'] = csv_count
                        st.rerun()
                    else:
                        st.error("Erreur de conversion CSV. Réessayez.")

    # Gherkin — généré à la demande
    with col_exp4:
        gherkin_data = st.session_state.get('gherkin_data')
        if gherkin_data:
            st.download_button(label="Gherkin", data=gherkin_data, file_name="test_cases.feature", mime="text/plain", use_container_width=True, key="dl_gherkin")
        else:
            if st.button("Générer Gherkin", use_container_width=True, key="btn_gherkin"):
                with st.spinner("Génération Gherkin..."):
                    gherkin_data = generate_gherkin(result)
                    if gherkin_data:
                        st.session_state['gherkin_data'] = gherkin_data
                        st.rerun()
                    else:
                        st.error("Erreur Gherkin. Réessayez.")

# --- Footer ---
st.markdown(f"""
<div class="footer">
    QA Test Generator {ICON_SHIELD} Propuls&eacute; par l'IA · Fait pour la communaut&eacute; QA<br>
    <span style="font-size: 0.7rem; color: #d1d5db;">Un outil par Amadou FOFANA — Le Testeur Augment&eacute;</span>
</div>
""", unsafe_allow_html=True)
