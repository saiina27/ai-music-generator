# AI Music Generator 🎵

AI Music Generator is a Python-based application that generates music beats from lyrics provided by the user. The application analyzes the mood of the lyrics and creates a custom beat based on selected genre, instrument, BPM, and beat patterns.

## Features

* Lyrics-based mood detection
* AI-generated melody notes
* Genre selection (Lofi, Rap, EDM, Pop)
* Instrument selection
* BPM (Tempo) control
* Volume control
* Beat Timeline Editor

  * Kick
  * Snare
  * HiHat
* MIDI beat generation
* Audio preview
* Download generated beat

## Tech Stack

* Python
* Streamlit
* TextBlob
* MIDIUtil
* NLTK

## Project Structure

ai_music_generator/

├── app.py

├── beat_generator.py

├── mood_analyzer.py

├── README.md

└── requirements.txt

## Installation

Clone the repository:

git clone https://github.com/saiina27/ai-music-generator.git

cd ai-music-generator

Create a virtual environment:

python3 -m venv venv

source venv/bin/activate

Install dependencies:

pip install -r requirements.txt

Run the application:

streamlit run app.py

## How It Works

1. Enter song lyrics.
2. Select mood manually or use Auto Detect.
3. Choose genre and instrument.
4. Adjust BPM and volume.
5. Create beat patterns using Kick, Snare, and HiHat controls.
6. Generate the beat.
7. Preview and download the generated music.

LIVE DEMO-https://ai-music-generator-bxhunualm8fnjqbvckrbww.streamlit.app/


## Future Improvements

* Advanced AI melody generation
* MP3 export support
* More instruments and genres
* Beat visualization
* Cloud deployment

## Author

Saina Yadav

B.Tech, Amity University Gurgaon

Graduation Year: 2026
