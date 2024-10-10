import pyttsx3
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
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again, please...\n")
        return "None"
    return query

def play_music():
    music_dir = "P:\\music(p)\\Facourite"
    if os.path.exists(music_dir):
        songs = os.listdir(music_dir)
        random_song = random.choice(songs)
        os.startfile(os.path.join(music_dir, random_song))
    else:
        speak("Music directory not found!")

def system_control(command):
    if command == "shutdown":
        speak("Shutting down the system.")
        os.system("shutdown /s /t 1")
    elif command == "restart":
        speak("Restarting the system.")
        os.system("shutdown /r /t 1")
    elif command == "sleep":
        speak("Putting the system in sleep mode.")
        os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

def conversation(command):
    if command == "your name":
        speak("My name is Jarvis.")
    elif command == "can you do":
        say = ("""I can perform the following tasks:
    1. Search for information on Wikipedia.
    2. Open websites like YouTube, Google, and Instagram.
    3. Play music from your system.
    4. Tell you the current time and date.
    5. Open applications like Visual Studio Code.
    6. Shut down, restart, or put the system to sleep.""")
    print(say)
    speak(say)
    
def main():
    wishMe()
    while True:
        query = takeCommand().lower()
        
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
            
        elif "your name" in query:
            conversation("your name")    
        elif "can you do" in query:
            conversation("can you do")   
            
        elif "open youtube" in query:
            webbrowser.open("youtube.com")
        elif "open google" in query:
            webbrowser.open("google.com")
        elif "open instagram" in query:
            webbrowser.open("instagram.com")
        elif "play music" in query or "play a song" in query:
            play_music()
        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
        elif "the date" in query or "date" in query:
            strDate = datetime.datetime.now().strftime("%d/%m/%Y")
            speak(f"Sir, the date is {strDate}")
        elif "open vs code" in query or "open code" in query:
            code_path = "C:\\Users\\ASUS\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(code_path)
                
        elif 'shutdown' in query:
            system_control("shutdown")
        elif 'restart' in query:
            system_control("restart")
        elif 'sleep' in query:
            system_control("sleep")    
            
        elif 'exit' in query or 'quit' in query:
            speak("Goodbye Sir!")
            break
        else:
            speak("I didn't understand that. Can you please repeat?")

if __name__ == "__main__":
    main()
