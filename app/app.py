import streamlit as st
from st_audiorec import st_audiorec
from pathlib import Path

# Titre onglet
st.set_page_config(
    page_title="Collecte Audio Anonyme",
    page_icon="🎙️",
    layout="centered",
)

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
    sentences = ["Bonjour", "Comment ça va ?", "Il fait beau aujourd'hui."]
    idx = st.session_state["sentence_idx"]
    st.write(f"Phrase {idx+1}/{len(sentences)} : {sentences[idx]}")

    audio_data = st_audiorec()

    if st.button("Valider") and audio_data is not None:
        age = st.session_state["age"]
        gender = st.session_state["gender"]
        idx = st.session_state["sentence_idx"]
        Path("recordings").mkdir(exist_ok=True)
        out_path = Path("recordings") / f"{age}_{gender}_phrase{idx+1}.wav"
        with open(out_path, "wb") as f:
            f.write(audio_data)
        # Passage à la phrase suivante ou fin
        if idx + 1 < len(sentences):
            st.session_state["sentence_idx"] += 1
        else:
            st.session_state["step"] = 4

    if audio_data is not None:
        st.audio(audio_data, format="audio/wav")

# Fin
if st.session_state["step"] == 4:
    st.write("Merci pour votre participation !")
    if st.button("Retour à l’accueil"):
        st.session_state["step"] = 1
