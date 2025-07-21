import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser

# Initialize the text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Speed of speech

def speak(text):
    print(f"Jarvis: {text}")
    engine.say(text)
    engine.runAndWait()

def take_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)

    try:
        print("🔍 Recognizing...")
        command = recognizer.recognize_google(audio, language='en-in')
        print(f"✅ You said: {command}")
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that. Please say again.")
        return "None"
    except sr.RequestError:
        speak("Internet error.")
        return "None"
    return command.lower()

def wish_user():
    hour = datetime.datetime.now().hour
    if hour < 12:
        speak("Good morning!")
    elif hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("I am Jarvis. How can I help you today? You can give me commands one by one.")

def run_jarvis():
    wish_user()
    while True:
        command = take_command()
        if command == "None":
            continue

        # COMMANDS HANDLING
        elif 'wikipedia' in command:
            speak("Searching Wikipedia...")
            query = command.replace("wikipedia", "")
            try:
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                speak(results)
            except:
                speak("Sorry, no result found on Wikipedia.")

        elif 'open youtube' in command:
            speak("Opening YouTube")
            webbrowser.open("https://www.youtube.com")

        elif 'open google' in command:
            speak("Opening Google")
            webbrowser.open("https://www.google.com")

        elif 'time' in command:
            time_now = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The current time is {time_now}")

        elif 'exit' in command or 'stop' in command or 'quit' in command:
            speak("Goodbye! Have a great day.")
            break

        else:
            speak("Sorry, I didn't understand that command.")

# Start the assistant
run_jarvis()
