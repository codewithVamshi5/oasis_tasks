import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

# Initialize
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def get_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        try:
            command = r.recognize_google(audio)
            print("You said:", command)
            return command.lower()
        except:
            speak("Sorry, I didn't catch that.")
            return ""

def run_assistant():
    command = get_command()

    if 'hello' in command:
        speak("Hello! How can I help you?")
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        speak(f"The time is {time}")
    elif 'date' in command:
        date = datetime.datetime.now().strftime('%A, %B %d, %Y')
        speak(f"Today is {date}")
    elif 'search' in command:
        query = command.replace('search', '')
        url = f"https://www.google.com/search?q={query}"
        webbrowser.open(url)
        speak(f"Searching for {query}")
    else:
        speak("I am not sure how to help with that.")

# Run the assistant
run_assistant()
