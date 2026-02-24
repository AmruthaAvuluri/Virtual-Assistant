import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
import os
import wikipedia
import pyjokes
import requests

engine = pyttsx3.init()

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

def take_command():
    recognizer = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio, language="en-US")
        print("You said:", command)
        return command.lower()
    
    except:
        print("Sorry, I did not understand.")
        return ""

# Weather function (uses free API)
def get_weather(city):
    api_key = "your_api_key_here"   # we will fix this next
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    
    if data["cod"] != "404":
        temp = data["main"]["temp"]
        description = data["weather"][0]["description"]
        speak(f"The temperature is {temp} degree Celsius with {description}")
    else:
        speak("City not found")

speak("Hello, I am your advanced AI assistant. How can I help you?")

while True:
    command = take_command()

    if "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    elif "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak("The current time is " + current_time)

    elif "date" in command:
        today = datetime.datetime.now().strftime("%B %d, %Y")
        speak("Today's date is " + today)

    elif "open notepad" in command:
        speak("Opening Notepad")
        os.system("notepad")

    elif "wikipedia" in command:
        speak("Searching Wikipedia")
        query = command.replace("wikipedia", "")
        result = wikipedia.summary(query, sentences=2)
        speak(result)

    elif "joke" in command:
        joke = pyjokes.get_joke()
        speak(joke)

    elif "search" in command:
        speak("What should I search for?")
        query = take_command()
        webbrowser.open(f"https://www.google.com/search?q={query}")
        speak("Here are the search results")

    elif "calculate" in command:
        speak("Tell me the calculation")
        query = take_command()
        try:
            result = eval(query)
            speak(f"The answer is {result}")
        except:
            speak("Sorry, I cannot calculate that.")

    elif "weather" in command:
        speak("Tell me the city name")
        city = take_command()
        get_weather(city)

    elif "how are you" in command:
        speak("I am doing great!")

    elif "stop" in command or "exit" in command:
        speak("Goodbye!")
        break

    else:
        speak("Sorry, I don't know that command yet.")