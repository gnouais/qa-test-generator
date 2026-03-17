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

Tu génères des cas de test CONCRETS et EXÉCUTABLES. Un testeur junior qui ne connaît pas l'application doit pouvoir exécuter chaque cas de test sans poser de question.

RÈGLES CRITIQUES :
- Chaque étape doit être SPÉCIFIQUE : pas de "cliquer sur le bouton (ou équivalent)" — précise le nom exact du bouton, de la page, du champ
- Si un contexte applicatif est fourni, utilise-le pour personnaliser les noms de pages, boutons, URLs, rôles
- Si aucun contexte n'est fourni, utilise des noms réalistes et cohérents (invente un contexte crédible plutôt que de rester vague)
- Si le contexte applicatif fournit des données (emails, URLs, identifiants), utilise-les dans les cas de test
- Si les données ne sont PAS fournies, NE LES INVENTE PAS. Indique clairement [À DÉFINIR PAR LE TESTEUR] pour chaque donnée manquante. Exemple : Email : [À DÉFINIR PAR LE TESTEUR], Mot de passe : [À DÉFINIR PAR LE TESTEUR]
- Ne génère JAMAIS de fausses données (emails fictifs, URLs inventées, identifiants imaginaires) sauf si le testeur les a explicitement fournis dans le contexte
- Chaque précondition doit décrire exactement comment atteindre l'état initial

À partir de la User Story (et du contexte applicatif si fourni), génère :

## 1. CAS DE TEST FONCTIONNELS
Pour chaque cas de test, fournis :
- **Titre** : nom court et clair
- **Préconditions** : état initial requis avec les étapes pour y arriver
- **Données de test** : valeurs concrètes à utiliser (emails, mots de passe, noms, etc.)
- **Étapes** : actions numérotées, spécifiques et détaillées
- **Résultat attendu** : ce qui doit se passer, avec les messages exacts si possible
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

# --- Header ---
st.markdown("""
<div class="main-header">
    <div class="badge">MVP — Phase 1</div>
    <h1>🧪 QA Test Generator</h1>
    <p>Collez une User Story → Obtenez vos cas de test en 30 secondes</p>
</div>
""", unsafe_allow_html=True)

# --- API Key (from secrets) ---
api_key = st.secrets.get("GEMINI_API_KEY", "")

with st.sidebar:
    st.markdown("### 📖 Comment ça marche")
    st.markdown("""
    1. Collez votre User Story
    2. *(Optionnel)* Ajoutez le contexte de votre app
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

# --- Main Inputs ---
user_story = st.text_area(
    "📋 Votre User Story",
    height=150,
    placeholder="En tant que [rôle], je veux [action], afin de [bénéfice]...\n\nVous pouvez aussi coller des critères d'acceptance, des règles métier, ou toute description fonctionnelle."
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

            # Build the user message with optional context
            user_message = f"Voici la User Story à analyser :\n\n{user_story}"
            if app_context and app_context.strip():
                user_message = f"CONTEXTE APPLICATIF :\n{app_context}\n\n---\n\nUSER STORY À ANALYSER :\n{user_story}"

            with st.spinner("🔄 Analyse de la User Story et génération des tests..."):
                response = model.generate_content(user_message)
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
                export_header = f"# QA Test Generator — Résultats\n\n## User Story\n{user_story}"
                if app_context and app_context.strip():
                    export_header += f"\n\n## Contexte applicatif\n{app_context}"
                markdown_content = f"{export_header}\n\n---\n\n{result}"
                st.download_button(
                    label="📄 Télécharger en Markdown",
                    data=markdown_content,
                    file_name="test_cases.md",
                    mime="text/markdown",
                    use_container_width=True
                )

            with col_exp2:
                # TXT export
                txt_header = f"User Story:\n{user_story}"
                if app_context and app_context.strip():
                    txt_header += f"\n\nContexte applicatif:\n{app_context}"
                csv_content = f"{txt_header}\n\n---\n\n{result}"
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

# --- Footer ---
st.markdown("""
<div class="footer">
    QA Test Generator — MVP Phase 1 · Propulsé par Google Gemini · Fait avec ❤️ pour la communauté QA
</div>
""", unsafe_allow_html=True)
