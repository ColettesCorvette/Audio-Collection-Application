import streamlit as st
from st_audiorec import st_audiorec
from pathlib import Path
import random

# Titre onglet
st.set_page_config(
    page_title="Collecte Audio Anonyme",
    page_icon="🎙️",
    layout="centered",
)

st.title("Enregistrement de phrases")

# Initialisation de l'étape
if "step" not in st.session_state:
    st.session_state["step"] = 1

# Accueil
if st.session_state["step"] == 1:
    st.write("Bienvenue. Cliquez pour commencer une nouvelle session.")
    if st.button("Commencer"):
        st.session_state["step"] = 2

# Saisie infos démographiques + choix du nombre de phrases + sélection aléatoire
if st.session_state["step"] == 2:
    # Charger les phrases
    sentences_file = Path(__file__).parent.parent / "sentences.txt"
    try:
        with open(sentences_file, "r", encoding="utf-8") as f:
            all_sentences = [line.strip() for line in f if line.strip()]
    except Exception as e:
        st.error(f"Erreur lors de la lecture des phrases : {e}")
        all_sentences = []
    max_phrases = len(all_sentences)
    if max_phrases == 0:
        st.error("Aucune phrase disponible. Merci de remplir sentences.txt.")
    else:
        age = st.number_input("Âge", min_value=10, max_value=100)
        gender = st.selectbox("Genre", ["Homme", "Femme", "Autre"])
        consent = st.checkbox("J’accepte de participer (obligatoire)")
        nb_phrases = st.slider(
            "Nombre de phrases à enregistrer :",
            min_value=1, max_value=max_phrases, value=min(5, max_phrases)
        )
        if consent and st.button("Commencer l’enregistrement"):
            st.session_state["age"] = age
            st.session_state["gender"] = gender
            st.session_state["nb_phrases"] = nb_phrases
            st.session_state["sentence_idx"] = 0
            st.session_state["selected_sentences"] = random.sample(all_sentences, nb_phrases)
            st.session_state["step"] = 3

# Affichage phrases aléatoires + enregistrement
if st.session_state["step"] == 3:
    sentences = st.session_state["selected_sentences"]
    idx = st.session_state["sentence_idx"]
    st.write(f"Phrase {idx+1}/{len(sentences)} : {sentences[idx]}")

    audio_data = st_audiorec()

    if st.button("Valider") and audio_data is not None:
        age = st.session_state["age"]
        gender = st.session_state["gender"]
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
        for key in ["step", "age", "gender", "nb_phrases", "sentence_idx", "selected_sentences"]:
            if key in st.session_state:
                del st.session_state[key]
