import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

# Initialize the recognizer
recognizer = sr.Recognizer()

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Function to make the assistant speak
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to recognize speech input from the microphone
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for background noise
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio)
        print(f"You said: {command}")
        return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, I did not understand that.")
        return None
    except sr.RequestError:
        speak("Sorry, my speech recognition service is down.")
        return None

# Function to handle voice commands
def handle_command(command):
    if 'time' in command:
        current_time = datetime.datetime.now().strftime('%I:%M %p')
        speak(f"The current time is {current_time}")
    elif 'open google' in command:
        speak("Opening Google")
        webbrowser.open('http://www.google.com')
    elif 'your name' in command:
        speak("I am your personal assistant.")
    else:
        speak("I am not sure how to respond to that.")

# Main function for the voice-controlled assistant
def personal_assistant():
    speak("Hello, how can I assist you today?")
    while True:
        command = listen()
        if command:
            if 'exit' in command or 'stop' in command:
                speak("Goodbye!")
                break
            handle_command(command)

if __name__ == "__main__":
    personal_assistant()
