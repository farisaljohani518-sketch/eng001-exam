#!/usr/bin/env python3
"""
Offline Audio Generator for ENG001 Platform using ElevenLabs API.
Run this script on your computer:
python generate_audio_mp3s.py
It will download all MP3 files into the audio/ folder for instant playback.
"""
import os
import json
import urllib.request
import urllib.error

API_KEY = "sk_5c26d519055085833ff478d1f2d178ad45daf979e9dd7b3d"
VOICE_ID = "21m00Tcm4TlvDq8ikWAM" # Rachel (Academic Instructor)
MODEL_ID = "eleven_multilingual_v2"

TRACKS = [
    {
        "filename": "track1.mp3",
        "text": "Good morning, everyone. My name is Tariq, and I study at Yanbu Industrial College. On weekdays, my alarm rings at 6:15 a.m. I usually eat a quick breakfast with my roommate, and our first English lecture starts at 8:00 a.m. sharp in Building 4. In the afternoon, I spend two hours in the library studying, before going to the college gym."
    },
    {
        "filename": "track2.mp3",
        "text": "Welcome to the new student orientation. The central library is located on the second floor, directly opposite the computer lab. All students must carry their digital student ID cards at all times. Remember, eating food inside the lecture halls is strictly forbidden. If you need campus directions, the main information desk is open until 4:00 p.m."
    },
    {
        "filename": "track3.mp3",
        "text": "Attention passengers on the Yanbu coastal shuttle bus. Our trip to the historic waterfront takes exactly twenty-five minutes. You should fasten your seat belts while the vehicle is in motion. The weather today is sunny and mild, with a temperature of 24 degrees Celsius. The return bus departs at 7:30 p.m."
    }
]

os.makedirs("audio", exist_ok=True)
url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}?output_format=mp3_44100_128"

print("Starting generation of academic studio audio files via ElevenLabs...")
for track in TRACKS:
    filepath = os.path.join("audio", track["filename"])
    print(f"Generating {track['filename']}...")
    payload = {
        "text": track["text"],
        "model_id": MODEL_ID,
        "voice_settings": {
            "stability": 0.48,
            "similarity_boost": 0.82,
            "style": 0.20,
            "use_speaker_boost": True
        }
    }
    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Accept": "audio/mpeg",
            "Content-Type": "application/json",
            "xi-api-key": API_KEY
        },
        method="POST"
    )
    try:
        with urllib.request.urlopen(req) as resp:
            with open(filepath, "wb") as f:
                f.write(resp.read())
        print(f" Saved: {filepath} ({os.path.getsize(filepath)} bytes)")
    except urllib.error.HTTPError as e:
        print(f"❌ Error generating {track['filename']}: HTTP {e.code} - {e.read().decode('utf-8')}")
    except Exception as e:
        print(f"❌ Network error: {e}")

print("Done! Place the audio/ folder in your GitHub repository.")
