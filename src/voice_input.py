import speech_recognition as sr

recognizer = sr.Recognizer()

def listen():
    print("[VOICE] Listening...")
    try:
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            audio = recognizer.listen(source)

        text = recognizer.recognize_google(audio)
        text = text.lower()
        print(f"[VOICE] Heard: {text}")
        return text

    except sr.UnknownValueError:
        print("[VOICE] Could not understand audio")
        return ""

    except sr.RequestError as e:
        print(f"[VOICE] API error: {e}")
        return ""

    except Exception as e:
        print(f"[VOICE] Error: {e}")
        return ""

