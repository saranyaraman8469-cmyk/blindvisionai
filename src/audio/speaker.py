import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 160)

def speak(text, lang="english"):
    print("[SPEAK]:", text)
    engine.say(text)
    engine.runAndWait()
