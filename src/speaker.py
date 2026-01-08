from gtts import gTTS
from playsound import playsound
import tempfile
import os

LANG_CODES = {
    "english": "en",
    "tamil": "ta",
    "hindi": "hi",
    "malayalam": "ml",
    "german": "de"
}

def speak(text, lang="english"):
    try:
        tts = gTTS(text=text, lang=LANG_CODES[lang])
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
            filename = fp.name

        tts.save(filename)
        playsound(filename)
        os.remove(filename)

    except Exception as e:
        print("🔴 Audio error:", e)
