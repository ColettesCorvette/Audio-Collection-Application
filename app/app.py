import streamlit as st
import datetime

st.title("Enregistrement de phrases")

# Accueil
if "step" not in st.session_state:
    st.session_state["step"] = 1

if st.session_state["step"] == 1:
    st.write("Bienvenue. Cliquez pour commencer une nouvelle session.")
    if st.button("Commencer"):
        st.session_state["step"] = 2

# Saisie infos démographiques
if st.session_state["step"] == 2:
    age = st.number_input("Âge", min_value=10, max_value=100)
    gender = st.selectbox("Genre", ["Homme", "Femme", "Autre"])
    consent = st.checkbox("J’accepte de participer (obligatoire)")
    if consent and st.button("Commencer l’enregistrement"):
        st.session_state["age"] = age
        st.session_state["gender"] = gender
        st.session_state["step"] = 3
        st.session_state["sentence_idx"] = 0

# Affichage phrases + enregistrement
if st.session_state["step"] == 3:
    # Liste de phrases
    sentences = ["Bonjour", "Comment ça va ?", "Il fait beau aujourd'hui."]
    idx = st.session_state["sentence_idx"]
    st.write(f"Phrase {idx+1}/{len(sentences)} : {sentences[idx]}")
    audio_data = st.audio_recorder("Enregistrez votre phrase")
    if st.button("Valider"):
        # Sauvegarder audio + infos dans le dossier recordings/
        # ... (code à compléter)
        if idx+1 < len(sentences):
            st.session_state["sentence_idx"] += 1
        else:
            st.session_state["step"] = 4

# Fin
if st.session_state["step"] == 4:
    st.write("Merci pour votre participation !")
    if st.button("Retour à l’accueil"):
        st.session_state["step"] = 1
