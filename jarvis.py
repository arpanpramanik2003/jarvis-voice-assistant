import pyttsx3  # Text to speech conversion
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    
    speak("I am Jarvis! Please tell me how may I help you!")

def takeCommand():
    # It takes microphone input and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:  # Corrected usage of sr.Microphone
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')  # Corrected the variable name
        print(f"User said: {query}\n")
    except Exception as e:
        # print(e)  # Uncomment to see the error for debugging if needed
        print("Say that again, please...\n")
        return "None"
    
    return query

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif "open youtube" in query:
            webbrowser.open("youtube.com")
        elif "open google" in query:
            webbrowser.open("google.com")
        elif "open instagram" in query:
            webbrowser.open("instagram.com")
        
        elif "play music" in query:
            music_dir = "P:\\music(p)\Facourite"
            songs = os.listdir(music_dir)
            print(songs)
            random_song = random.choice(songs)
            os.startfile(os.path.join(music_dir,random_song))
        
        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the date is {strTime}")
        elif ("the date" or "date") in query:
            strDate = datetime.datetime.now().strftime("%d/%m/%Y")
            speak(f"Sir, the date is {strDate}")
        
        elif "open vs code" or "open code" in query:
              code_path = "C:\\Users\\ASUS\\AppData\\Local\\Programs\Microsoft VS Code\\Code.exe"
              os.startfile(code_path)
        
                  