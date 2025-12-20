import pyttsx3

def speak(message):
    engine = pyttsx3.init()
    engine.say(message)
    engine.runAndWait()

if __name__ == "__main__":
    speak("Obstacle ahead. Please turn left.")
