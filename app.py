import streamlit as st
import google.generativeai as genai
import json
import csv
import io
import re

# --- SVG Icons ---
ICON_ZAP = '<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#059669" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg>'
ICON_CLIPBOARD = '<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#059669" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"/><rect x="8" y="2" width="8" height="4" rx="1" ry="1"/></svg>'
ICON_DOWNLOAD = '<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#059669" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>'
ICON_SHIELD = '<svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#059669" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>'
ICON_MSG = '<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#059669" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg>'

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
.question-box {
    background: #f0fdf4; border: 1px solid #a7f3d0; border-radius: 8px;
    padding: 1rem; margin: 0.5rem 0;
}
.footer {
    text-align: center; color: #9ca3af; font-size: 0.8rem; padding: 2rem 0 1rem 0;
    border-top: 1px solid #e5e7eb; margin-top: 3rem;
}
.footer svg { vertical-align: -3px; margin: 0 3px; }
</style>
""", unsafe_allow_html=True)

# --- Prompts (all bilingual to avoid language bias) ---
ANALYSIS_PROMPT = """You are a senior QA expert. / Tu es un expert QA senior.
You are given a User Story. You must analyze the MISSING information needed to generate complete and executable test cases.

LANGUAGE: Detect the language of the User Story. Ask all questions in the same language. If the User Story is in English, questions must be in English. If in French, questions must be in French.

Return ONLY valid JSON with this structure:
{
  "questions": [
    {
      "id": "app_name",
      "question": "What is the application name? / Quel est le nom de l'application ?",
      "why": "To name test cases and URLs / Pour nommer les cas de test et les URLs",
      "example": "MyApp.com / MonBanquier.fr"
    }
  ]
}

RULES:
- Identify between 3 and 8 questions maximum — the most important only
- Each question must target CONCRETE data needed for test cases
- Possible question categories: app name, URLs/pages, button/field names, user roles, validation rules (password, email...), error/success messages, test data (credentials), technical constraints
- Do NOT include questions about the User Story itself — it is already provided
- The "why" field explains why this info is needed
- The "example" field gives a concrete example answer
- Return ONLY the JSON, nothing else
- No backticks, no comments"""

SYSTEM_PROMPT = """You are a senior QA expert with 15 years of experience in software testing. / Tu es un expert QA senior avec 15 ans d'expérience en test logiciel.

You generate CONCRETE and EXECUTABLE test cases. A junior tester who does not know the application must be able to execute each test case without asking any questions.

=== ABSOLUTE RULE / RÈGLE ABSOLUE ===
Use ONLY the information provided in the application context.
Do not complete, do not invent, do not extrapolate.
If some data is still missing despite the context provided, mark it [TO BE DEFINED BY TESTER] or [À DÉFINIR PAR LE TESTEUR].
LANGUAGE: Detect the language of the User Story. Respond ENTIRELY in that language. If the User Story is in English, EVERYTHING must be in English. If in French, EVERYTHING must be in French.
=== END RULE / FIN RÈGLE ===

From the User Story and application context provided, generate:
NEVER introduce yourself. No introduction. Start DIRECTLY with section 1.

## 1. FUNCTIONAL TEST CASES / CAS DE TEST FONCTIONNELS
This section must contain ~70% of all test cases. Include ALL nominal, alternative, and error cases here.
Number each case: CTF-001, CTF-002, CTF-003, etc.
For each test case, use exactly this structure (in the language of the User Story):
- Title / Titre
- Preconditions / Préconditions
- Test Data / Données de test
- Numbered Steps / Étapes numérotées
- Expected Result / Résultat attendu
- Priority (High/Medium/Low) / Priorité (Haute/Moyenne/Basse)

## 2. EDGE CASES / CAS LIMITES
This section must contain ~30% of all test cases. ONLY boundary values, concurrency, timeout, and extreme scenarios that go beyond normal functional testing.
Number each case: CE-001, CE-002, CE-003, etc.
Use the same structure as functional test cases:
- Title / Titre
- Preconditions / Préconditions
- Test Data / Données de test
- Numbered Steps / Étapes numérotées
- Expected Result / Résultat attendu
- Priority (High/Medium/Low) / Priorité (Haute/Moyenne/Basse)

## 3. RISK SUGGESTIONS / SUGGESTIONS DE RISQUES
Number each risk: R-001, R-002, R-003, etc.
Functional, performance, security, integration risks. For each: title + description + impact + mitigation

