import speech_recognition as sr
import pyttsx3

# Initialize the speech recognizer
recognizer = sr.Recognizer()

# Initialize the text-to-speech engine
engine = pyttsx3.init()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio)
        print("You:", query)
        return query
    except sr.UnknownValueError:
        print("Sorry, I didn't understand that.")
        return ""
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        return ""

def speak(response):
    engine.say(response)
    engine.runAndWait()

def main():
    speak("Hello! I'm your Python voice assistant. How can I assist you today?")
    while True:
        user_input = listen().lower()
        
        if "hello" in user_input:
            speak("Hello there!")
        elif "how are you" in user_input:
            speak("I'm doing well, thank you!")
        elif "goodbye" in user_input or "bye" in user_input:
            speak("Goodbye! Have a great day!")
            break
        else:
            speak("Sorry, I didn't understand that.")

if __name__ == "__main__":
    main()
