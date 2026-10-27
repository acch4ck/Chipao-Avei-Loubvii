import sys
import os
import json

# Ensure scripts/hymn_builder exists
os.makedirs("scripts/hymn_builder", exist_ok=True)

# Helper to calculate frequency from key
KEY_PITCH = {
    "C": 261.63, "C#": 277.18, "Db": 277.18,
    "D": 293.66, "D#": 311.13, "Eb": 311.13,
    "E": 329.63,
    "F": 349.23, "F#": 369.99,
    "G": 392.00, "G#": 415.30, "Ab": 415.30,
    "A": 440.00, "A#": 466.16, "Bb": 466.16,
    "B": 493.88
}

def parse_key_pitch(key_sig):
    if not key_sig:
        return 440.0, "A"
    clean = key_sig.replace("Doh is", "").replace("Doh Is", "").strip()
    return KEY_PITCH.get(clean, 440.0), clean

print("Generator script loaded")
