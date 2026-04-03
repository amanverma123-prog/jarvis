import speech_recognition as sr
import pyttsx3
import webbrowser
import musicLibrary as ml
import requests
from dotenv import load_dotenv  
import os
from pathlib import Path

load_dotenv(dotenv_path=Path("C:/Users/HP/OneDrive/Desktop/Python/Mega Project 1/.env"))
newsApi = os.getenv("NEWS_API_KEY")

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    engine.stop()

def processCommand(c):
    if "open youtube" in c.lower().strip():
        print("opening youtube...")
        speak("opening youtube...")
        webbrowser.open("https://www.youtube.com")
    elif "open google" in c.lower().strip():
        print("opening google...")
        speak("opening google...")
        webbrowser.open("https://www.google.com")
    elif "open assistant" in c.lower().strip():
        print("opening chatgpt assistant...")
        speak("opening chatgpt assistant...")
        webbrowser.open("https://chat.openai.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = ml.music[song]
        print("playing song...")
        speak("playing song...")
        webbrowser.open(link)
    elif "news" in c.lower():    
        r = requests.get(f"https://newsapi.org/v2/everything?q=india&apiKey={newsApi}")
        if r.status_code == 200:
            data = r.json()
            articles = data["articles"]
            # Print the headlines
            for article in articles:
                print(article["title"])
                speak(article["title"])

if __name__ == "__main__":
    speak("Initializing Jarvis...")
    while True:
        r = sr.Recognizer()  
        try:
            with sr.Microphone() as source:
                print("Listening..")
                audio = r.listen(source, timeout = 2, phrase_time_limit = 1)
            word = r.recognize_google(audio)   
            # Listen for the wake word Jarvis
            if(word.lower() == "jarvis"):
                speak("yes sir")
                # Listen for the command
                with sr.Microphone() as source:
                    print("Jarvis Activated..")
                    audio = r.listen(source)
                    command = r.recognize_google(audio) 
                    processCommand(command)
        except Exception as e:
            print("Error; {0}".format(e))