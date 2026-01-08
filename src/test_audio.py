from gtts import gTTS
from playsound import playsound
import tempfile
import os

tts = gTTS("Audio test working", lang="en")

with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
    filename = fp.name

tts.save(filename)
playsound(filename)
os.remove(filename)

print("✅ Audio played")
