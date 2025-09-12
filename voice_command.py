import speech_recognition as sr
import pyttsx3
import webbrowser

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen_for_voice_commands():
    recognizer = sr.Recognizer()
    recognizer.energy_threshold = 300  # set fixed energy threshold (adjust if needed)
    recognizer.dynamic_energy_adjustment_ratio = 0.1  # reduce dynamic adjustment

    with sr.Microphone() as source:
        print("Listening for voice command...")
        # Comment out or remove this to skip ambient noise adjustment
        # recognizer.adjust_for_ambient_noise(source, duration=0.1)
        
        print("You can speak now...")
        audio = recognizer.listen(source)

        try:
            command = recognizer.recognize_google(audio)
            print("You said:", command)
            command = command.lower()

            if "open youtube" in command:
                speak("Opening YouTube")
                webbrowser.open("https://www.youtube.com")
            elif "open google" in command:
                speak("Opening Google")
                webbrowser.open("https://www.google.com")
            elif "open wikipedia" in command:
                speak("Opening Wikipedia")
                webbrowser.open("https://www.wikipedia.org")
            elif "open github" in command:
                speak("Opening GitHub")
                webbrowser.open("https://www.github.com")
            elif "search" in command:
                query = command.split("search", 1)[-1].strip()
                speak(f"Searching for {query}")
                webbrowser.open(f"https://www.google.com/search?q={query}")
            else:
                speak("Sorry, I didn't understand that command.")
                print("Sorry, I didn't understand that command.")

        except sr.UnknownValueError:
            speak("Sorry, I couldn't understand the audio.")
            print("Error: Could not understand the audio")
        except sr.RequestError:
            speak("Could not request results from Google.")
            print("Error: Could not request results from Google.")
        except Exception as e:
            speak(f"An error occurred: {str(e)}")
            print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    listen_for_voice_commands()
