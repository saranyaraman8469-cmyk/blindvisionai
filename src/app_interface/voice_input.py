import speech_recognition as sr

def listen_language():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say language (Tamil / English / Hindi / Malayalam / German)")
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio).lower()
        print("You said:", text)
        return "english"
    except:
        return "english"
