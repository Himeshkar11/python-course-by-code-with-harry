import pyttsx3

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

speak("Hello, I am Jarvis")
import pyttsx3

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

speak("Hello, I am Jarvis")
import datetime
import wikipedia
import pywhatkit

def run_jarvis():
    command = take_command()
    print(command)

    if "time" in command:
        time = datetime.datetime.now().strftime('%H:%M')
        speak("Current time is " + time)

    elif "who is" in command:
        person = command.replace("who is", "")
        info = wikipedia.summary(person, 1)
        speak(info)

    elif "play" in command:
        song = command.replace("play", "")
        speak("Playing " + song)
        pywhatkit.playonyt(song)
        while True:
    run_jarvis()