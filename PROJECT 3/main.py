import speech_recognition as sr
import webbrowser
import pyttsx3
import time
import musicLibrary
import requests

recognizer = sr.Recognizer()
engine = pyttsx3.init()

NEWS_API_KEY = "b8d5083df55643289af9b849e14e87dd"

def speak(text):
    engine.say(text)
    engine.runAndWait()

def getNews():
    speak("Fetching latest news")
    time.sleep(0.5)

    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={NEWS_API_KEY}"
    r = requests.get(url)

    if r.status_code != 200:
        speak("Unable to fetch news")
        return

    data = r.json()
    articles = data.get("articles", [])

    if not articles:
        speak("No news found")
        return

    for i, article in enumerate(articles[:5]):
        speak(f"News {i+1}")
        time.sleep(0.3)
        speak(article["title"])
        time.sleep(0.6)

def processCommand(command):
    command = command.lower()
    print("Executing:", command)

    if "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    elif "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif "open facebook" in command:
        speak("Opening Facebook")
        webbrowser.open("https://www.facebook.com")

    elif "open linkedin" in command:
        speak("Opening LinkedIn")
        webbrowser.open("https://www.linkedin.com")

    elif command.startswith("play"):
        song = command.replace("play", "").strip()

        if song in musicLibrary.music:
            speak(f"Playing {song}")
            webbrowser.open(musicLibrary.music[song])
        else:
            speak("Song not found")

    elif "news" in command:
        getNews()
  
    elif "jarvis" in command:
        question = command.replace("jarvis", "").strip()
        if question:
            askJarvisAI(question)
        else:
            speak("Yes, how can I help you?")

    else:
        pass
        

if __name__ == "__main__":
    speak("Jarvis initialized")

    with sr.Microphone() as source:
        print("Calibrating microphone...")
        recognizer.adjust_for_ambient_noise(source, duration=1)

    while True:
        print("Recognizing......")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=4)

            text = recognizer.recognize_google(audio).lower()
            print("Heard:", text)

            # ✅ ROUTE ALL COMMANDS
            if any(word in text for word in ["open", "play", "news"]):
                processCommand(text)

            elif "jarvis" in text:
                speak("Ya")

            time.sleep(0.5)

        except sr.UnknownValueError:
            print("Could not understand audio")

        except Exception as e:
            print("Error:", e)










# newsapi used