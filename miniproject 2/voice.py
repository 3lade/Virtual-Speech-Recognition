# Import necessary modules
import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os

# Initialize the text-to-speech module
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# Define a function to speak the given text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Define a function to recognize speech
def recognize_speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-us')
        print(f"You said: {query}\n")
    except Exception as e:
        print("Sorry, I didn't understand. Please try again.")
        return "None"
    return query

# Greet the user and ask for their name
speak("Hello! I am your virtual assistant. What should I call you?")
name = recognize_speech()
speak(f"Hello, {name}. How can I assist you today?")

# Define a function to handle voice commands
def handle_command(command):
    if 'wikipedia' in command:
        speak('Searching Wikipedia...')
        command = command.replace("wikipedia", "")
        results = wikipedia.summary(command, sentences=2)
        speak("According to Wikipedia")
        speak(results)
    elif 'open youtube' in command:
        speak("Opening YouTube...")
        webbrowser.open("youtube.com")
    elif 'open google' in command:
        speak("Opening Google...")
        webbrowser.open("google.com")
    elif 'play music' in command:
        music_dir = 'C:/Users/Public/Music/Sample Music'
        songs = os.listdir(music_dir)
        os.startfile(os.path.join(music_dir, songs[0]))
    elif 'the time' in command:
        time = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The time is {time}")
    elif 'open code' in command:
        speak("Opening Visual Studio Code...")
        code_path = "C:\\Program Files\\Microsoft VS Code\\Code.exe"
        os.startfile(code_path)
    elif 'shutdown' in command:
        speak("Shutting down...")
        os.system("shutdown /s /t 1")
    else:
        speak("I'm sorry, I don't know how to do that.")

# Start the voice assistant
while True:
    command = recognize_speech().lower()
    if 'exit' in command:
        speak("Goodbye!")
        break
    handle_command(command)