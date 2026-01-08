import time
import cv2

from speaker import speak
from camera import start_camera, show_camera, stop_camera
from commands import COMMAND_TEXT
from voice_input import listen

# ---------------- SYSTEM START ----------------
print("[SYSTEM] BlindVisionAI starting")
speak("Blind Vision AI starting", "english")

# ---------------- VOICE-BASED LANGUAGE SELECTION ----------------
print("[SYSTEM] Please say your preferred language")
print("Say: English, Tamil, Malayalam, Hindi, or German")

LANGUAGE_MAP = {
    "english": "english",
    "tamil": "tamil",
    "malayalam": "malayalam",
    "hindi": "hindi",
    "german": "german"
}

lang = ""

while lang == "":
    spoken = listen()
    print("[VOICE] Heard:", spoken)

    for key in LANGUAGE_MAP:
        if key in spoken:
            lang = LANGUAGE_MAP[key]
            break

    if lang == "":
        speak("Please say the language again", "english")

print(f"[SYSTEM] Language selected: {lang.upper()}")
speak("Language selected", lang)

# ---------------- CAMERA START ----------------
speak("Camera will start now", lang)

cap = start_camera()
if cap is None:
    speak("Camera failed to start", lang)
    exit()

speak("Camera started. Monitoring surroundings.", lang)

# ---------------- DEMO COMMAND SEQUENCE ----------------
COMMAND_SEQUENCE = [
    "PATH CLEAR",
    "NO MOTION",
    "MOVE LEFT",
    "MOVE RIGHT",
    "MOVE FORWARD",
    "MOVE BACKWARD",
    "STOP"
]

# ---------------- MAIN LOOP ----------------
try:
    while True:
        show_camera(cap)

        for command in COMMAND_SEQUENCE:
            print("[COMMAND]", command)
            speak(COMMAND_TEXT[command][lang], lang)

            if command == "STOP":
                raise KeyboardInterrupt

            time.sleep(3)

except KeyboardInterrupt:
    pass

# ---------------- SHUTDOWN ----------------
speak("Navigation stopped", lang)
stop_camera(cap)
cv2.destroyAllWindows()
