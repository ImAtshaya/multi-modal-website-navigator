import tkinter as tk
from tkinter import messagebox
import subprocess
import threading
import webbrowser  # ✅ Added to fix NameError

# Function to handle gesture command
def run_gesture_command():
    def target():
        print("Gesture recognition started...")
        subprocess.run(["python", "gesture_command.py"])
    threading.Thread(target=target).start()

# Function to handle voice command
def run_voice_command():
    def target():
        print("Voice recognition started...")
        subprocess.run(["python", "voice_command.py"])
    threading.Thread(target=target).start()

# Function to handle text command
def process_text_input():
    user_input = text_entry.get()
    print(f"Text input: {user_input}")
    if "open" in user_input:
        website = user_input.split("open")[-1].strip()
        if website:
            webbrowser.open(f"https://{website}.com")
        else:
            messagebox.showerror("Input Error", "Please provide a valid website name.")
    elif "search" in user_input:
        query = user_input.split("search")[-1].strip()
        if query:
            webbrowser.open(f"https://www.google.com/search?q={query}")
        else:
            messagebox.showerror("Input Error", "Please provide a search query.")
    else:
        messagebox.showinfo("Info", "Unsupported command.")

# Main GUI
root = tk.Tk()
root.title("Multi-Modal Command Interface")
root.geometry("400x300")

label = tk.Label(root, text="Choose an interaction method:", font=("Helvetica", 14))
label.pack(pady=10)

gesture_button = tk.Button(root, text="Gesture", command=run_gesture_command, width=20, height=2)
gesture_button.pack(pady=5)

voice_button = tk.Button(root, text="Voice", command=run_voice_command, width=20, height=2)
voice_button.pack(pady=5)

text_label = tk.Label(root, text="Type your command below:", font=("Helvetica", 12))
text_label.pack(pady=10)

text_entry = tk.Entry(root, width=30)
text_entry.pack(pady=5)

text_button = tk.Button(root, text="Submit", command=process_text_input)
text_button.pack(pady=10)

root.mainloop()
