import speech_recognition as sr
import os


r = sr.Recognizer()


with sr.Microphone() as source:
    print("Speak now")
    audio = r.listen(source)
    try:
        
        command = r.recognize_google(audio)
        print(f"Your command: {command}")
        if command == "execute dnscan":
            os.system(r 'C:\Users\Durvesh\Dropbox\My PC (LAPTOP-1K31VN3D)\Documents\Data Science Project\A.I asistant\J.A.R.V.I.S\LOKI\dnscan\dnscan.py')
    except sr.UnknownValueError:
        print("Could not recognize speech")
    except sr.RequestError as e:
        print(f"Error: {e}")
