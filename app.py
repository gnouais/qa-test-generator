import streamlit as st
import google.generativeai as genai
import json
import time
import csv
import io
import re


# --- Page Config ---
st.set_page_config(
    page_title="QA Test Generator",
    page_icon="🧪",
    layout="wide"
)

# --- Custom CSS - Emerald Theme ---
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;600;700&family=DM+Sans:wght@400;500;600;700&display=swap');

/* === GLOBAL === */
.stApp {
    font-family: 'DM Sans', sans-serif;
}

/* === HEADER === */
.main-header {
    text-align: center;
    padding: 2.5rem 0 1.5rem 0;
}
.main-header h1 {
    font-family: 'JetBrains Mono', monospace;
    font-size: 2.4rem;
    font-weight: 700;
    background: linear-gradient(135deg, #059669, #10B981, #34D399);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 0.5rem;
}
.main-header .tagline {
    font-size: 1.15rem;
    color: #6b7280;
    margin-top: 0;
    margin-bottom: 1rem;
}
.badge {
    display: inline-block;
    background: #ecfdf5;
    color: #059669;
    font-size: 0.75rem;
    font-weight: 700;
    padding: 0.3rem 0.9rem;
    border-radius: 999px;
    border: 1px solid #a7f3d0;
    margin-bottom: 0.8rem;
    letter-spacing: 0.5px;
    text-transform: uppercase;
}
.welcome-stats {
    display: flex;
    justify-content: center;
    gap: 2rem;
    margin-top: 1rem;
    margin-bottom: 0.5rem;
}
.stat-item {
    text-align: center;
}
.stat-number {
    font-family: 'JetBrains Mono', monospace;
    font-size: 1.5rem;
    font-weight: 700;
    color: #059669;
}
.stat-label {
    font-size: 0.8rem;
    color: #9ca3af;
    margin-top: 0.1rem;
}

/* === SIDEBAR === */
section[data-testid="stSidebar"] {
    background-color: #f0fdf4;
}
section[data-testid="stSidebar"] .stMarkdown h3 {
    color: #059669;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.95rem;
}

/* === BUTTONS === */
.stButton > button[kind="primary"] {
    background: linear-gradient(135deg, #059669, #10B981) !important;
    color: white !important;
    border: none !important;
    font-weight: 600 !important;
    padding: 0.6rem 1.5rem !important;
    border-radius: 8px !important;
    font-size: 1rem !important;
    transition: all 0.2s ease !important;
}
.stButton > button[kind="primary"]:hover {
    background: linear-gradient(135deg, #047857, #059669) !important;
    transform: translateY(-1px) !important;
    box-shadow: 0 4px 12px rgba(5, 150, 105, 0.3) !important;
}

/* === DOWNLOAD BUTTONS === */
.stDownloadButton > button {
    border: 1px solid #d1fae5 !important;
    color: #059669 !important;
    font-weight: 600 !important;
    border-radius: 8px !important;
    transition: all 0.2s ease !important;
}
.stDownloadButton > button:hover {
    background-color: #ecfdf5 !important;
    border-color: #059669 !important;
}

/* === TEXT AREA === */
.stTextArea textarea {
    border-radius: 8px !important;
    border: 1px solid #d1d5db !important;
    font-family: 'DM Sans', sans-serif !important;
}
.stTextArea textarea:focus {
    border-color: #10B981 !important;
    box-shadow: 0 0 0 2px rgba(16, 185, 129, 0.15) !important;
}

/* === FOOTER === */
.footer {
    text-align: center;
    color: #9ca3af;
    font-size: 0.8rem;
    padding: 2rem 0 1rem 0;
    border-top: 1px solid #e5e7eb;
    margin-top: 3rem;
}
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

Exemples corrects SANS contexte :
- "Naviguer vers [URL DE LA PAGE DE CONNEXION — À DÉFINIR PAR LE TESTEUR]"
- "Cliquer sur le bouton [NOM DU BOUTON DE CONNEXION — À DÉFINIR PAR LE TESTEUR]"
- "Email de test : [À DÉFINIR PAR LE TESTEUR]"
- "Vérifier que le message d'erreur [MESSAGE EXACT — À DÉFINIR PAR LE TESTEUR] s'affiche"

Exemples INTERDITS sans contexte :
- "Naviguer vers https://www.monapp.com/login" ❌
- "Cliquer sur le bouton 'Se connecter'" ❌
- "Email de test : jean.dupont@email.com" ❌
- "L'application PixelConnect affiche..." ❌

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
- "Preconditions": les préconditions, chaque précondition sur une ligne séparée avec un numéro (1. xxx\\n2. xxx\\n3. xxx)
- "Test Steps": les étapes, CHAQUE ÉTAPE SUR UNE LIGNE SÉPARÉE avec un numéro (1. xxx\\n2. xxx\\n3. xxx). Utilise \\n pour séparer les lignes.
- "Expected Result": les résultats attendus, CHAQUE RÉSULTAT SUR UNE LIGNE SÉPARÉE avec un numéro (1. xxx\\n2. xxx). Utilise \\n pour séparer les lignes.
- "Priority": "Haute", "Moyenne" ou "Basse" (en français)

RÈGLES STRICTES :
- Retourne UNIQUEMENT le tableau JSON, rien d'autre
- Pas de texte avant ou après le JSON
- Pas de backticks ```json
- Pas de commentaires
- Le JSON doit être valide et parsable directement
- Garde les priorités en français : "Haute", "Moyenne", "Basse"
- Supprime tout formatage Markdown (**, ##, *, etc.) dans les valeurs
- IMPORTANT : utilise le caractère newline \\n entre chaque étape/résultat, PAS un espace ou un point-virgule
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
- Utilise les mots-clés Gherkin en ANGLAIS : Feature, Scenario, Given, When, Then, And, But
- Le contenu des étapes est en FRANÇAIS
- Chaque cas de test fonctionnel ET chaque cas limite devient un Scenario
- NE PAS inclure les risques — uniquement les cas de test
- Given = préconditions et état initial
- When = actions de l'utilisateur
- Then = résultats attendus et vérifications
- Utilise "And" pour les étapes supplémentaires dans chaque section
- Si des données sont marquées [À DÉFINIR PAR LE TESTEUR], garde-les telles quelles dans le Gherkin
- Pour les scénarios avec plusieurs jeux de données, utilise Scenario Outline avec Examples
- Pas de formatage Markdown — du texte brut Gherkin uniquement
- Sépare chaque Scenario par une ligne vide
"""

# --- Header ---
st.markdown("""
<div class="main-header">
    <div class="badge">✨ Propulsé par l'IA</div>
    <h1>🧪 QA Test Generator</h1>
    <p class="tagline">Transformez vos User Stories en cas de test complets en 30 secondes.</p>
    <div class="welcome-stats">
        <div class="stat-item">
            <div class="stat-number">4</div>
            <div class="stat-label">Formats d'export</div>
        </div>
        <div class="stat-item">
            <div class="stat-number">30s</div>
            <div class="stat-label">Temps de génération</div>
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
    st.markdown("### 🧪 QA Test Generator")
    st.markdown("---")
    st.markdown("### 📖 Comment ça marche")
    st.markdown("""
    1. Collez votre User Story
    2. *(Optionnel)* Ajoutez le contexte de votre app
    3. Cliquez sur **Générer**
    4. Exportez en Markdown, TXT, CSV Jira ou Gherkin
    """)

    st.markdown("---")
    st.markdown("### 💡 Exemple de User Story")
    st.code("""En tant qu'utilisateur,
je veux pouvoir réinitialiser
mon mot de passe via email,
afin de récupérer l'accès
à mon compte.""", language=None)

    st.markdown("---")
    st.markdown("### 💡 Exemple de contexte")
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
    st.markdown("### 📊 Exports disponibles")
    st.markdown("📄 Markdown · 📋 TXT · 📊 CSV Jira · 🥒 Gherkin")

# --- Helper: Convert JSON to CSV ---
def json_to_jira_csv(test_cases_json):
    """Convert parsed JSON test cases to CSV string for Jira import."""
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

# --- Main Inputs ---
st.markdown("#### 📋 Votre User Story")
user_story = st.text_area(
    "User Story",
    height=150,
    placeholder="En tant que [rôle], je veux [action], afin de [bénéfice]...\n\nVous pouvez aussi coller des critères d'acceptance, des règles métier, ou toute description fonctionnelle.",
    label_visibility="collapsed"
)

with st.expander("🏢 Contexte applicatif (optionnel — recommandé pour des tests plus précis)"):
    app_context = st.text_area(
        "Décrivez votre application",
        height=120,
        placeholder="Nom de l'app, type (web/mobile), URL, pages principales, rôles utilisateurs, règles métier, stack technique, contraintes spécifiques...\n\nPlus vous donnez de contexte, plus les cas de test seront précis et exécutables.",
        label_visibility="collapsed"
    )

# --- Generate Button ---
col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    generate = st.button("🚀 Générer les cas de test", use_container_width=True, type="primary")

# --- Generation Logic ---
if generate:
    if not api_key:
        st.error("⚠️ Configuration API manquante. Contactez l'administrateur.")
    elif not user_story.strip():
        st.error("⚠️ Collez une User Story pour commencer.")
    else:
        try:
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel(
                model_name="gemini-2.5-flash",
                system_instruction=SYSTEM_PROMPT
            )

            if app_context and app_context.strip():
                user_message = f"CONTEXTE APPLICATIF :\n{app_context}\n\n---\n\nUSER STORY À ANALYSER :\n{user_story}"
            else:
                user_message = f"AUCUN CONTEXTE APPLICATIF FOURNI. Tu DOIS utiliser [À DÉFINIR PAR LE TESTEUR] pour toute donnée spécifique à l'application (URLs, noms de boutons, noms de pages, emails, mots de passe, messages d'erreur, etc.). N'invente RIEN.\n\n---\n\nUSER STORY À ANALYSER :\n{user_story}"

            with st.spinner("🔄 Analyse de la User Story et génération des tests..."):
                response = model.generate_content(user_message)
                result = response.text

            st.session_state['result'] = result
            st.session_state['user_story'] = user_story
            st.session_state['app_context'] = app_context if app_context else ""

            with st.spinner("🔄 Préparation de l'export CSV Jira..."):
                try:
                    csv_model = genai.GenerativeModel(
                        model_name="gemini-2.5-flash",
                        system_instruction=CSV_CONVERSION_PROMPT
                    )
                    csv_response = csv_model.generate_content(
                        f"Convertis ces cas de test en JSON :\n\n{result}"
                    )
                    raw_json = csv_response.text.strip()
                    if raw_json.startswith("```"):
                        raw_json = raw_json.split("\n", 1)[1]
                    if raw_json.endswith("```"):
                        raw_json = raw_json.rsplit("```", 1)[0]
                    raw_json = raw_json.strip()
                    test_cases = json.loads(raw_json)
                    st.session_state['csv_data'] = json_to_jira_csv(test_cases)
                    st.session_state['csv_count'] = len(test_cases)
                except Exception:
                    st.session_state['csv_data'] = None
                    st.session_state['csv_count'] = 0

            with st.spinner("🔄 Génération des scénarios Gherkin / BDD..."):
                try:
                    gherkin_model = genai.GenerativeModel(
                        model_name="gemini-2.5-flash",
                        system_instruction=GHERKIN_CONVERSION_PROMPT
                    )
                    gherkin_response = gherkin_model.generate_content(
                        f"Convertis ces cas de test en scénarios Gherkin :\n\n{result}"
                    )
                    gherkin_text = gherkin_response.text.strip()
                    if gherkin_text.startswith("```"):
                        gherkin_text = gherkin_text.split("\n", 1)[1]
                    if gherkin_text.endswith("```"):
                        gherkin_text = gherkin_text.rsplit("```", 1)[0]
                    st.session_state['gherkin_data'] = gherkin_text.strip()
                except Exception:
                    st.session_state['gherkin_data'] = None

        except Exception as e:
            st.error(f"❌ Erreur : {str(e)}")

# --- Display results from session_state ---
if st.session_state.get('result'):
    result = st.session_state['result']
    us = st.session_state.get('user_story', '')
    ctx = st.session_state.get('app_context', '')

    st.markdown("---")

    # --- Results in tabs ---
    tab_results, tab_gherkin = st.tabs(["📊 Cas de test", "🥒 Gherkin / BDD"])

    with tab_results:
        st.markdown(result)

    with tab_gherkin:
        gherkin_data = st.session_state.get('gherkin_data')
        if gherkin_data:
            st.code(gherkin_data, language="gherkin")
        else:
            st.info("Gherkin non disponible pour cette génération.")

    # --- Export Options ---
    st.markdown("---")
    st.markdown("### 📥 Exporter les résultats")

    col_exp1, col_exp2, col_exp3, col_exp4 = st.columns(4)

    with col_exp1:
        export_header = f"# QA Test Generator — Résultats\n\n## User Story\n{us}"
        if ctx.strip():
            export_header += f"\n\n## Contexte applicatif\n{ctx}"
        markdown_content = f"{export_header}\n\n---\n\n{result}"
        st.download_button(
            label="📄 Markdown",
            data=markdown_content,
            file_name="test_cases.md",
            mime="text/markdown",
            use_container_width=True,
            key="dl_markdown"
        )

    with col_exp2:
        txt_header = f"User Story:\n{us}"
        if ctx.strip():
            txt_header += f"\n\nContexte applicatif:\n{ctx}"
        txt_content = f"{txt_header}\n\n---\n\n{result}"
        st.download_button(
            label="📋 TXT",
            data=txt_content,
            file_name="test_cases.txt",
            mime="text/plain",
            use_container_width=True,
            key="dl_txt"
        )

    with col_exp3:
        csv_data = st.session_state.get('csv_data')
        csv_count = st.session_state.get('csv_count', 0)
        if csv_data:
            st.download_button(
                label=f"📊 CSV Jira ({csv_count})",
                data=csv_data,
                file_name="test_cases_jira.csv",
                mime="text/csv",
                use_container_width=True,
                key="dl_csv"
            )
        else:
            st.warning("CSV indisponible")

    with col_exp4:
        gherkin_data = st.session_state.get('gherkin_data')
        if gherkin_data:
            st.download_button(
                label="🥒 Gherkin",
                data=gherkin_data,
                file_name="test_cases.feature",
                mime="text/plain",
                use_container_width=True,
                key="dl_gherkin"
            )
        else:
            st.warning("Gherkin indisponible")

# --- Footer ---
st.markdown("""
<div class="footer">
    QA Test Generator · Propulsé par l'IA · Fait avec ❤️ pour la communauté QA<br>
    <span style="font-size: 0.7rem; color: #d1d5db;">Un outil par Amadou FOFANA — Le Testeur Augmenté</span>
</div>
""", unsafe_allow_html=True)
