import streamlit as st
import google.generativeai as genai
import json
import time

# --- Page Config ---
st.set_page_config(
    page_title="QA Test Generator",
    page_icon="🧪",
    layout="wide"
)

# --- Custom CSS ---
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;600;700&family=DM+Sans:wght@400;500;600;700&display=swap');

/* Global */
.stApp {
    font-family: 'DM Sans', sans-serif;
}

/* Header */
.main-header {
    text-align: center;
    padding: 2rem 0 1rem 0;
}
.main-header h1 {
    font-family: 'JetBrains Mono', monospace;
    font-size: 2.2rem;
    font-weight: 700;
    color: #1a1a2e;
    margin-bottom: 0.3rem;
}
.main-header p {
    font-size: 1.1rem;
    color: #6b7280;
    margin-top: 0;
}
.badge {
    display: inline-block;
    background: #f0fdf4;
    color: #16a34a;
    font-size: 0.75rem;
    font-weight: 600;
    padding: 0.25rem 0.75rem;
    border-radius: 999px;
    border: 1px solid #bbf7d0;
    margin-bottom: 1rem;
}

/* Results sections */
.section-header {
    font-family: 'JetBrains Mono', monospace;
    font-size: 1rem;
    font-weight: 600;
    color: #1a1a2e;
    padding: 0.5rem 0;
    border-bottom: 2px solid #e5e7eb;
    margin: 1.5rem 0 0.75rem 0;
}
.test-case {
    background: #f8fafc;
    border-left: 3px solid #3b82f6;
    padding: 1rem;
    margin: 0.5rem 0;
    border-radius: 0 8px 8px 0;
    font-size: 0.9rem;
    line-height: 1.6;
}
.edge-case {
    background: #fff7ed;
    border-left: 3px solid #f97316;
    padding: 1rem;
    margin: 0.5rem 0;
    border-radius: 0 8px 8px 0;
    font-size: 0.9rem;
    line-height: 1.6;
}
.risk-item {
    background: #fef2f2;
    border-left: 3px solid #ef4444;
    padding: 1rem;
    margin: 0.5rem 0;
    border-radius: 0 8px 8px 0;
    font-size: 0.9rem;
    line-height: 1.6;
}
.case-title {
    font-weight: 600;
    color: #1e293b;
    margin-bottom: 0.25rem;
}
.case-detail {
    color: #475569;
}

/* Footer */
.footer {
    text-align: center;
    color: #9ca3af;
    font-size: 0.8rem;
    padding: 2rem 0 1rem 0;
    border-top: 1px solid #f3f4f6;
    margin-top: 3rem;
}
</style>
""", unsafe_allow_html=True)

# --- System Prompt ---
SYSTEM_PROMPT = """Tu es un expert QA senior avec 15 ans d'expérience en test logiciel.

À partir de la User Story fournie, tu dois générer :

## 1. CAS DE TEST FONCTIONNELS
Pour chaque cas de test, fournis :
- **Titre** : nom court et clair
- **Préconditions** : état initial requis
- **Étapes** : actions numérotées à exécuter
- **Résultat attendu** : ce qui doit se passer
- **Priorité** : Haute / Moyenne / Basse

## 2. CAS LIMITES (EDGE CASES)
Identifie les scénarios aux frontières :
- Valeurs limites (min, max, vide, null)
- Cas d'erreur et comportements inattendus
- Concurrence, timeout, données corrompues
- Pour chaque edge case : titre + description + résultat attendu

## 3. SUGGESTIONS DE RISQUES
Identifie les risques potentiels :
- Risques fonctionnels
- Risques de performance
- Risques de sécurité
- Risques d'intégration
- Pour chaque risque : titre + description + impact (Critique / Majeur / Mineur) + mitigation suggérée

RÈGLES :
- Sois exhaustif mais pertinent — pas de cas de test inutiles
- Adapte le niveau de détail à la complexité de la User Story
- Utilise un langage clair, compréhensible par un testeur junior
- Réponds en français sauf pour les termes techniques standards
- Structure ta réponse en Markdown clair avec les 3 sections ci-dessus
"""

# --- Header ---
st.markdown("""
<div class="main-header">
    <div class="badge">MVP — Phase 1</div>
    <h1>🧪 QA Test Generator</h1>
    <p>Collez une User Story → Obtenez vos cas de test en 30 secondes</p>
</div>
""", unsafe_allow_html=True)

# --- API Key ---
with st.sidebar:
    st.markdown("### ⚙️ Configuration")
    api_key = st.text_input(
        "Clé API Google Gemini",
        type="password",
        help="Obtenez votre clé gratuite sur aistudio.google.com"
    )

    st.markdown("---")
    st.markdown("### 📖 Comment ça marche")
    st.markdown("""
    1. Entrez votre clé API Gemini
    2. Collez votre User Story
    3. Cliquez sur **Générer**
    4. Copiez ou exportez les résultats
    """)

    st.markdown("---")
    st.markdown("### 💡 Exemple de User Story")
    st.code("""En tant qu'utilisateur,
je veux pouvoir réinitialiser
mon mot de passe via email,
afin de récupérer l'accès
à mon compte.""", language=None)

# --- Main Input ---
user_story = st.text_area(
    "📋 Votre User Story",
    height=150,
    placeholder="En tant que [rôle], je veux [action], afin de [bénéfice]...\n\nVous pouvez aussi coller des critères d'acceptance, des règles métier, ou toute description fonctionnelle."
)

# --- Generate Button ---
col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    generate = st.button("🚀 Générer les cas de test", use_container_width=True, type="primary")

# --- Generation Logic ---
if generate:
    if not api_key:
        st.error("⚠️ Entrez votre clé API Gemini dans la barre latérale.")
    elif not user_story.strip():
        st.error("⚠️ Collez une User Story pour commencer.")
    else:
        try:
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel(
                model_name="gemini-2.0-flash-lite",
                system_instruction=SYSTEM_PROMPT
            )

            with st.spinner("🔄 Analyse de la User Story et génération des tests..."):
                response = model.generate_content(
                    f"Voici la User Story à analyser :\n\n{user_story}"
                )
                result = response.text

            # Display results
            st.markdown("---")
            st.markdown("## 📊 Résultats")

            # Show the generated content
            st.markdown(result)

            # --- Export Options ---
            st.markdown("---")
            st.markdown("### 📥 Exporter")

            col_exp1, col_exp2 = st.columns(2)

            with col_exp1:
                # Markdown export
                markdown_content = f"# QA Test Generator — Résultats\n\n## User Story\n{user_story}\n\n---\n\n{result}"
                st.download_button(
                    label="📄 Télécharger en Markdown",
                    data=markdown_content,
                    file_name="test_cases.md",
                    mime="text/markdown",
                    use_container_width=True
                )

            with col_exp2:
                # CSV-like export
                csv_content = f"User Story:\n{user_story}\n\n---\n\n{result}"
                st.download_button(
                    label="📋 Télécharger en TXT",
                    data=csv_content,
                    file_name="test_cases.txt",
                    mime="text/plain",
                    use_container_width=True
                )

            # Store in session for copy
            st.session_state['last_result'] = result

        except Exception as e:
            st.error(f"❌ Erreur : {str(e)}")
            if "API_KEY" in str(e).upper() or "INVALID" in str(e).upper():
                st.info("💡 Vérifiez que votre clé API est correcte sur aistudio.google.com")

# --- Footer ---
st.markdown("""
<div class="footer">
    QA Test Generator — MVP Phase 1 · Propulsé par Google Gemini · Fait avec ❤️ pour la communauté QA
</div>
""", unsafe_allow_html=True)