RULES: exhaustive but relevant, clear language, structured Markdown."""

SYSTEM_PROMPT_DIRECT = """You are a senior QA expert with 15 years of experience in software testing. / Tu es un expert QA senior avec 15 ans d'expérience en test logiciel.

You generate CONCRETE and EXECUTABLE test cases. A junior tester who does not know the application must be able to execute each test case without asking any questions.

=== ABSOLUTE RULE ON DATA / RÈGLE ABSOLUE SUR LES DONNÉES ===
If application context is provided:
- Use ONLY the information given
- Do not complete, do not invent, do not extrapolate
- If some data is missing, mark it [TO BE DEFINED BY TESTER] or [À DÉFINIR PAR LE TESTEUR]

If NO application context is provided:
- Do NOT INVENT any context
- For EACH missing data point, write: [TO BE DEFINED BY TESTER] or [À DÉFINIR PAR LE TESTEUR]

LANGUAGE: Detect the language of the User Story. Respond ENTIRELY in that language. If the User Story is in English, EVERYTHING must be in English. If in French, EVERYTHING must be in French.
=== END RULE / FIN RÈGLE ===

From the User Story (and application context if provided), generate:

NEVER introduce yourself. No introduction. Start DIRECTLY with section 1.

## 1. FUNCTIONAL TEST CASES / CAS DE TEST FONCTIONNELS
This section must contain ~70% of all test cases. Include ALL nominal, alternative, and error cases here.
Number each case: CTF-001, CTF-002, CTF-003, etc.
For each test case, use exactly this structure (in the language of the User Story):
- Title / Titre
- Preconditions / Préconditions
- Test Data / Données de test
- Numbered Steps / Étapes numérotées
- Expected Result / Résultat attendu
- Priority (High/Medium/Low) / Priorité (Haute/Moyenne/Basse)

## 2. EDGE CASES / CAS LIMITES
This section must contain ~30% of all test cases. ONLY boundary values, concurrency, timeout, and extreme scenarios that go beyond normal functional testing.
Number each case: CE-001, CE-002, CE-003, etc.
Use the same structure as functional test cases:
- Title / Titre
- Preconditions / Préconditions
- Test Data / Données de test
- Numbered Steps / Étapes numérotées
- Expected Result / Résultat attendu
- Priority (High/Medium/Low) / Priorité (Haute/Moyenne/Basse)

## 3. RISK SUGGESTIONS / SUGGESTIONS DE RISQUES
Number each risk: R-001, R-002, R-003, etc.
Functional, performance, security, integration risks. For each: title + description + impact + mitigation

RULES: exhaustive but relevant, clear language, structured Markdown."""

CSV_CONVERSION_PROMPT = """Convert the test cases into a strict JSON table for Jira. / Convertis les cas de test en tableau JSON strict pour Jira.
Extract functional and edge cases (NOT risks). / Extrais les cas fonctionnels et limites (PAS les risques).
Fields: "Test Case ID" (keep original IDs: CTF-001, CE-001, etc.), "Summary", "Description", "Preconditions", "Test Steps", "Expected Result", "Priority".
Content must be in the same language as the test cases provided.
Return ONLY valid JSON. No backticks. No Markdown in values."""

GHERKIN_CONVERSION_PROMPT = """Convert the test cases into strict Gherkin format. / Convertis les cas de test en Gherkin strict.
Gherkin keywords (Feature, Scenario, Given, When, Then, And, Scenario Outline, Examples) are always in English.
ALL other content (Feature titles, Scenario titles, step content, Examples data) MUST be in the same language as the test cases provided. If test cases are in English, ALL content must be in English. If test cases are in French, ALL content must be in French.
Each test case = one Scenario. Do not include risks.
Use Scenario Outline with Examples for multiple data sets.
Plain text only, no Markdown."""

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
    st.markdown("""1. Collez votre User Story
2. Choisissez le mode :
   - **Guidé** : l'IA vous pose des questions avant de générer
   - **Direct** : génération immédiate
