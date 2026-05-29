import streamlit as st
import matplotlib.pyplot as plt

from mood_analyzer import detect_mood, generate_notes
from beat_generator import create_beat


# Page Config
st.set_page_config(
    page_title="AI Music Generator",
    page_icon="🎵",
    layout="centered"
)


# Title
st.markdown(
    """
    <h1 style='text-align:center;color:#8A2BE2;'>
    🎵 AI Music Beat Generator
    </h1>
    """,
    unsafe_allow_html=True
)


# Lyrics Input
lyrics = st.text_area(
    "Enter Lyrics"
)


# Empty Lyrics Protection
if lyrics.strip() == "":

    st.warning(
        "Please enter lyrics to generate music"
    )

    st.stop()


# Mood Selection
mood_option = st.selectbox(
    "Mood",
    [
        "Auto Detect",
        "Happy",
        "Sad",
        "Energetic",
        "Chill"
    ]
)


# Genre Selection
genre = st.selectbox(
    "Genre",
    [
        "Lofi",
        "Rap",
        "EDM",
        "Pop"
    ]
)


# Instrument Selection
instrument = st.selectbox(
    "Instrument",
    [
        "Piano",
        "Guitar",
        "Synth",
        "Violin"
    ]
)


# BPM Slider
bpm = st.slider(
    "Tempo BPM",
    60,
    180,
    100
)


# Volume Slider
volume = st.slider(
    "Volume",
    20,
    127,
    90
)


# Mood Detection
if mood_option == "Auto Detect":

    mood = detect_mood(
        lyrics
    )

else:

    mood = mood_option


# Generate Notes
notes = generate_notes(
    mood
)


# Beat Timeline
st.markdown(
    "## 🥁 Beat Timeline Editor"
)

kick = []
snare = []
hihat = []

col1, col2, col3, col4 = st.columns(4)


# Column 1
with col1:

    kick.append(
        st.checkbox("Kick 1")
    )

    snare.append(
        st.checkbox("Snare 1")
    )

    hihat.append(
        st.checkbox("HiHat 1")
    )


# Column 2
with col2:

    kick.append(
        st.checkbox("Kick 2")
    )

    snare.append(
        st.checkbox("Snare 2")
    )

    hihat.append(
        st.checkbox("HiHat 2")
    )


# Column 3
with col3:

    kick.append(
        st.checkbox("Kick 3")
    )

    snare.append(
        st.checkbox("Snare 3")
    )

    hihat.append(
        st.checkbox("HiHat 3")
    )


# Column 4
with col4:

    kick.append(
        st.checkbox("Kick 4")
    )

    snare.append(
        st.checkbox("Snare 4")
    )

    hihat.append(
        st.checkbox("HiHat 4")
    )


# Generate Beat Button
if st.button(
    "🎶 Generate Beat"
):

    midi_file, wav_file = create_beat(
        mood,
        genre,
        bpm,
        notes,
        volume,
        instrument,
        kick,
        snare,
        hihat
    )

    # Success Message
    st.success(
        f"Music generated successfully! Mood: {mood}"
    )


    # Mood Effects
    if mood == "Happy":

        st.balloons()

    elif mood == "Energetic":

        st.snow()


    # Beat Details
    st.markdown(
        "## 🎼 Beat Information"
    )

    st.write(
        f"🎭 Mood: {mood}"
    )

    st.write(
        f"🎧 Genre: {genre}"
    )

    st.write(
        f"🎹 Instrument: {instrument}"
    )

    st.write(
        f"⚡ BPM: {bpm}"
    )

    st.write(
        f"🎵 AI Notes: {notes}"
    )

    st.write(
        f"🥁 Kick Pattern: {kick}"
    )

    st.write(
        f"🥁 Snare Pattern: {snare}"
    )

    st.write(
        f"🥁 HiHat Pattern: {hihat}"
    )


    # Audio Player
    st.markdown(
        "## 🔊 Audio Preview"
    )

    st.audio(
        wav_file
    )


    # Melody Visualization
    st.markdown(
        "## 📈 AI Melody Visualization"
    )

    fig, ax = plt.subplots()

    ax.plot(
        notes,
        marker='o'
    )

    ax.set_title(
        "AI Generated Melody"
    )

    ax.set_xlabel(
        "Step"
    )

    ax.set_ylabel(
        "MIDI Note"
    )

    st.pyplot(
        fig
    )


    # Download MIDI
    st.markdown(
        "## ⬇ Download Beat"
    )

    with open(
        midi_file,
        "rb"
    ) as f:

        st.download_button(
            "Download MIDI Beat",
            f,
            file_name="beat.mid"
        )