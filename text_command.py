# text_command.py
import pyttsx3
import webbrowser

# Initialize Text-to-Speech engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def text_based_interaction(command):
    command = command.lower().strip()
    
    # Basic conversational responses
    if "hello" in command:
        response = "Hello! How can I assist you today?"
    
    elif "how are you" in command:
        response = "I'm doing great, thank you for asking!"
    
    # Specific commands for known sites
    elif command == "open google":
        response = "Opening Google"
        webbrowser.open("https://www.google.com")

    elif command == "open youtube":
        response = "Opening YouTube"
        webbrowser.open("https://www.youtube.com")

    elif command == "open github":
        response = "Opening GitHub"
        webbrowser.open("https://www.github.com")

    elif command == "open wikipedia":
        response = "Opening Wikipedia"
        webbrowser.open("https://www.wikipedia.org")

    # General open command for other websites
    elif command.startswith("open "):
        site = command.split("open ")[1].strip()
        response = f"Opening {site}"
        webbrowser.open(f"https://{site}.com")
    
    # Search query
    elif command.startswith("search "):
        query = command.split("search ")[1].strip()
        response = f"Searching for {query}"
        webbrowser.open(f"https://www.google.com/search?q={query}")
    
    else:
        response = "Sorry, I didn't understand that."

    # Speak the response
    speak(response)
    return response

# Main CLI for testing
if __name__ == "__main__":
    print("Text-based chatbot activated!")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        response = text_based_interaction(user_input)
        print("Bot:", response)
