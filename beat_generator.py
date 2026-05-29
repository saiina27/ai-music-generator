from midiutil import MIDIFile
import numpy as np
from scipy.io.wavfile import write


def create_beat(
    mood,
    genre,
    bpm,
    notes,
    volume,
    instrument,
    kick,
    snare,
    hihat
):

    music = MIDIFile(3)

    track = 0
    time_pos = 0

    instruments = {
        "Piano": 0,
        "Guitar": 24,
        "Synth": 81,
        "Violin": 40
    }

    # Track Name
    music.addTrackName(
        track,
        time_pos,
        "Beat"
    )

    # Tempo
    music.addTempo(
        track,
        time_pos,
        bpm
    )

    # Instrument
    music.addProgramChange(
        track,
        0,
        time_pos,
        instruments[instrument]
    )

    # Melody Notes
    for i, note in enumerate(notes):

        music.addNote(
            track,
            0,
            note,
            i,
            1,
            volume
        )

    # Kick Drum
    for i, active in enumerate(kick):

        if active:

            music.addNote(
                1,
                9,
                36,
                i,
                0.5,
                volume
            )

    # Snare Drum
    for i, active in enumerate(snare):

        if active:

            music.addNote(
                2,
                9,
                38,
                i,
                0.5,
                volume
            )

    # HiHat
    for i, active in enumerate(hihat):

        if active:

            music.addNote(
                2,
                9,
                42,
                i,
                0.25,
                volume
            )

    # Save MIDI File
    with open(
        "beat.mid",
        "wb"
    ) as output:

        music.writeFile(output)

    # -----------------------------
    # WAV AUDIO GENERATION
    # -----------------------------

    sample_rate = 44100
    duration = 4

    t = np.linspace(
        0,
        duration,
        sample_rate * duration
    )

    audio = np.zeros_like(t)

    # Melody Sound
    for i, note in enumerate(notes):

        freq = 440 * (2 ** ((note - 69) / 12))

        start = int(i * sample_rate * 0.5)

        end = start + int(sample_rate * 0.5)

        wave_data = 0.3 * np.sin(
            2 * np.pi *
            freq *
            t[:end-start]
        )

        audio[start:end] += wave_data

    # Normalize Audio
    if np.max(np.abs(audio)) != 0:

        audio = np.int16(
            audio / np.max(np.abs(audio)) * 32767
        )

    else:

        audio = np.int16(audio)

    # Save WAV File
    write(
        "beat.wav",
        sample_rate,
        audio
    )

    return "beat.mid", "beat.wav"