3. Exportez en Markdown, TXT, CSV Jira ou Gherkin""")
    st.markdown("---")
    st.markdown("### Exemple de User Story")
    st.code("En tant qu'utilisateur,\nje veux pouvoir réinitialiser\nmon mot de passe via email,\nafin de récupérer l'accès\nà mon compte.", language=None)
    st.markdown("---")
    st.markdown("### Exports disponibles")
    st.markdown("Markdown · TXT · CSV Jira · Gherkin")

# --- Helpers ---
def json_to_jira_csv(test_cases_json):
    output = io.StringIO()
    fieldnames = ["Test Case ID", "Summary", "Description", "Preconditions", "Test Steps", "Expected Result", "Priority"]
    writer = csv.DictWriter(output, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
    writer.writeheader()
    for tc in test_cases_json:
        def to_str(val):
            if val is None:
                return ""
            if isinstance(val, list):
                return "\n".join(str(item) for item in val)
            return str(val)
        def fmt(val):
            val = to_str(val)
            val = re.sub(r'(?<!\n)\s*(\d+)\.\s', lambda m: ('\n' + m.group(1) + '. ') if int(m.group(1)) > 1 else (m.group(1) + '. '), val)
            return val.strip()
        def trunc(val, limit=255):
            val = to_str(val)
            return val[:252] + "..." if len(val) > limit else val
        writer.writerow({
            "Test Case ID": to_str(tc.get("Test Case ID", "")),
            "Summary": trunc(tc.get("Summary", "")),
            "Description": to_str(tc.get("Description", "")),
            "Preconditions": trunc(fmt(tc.get("Preconditions", ""))),
            "Test Steps": trunc(fmt(tc.get("Test Steps", ""))),
            "Expected Result": trunc(fmt(tc.get("Expected Result", ""))),
            "Priority": to_str(tc.get("Priority", "")),
        })
    return output.getvalue()

def generate_csv(result):
    try:
        genai.configure(api_key=api_key)
        m = genai.GenerativeModel(model_name="gemini-2.5-flash", system_instruction=CSV_CONVERSION_PROMPT)
        r = m.generate_content(f"Convert these test cases to JSON / Convertis ces cas de test en JSON :\n\n{result}")
        raw = r.text.strip()
        if raw.startswith("```"): raw = raw.split("\n", 1)[1]
        if raw.endswith("```"): raw = raw.rsplit("```", 1)[0]
        tc = json.loads(raw.strip())
        return json_to_jira_csv(tc), len(tc)
    except Exception as e:
        st.error(f"Erreur CSV : {str(e)}")
        return None, 0

def generate_gherkin(result):
    try:
        genai.configure(api_key=api_key)
        m = genai.GenerativeModel(model_name="gemini-2.5-flash", system_instruction=GHERKIN_CONVERSION_PROMPT)
        r = m.generate_content(f"Convert these test cases to Gherkin scenarios / Convertis ces cas de test en scénarios Gherkin :\n\n{result}")
        t = r.text.strip()
        if t.startswith("```"): t = t.split("\n", 1)[1]
        if t.endswith("```"): t = t.rsplit("```", 1)[0]
        return t.strip()
    except Exception as e:
        st.error(f"Erreur Gherkin : {str(e)}")
        return None

# --- Init session state ---
for key in ['result', 'user_story', 'app_context',
            'csv_data', 'csv_count', 'gherkin_data', 'questions', 'answers',
            'step', 'analysis_us', 'pending_csv', 'pending_gherkin']:
    if key not in st.session_state:
        if key in ['user_story', 'app_context', 'analysis_us']:
            st.session_state[key] = ""
        elif key in ['result', 'csv_data', 'gherkin_data', 'questions']:
            st.session_state[key] = None
        elif key in ['csv_count']:
            st.session_state[key] = 0
        elif key == 'answers':
            st.session_state[key] = {}
        elif key == 'step':
            st.session_state[key] = 'input'
        elif key in ['pending_csv', 'pending_gherkin']:
            st.session_state[key] = False

# --- Handle pending CSV/Gherkin generation (runs BEFORE UI to avoid double-click) ---
if st.session_state.get('pending_csv') and st.session_state.get('result'):
    st.session_state['pending_csv'] = False
    with st.spinner("Conversion en CSV Jira..."):
        csv_data, csv_count = generate_csv(st.session_state['result'])
        if csv_data:
            st.session_state['csv_data'] = csv_data
            st.session_state['csv_count'] = csv_count
            st.rerun()

if st.session_state.get('pending_gherkin') and st.session_state.get('result'):
    st.session_state['pending_gherkin'] = False
    with st.spinner("Génération Gherkin..."):
        gherkin_data = generate_gherkin(st.session_state['result'])
        if gherkin_data:
            st.session_state['gherkin_data'] = gherkin_data
            st.rerun()

# --- Main Input ---
st.markdown(f'<p class="section-title">{ICON_CLIPBOARD} Votre User Story</p>', unsafe_allow_html=True)

col_demo1, col_demo2, col_demo3 = st.columns([1, 1, 1])
with col_demo2:
    def load_demo():
        st.session_state['user_story_input'] = DEMO_USER_STORY
        st.session_state['step'] = 'input'
        st.session_state['result'] = None
        st.session_state['questions'] = None

    st.button("Voir une démo — pré-remplir avec un exemple", use_container_width=True, on_click=load_demo)

if 'user_story_input' not in st.session_state:
    st.session_state['user_story_input'] = ""

user_story = st.text_area(
    "User Story", height=150, key="user_story_input",
    placeholder="En tant que [rôle], je veux [action], afin de [bénéfice]...",
    label_visibility="collapsed"
)

# --- Mode Selection + Generate ---
st.markdown("---")

if st.session_state.get('step') == 'input' or st.session_state.get('step') is None:
    col_mode1, col_mode2 = st.columns(2)

    with col_mode1:
        guided = st.button("Mode guidé — l'IA pose des questions d'abord", use_container_width=True, type="primary")

    with col_mode2:
        direct = st.button("Mode direct — génération immédiate", use_container_width=True)

    # --- GUIDED MODE: Step 1 - Analysis ---
    if guided:
        st.session_state['result'] = None
        st.session_state['csv_data'] = None
        st.session_state['gherkin_data'] = None

        if not api_key:
            st.error("Configuration API manquante.")
        elif not user_story.strip():
            st.error("Collez une User Story pour commencer.")
        else:
            try:
                genai.configure(api_key=api_key)
                model = genai.GenerativeModel(model_name="gemini-2.5-flash", system_instruction=ANALYSIS_PROMPT)

                with st.spinner("Analyse de la User Story..."):
                    response = model.generate_content(f"Analyze this User Story and identify missing information / Analyse cette User Story et identifie les informations manquantes :\n\n{user_story}")
                    raw = response.text.strip()
                    if raw.startswith("```"): raw = raw.split("\n", 1)[1]
                    if raw.endswith("```"): raw = raw.rsplit("```", 1)[0]
                    questions_data = json.loads(raw.strip())

                st.session_state['questions'] = questions_data.get('questions', [])
                st.session_state['answers'] = {}
                st.session_state['analysis_us'] = user_story
                st.session_state['step'] = 'questions'
                st.rerun()

            except Exception as e:
                st.error(f"Erreur d'analyse : {str(e)}")

    # --- DIRECT MODE ---
    if direct:
        st.session_state['result'] = None
        st.session_state['csv_data'] = None
        st.session_state['gherkin_data'] = None
        st.session_state['questions'] = None
        st.session_state['step'] = 'input'

        if not api_key:
            st.error("Configuration API manquante.")
        elif not user_story.strip():
            st.error("Collez une User Story pour commencer.")
        else:
            try:
                genai.configure(api_key=api_key)
                model = genai.GenerativeModel(model_name="gemini-2.5-flash", system_instruction=SYSTEM_PROMPT_DIRECT)
                user_message = f"NO APPLICATION CONTEXT PROVIDED / AUCUN CONTEXTE APPLICATIF FOURNI.\n\n---\n\nUSER STORY:\n{user_story}"

                with st.spinner("Analyse et génération des tests..."):
                    response = model.generate_content(user_message)
                    result = response.text
                    if "## 1." in result:
                        result = result[result.index("## 1."):]

                st.session_state['result'] = result
                st.session_state['user_story'] = user_story
                st.session_state['app_context'] = ""
                st.rerun()

            except Exception as e:
                st.error(f"Erreur : {str(e)}")

# --- GUIDED MODE: Step 2 - Questions Form ---
if st.session_state.get('step') == 'questions' and st.session_state.get('questions'):
    questions = st.session_state['questions']

    st.markdown(f'<p class="section-title">{ICON_MSG} L\'IA a besoin de quelques pr&eacute;cisions</p>', unsafe_allow_html=True)
    st.markdown("Remplissez les champs ci-dessous pour obtenir des cas de test **complets et prêts à exécuter**. Laissez vide si vous ne savez pas.")

    with st.form("questions_form"):
        answers = {}
        for q in questions:
            answers[q['id']] = st.text_input(
                q['question'],
                placeholder=f"Ex: {q.get('example', '')}",
                help=q.get('why', ''),
                key=f"q_{q['id']}"
            )

        col_sub1, col_sub2, col_sub3 = st.columns([1, 1, 1])
        with col_sub2:
            submitted = st.form_submit_button("Générer les cas de test", use_container_width=True, type="primary")

        if submitted:
            context_parts = []
            for q in questions:
                answer = answers.get(q['id'], '').strip()
                if answer:
                    context_parts.append(f"{q['question']} : {answer}")

            built_context = "\n".join(context_parts)
            us = st.session_state.get('analysis_us', '')

            try:
                genai.configure(api_key=api_key)
                model = genai.GenerativeModel(model_name="gemini-2.5-flash", system_instruction=SYSTEM_PROMPT)

                user_message = f"APPLICATION CONTEXT / CONTEXTE APPLICATIF :\n{built_context}\n\n---\n\nUSER STORY:\n{us}"

                with st.spinner("Génération des cas de test avec vos précisions..."):
                    response = model.generate_content(user_message)
                    result = response.text
                    if "## 1." in result:
                        result = result[result.index("## 1."):]

                st.session_state['result'] = result
                st.session_state['user_story'] = us
                st.session_state['app_context'] = built_context
                st.session_state['step'] = 'results'
                st.session_state['csv_data'] = None
                st.session_state['gherkin_data'] = None
                st.rerun()

            except Exception as e:
                st.error(f"Erreur : {str(e)}")

    if st.button("Revenir à la saisie", key="back_to_input"):
        st.session_state['step'] = 'input'
        st.session_state['questions'] = None
        st.session_state['result'] = None
        st.session_state['csv_data'] = None
        st.session_state['gherkin_data'] = None
        st.rerun()

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

    st.markdown("---")
    st.markdown(f'<p class="section-title">{ICON_DOWNLOAD} Exporter les r&eacute;sultats</p>', unsafe_allow_html=True)

    col_exp1, col_exp2, col_exp3, col_exp4 = st.columns(4)

    with col_exp1:
        export_header = f"# QA Test Generator\n\n## User Story\n{us}"
        if ctx.strip(): export_header += f"\n\n## Application Context\n{ctx}"
        markdown_content = f"{export_header}\n\n---\n\n{result}"
        st.download_button(label="Markdown", data=markdown_content, file_name="test_cases.md", mime="text/markdown", use_container_width=True, key="dl_markdown")

    with col_exp2:
        txt_header = f"User Story:\n{us}"
        if ctx.strip(): txt_header += f"\n\nApplication Context:\n{ctx}"
        txt_content = f"{txt_header}\n\n---\n\n{result}"
        st.download_button(label="TXT", data=txt_content, file_name="test_cases.txt", mime="text/plain", use_container_width=True, key="dl_txt")

    with col_exp3:
        csv_data = st.session_state.get('csv_data')
        if csv_data:
            csv_count = st.session_state.get('csv_count', 0)
            st.download_button(label=f"CSV Jira ({csv_count})", data=csv_data, file_name="test_cases_jira.csv", mime="text/csv", use_container_width=True, key="dl_csv")
        else:
            def trigger_csv():
                st.session_state['pending_csv'] = True
            st.button("Générer CSV Jira", use_container_width=True, key="btn_csv", on_click=trigger_csv)

    with col_exp4:
        gherkin_data = st.session_state.get('gherkin_data')
        if gherkin_data:
            st.download_button(label="Gherkin", data=gherkin_data, file_name="test_cases.feature", mime="text/plain", use_container_width=True, key="dl_gherkin")
        else:
            def trigger_gherkin():
                st.session_state['pending_gherkin'] = True
            st.button("Générer Gherkin", use_container_width=True, key="btn_gherkin", on_click=trigger_gherkin)

    st.markdown("---")
    col_new1, col_new2, col_new3 = st.columns([1, 1, 1])
    with col_new2:
        def reset_app():
            for key in ['result', 'csv_data', 'gherkin_data', 'questions']:
                st.session_state[key] = None
            st.session_state['step'] = 'input'
            st.session_state['csv_count'] = 0
            st.session_state['answers'] = {}
            st.session_state['user_story_input'] = ""
            st.session_state['pending_csv'] = False
            st.session_state['pending_gherkin'] = False

        st.button("Nouvelle génération", use_container_width=True, on_click=reset_app)

# --- Footer ---
st.markdown(f"""
<div class="footer">
    QA Test Generator {ICON_SHIELD} Propuls&eacute; par l'IA · Fait pour la communaut&eacute; QA<br>
    <span style="font-size: 0.7rem; color: #d1d5db;">Un outil par Amadou FOFANA — Le Testeur Augment&eacute;</span>
</div>
""", unsafe_allow_html=True)
