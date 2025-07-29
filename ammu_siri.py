import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import webbrowser
import os
import sys

# Initialize speech engine
engine = pyttsx3.init()

engine.setProperty('rate', 170)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Female voice

def talk(text):
    print("🎙 chintu:", text)
    engine.say(text)
    engine.runAndWait()

def take_command():
    listener = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎧 Listening...")
        listener.adjust_for_ambient_noise(source)
        voice = listener.listen(source)
    try:
        command = listener.recognize_google(voice)
        command = command.lower()
        print("🗣 You said:", command)
    except sr.UnknownValueError:
        talk("Sorry chintu, I didn’t catch that.")
        return ""
    except sr.RequestError:
        talk("Network issue with Google service.")
        return ""
    return command

def play_from_app(song, app="youtube"):
    if "spotify" in app:
        talk(f"Opening Spotify for {song} 🎵")
        webbrowser.open(f"https://open.spotify.com/search/{song}")
    elif "gaana" in app:
        talk(f"Opening Gaana for {song} 🎼")
        webbrowser.open(f"https://gaana.com/search/{song}")
    else:
        talk(f"Playing {song} on YouTube 🎶")
        pywhatkit.playonyt(song)

def run_chintu():
    talk("Yo bro! What do you want to do?")
    command = take_command()

    if "play" in command and "spotify" in command:
        song = command.replace("play", "").replace("from spotify", "").replace("on spotify", "").replace("spotify", "").strip()
        play_from_app(song, "spotify")

    elif "play" in command and "gaana" in command:
        song = command.replace("play", "").replace("from gaana", "").replace("on gaana", "").replace("gaana", "").strip()
        play_from_app(song, "gaana")

    elif "play" in command:
        song = command.replace("play", "").strip()
        play_from_app(song, "youtube")

    elif "time" in command:
        time_now = datetime.datetime.now().strftime('%I:%M %p')
        talk(f"It’s {time_now} ⏰")

    elif "who is" in command:
        person = command.replace("who is", "").strip()
        try:
            info = wikipedia.summary(person, sentences=1)
            talk(info)
        except:
            talk("Sorry, I couldn’t find information about that person.")

    elif "comedy" in command:
        talk("Here’s a comedy for you: Why did the computer show up at work late? It had a hard drive! 😂")

    elif "cartoon" in command:
        talk("Opening cartoons on YouTube 📺")
        webbrowser.open("https://www.youtube.com/results?search_query=cartoons")

    elif "open chrome" in command:
        chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
        if os.path.exists(chrome_path):
            talk("Opening Chrome 🚀")
            os.startfile(chrome_path)
        else:
            talk("Chrome path not found 😬")

    elif "open code" in command or "open vs code" in command:
        talk("Opening VS Code 💻")
        os.system("code")

    else:
        talk("I didn’t understand that 😅")

# ✅ Start assistant – only runs one command, then exits
talk("Yo! I'm CHINTU – your personal voice assistant 💡")
run_chintu()
