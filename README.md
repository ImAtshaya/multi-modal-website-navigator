# 🎯 Multi-Modal Website Navigator Using Voice, Text, and Gesture Recognition

![Python](https://img.shields.io/badge/Python-3.11-blue) ![Tkinter](https://img.shields.io/badge/Tkinter-GUI-green) ![OpenCV](https://img.shields.io/badge/OpenCV-4.x-orange) ![MediaPipe](https://img.shields.io/badge/MediaPipe-Hand%20Gestures-red) ![TensorFlow Lite](https://img.shields.io/badge/TensorFlow%20Lite-ML-purple)

---

## 🧠 Project Overview
This project is an **intelligent system** that allows users to interact with and navigate websites using **three modes of input**:

1. **Voice commands**  
2. **Text input**  
3. **Hand gestures**  

It enhances accessibility and provides a hands-free experience by integrating **speech recognition**, **computer vision**, and **GUI-based navigation** using **Python**.

---

## 🛠️ Technologies & Tools Used
- **Programming Language:** Python  
- **GUI Framework:** Tkinter  
- **Voice Recognition:** `speech_recognition`, `pyaudio`  
- **Text Input:** Tkinter Input Box  
- **Gesture Recognition:** MediaPipe, OpenCV  
- **Web Automation:** `webbrowser` module  
- **ML Framework:** TensorFlow Lite (for model inference)  
- **IDE:** VS Code / PyCharm  
- **Operating System:** Windows

---

## 🧩 Modules and Components

### Voice Recognition Module
- Listens for voice input using a microphone.  
- Converts speech to text.  
- Navigates to the relevant website.  

### Text Command Module
- Accepts typed website names.  
- Opens the specified site via the browser.  

### Gesture Recognition Module
- Uses webcam to detect hand gestures.  
- Maps gestures to specific websites:
  - 👍 Thumbs Up → YouTube  
  - ✊ Fist → Google  
  - ✌️ Peace → GitHub  
  - 🖐️ Open Hand → Wikipedia  

### Main GUI Interface
- Centralized control panel with buttons to activate each feature.  
- Built using Tkinter for a simple, interactive interface.

---

## 🧪 Implementation Flow
1. User launches the main GUI (`main_gui.py`).  
2. Three options appear: Text, Voice, Gesture.  
3. Based on input mode:
   - **Text input:** Website is opened.  
   - **Voice input:** Converts speech to text and opens the site.  
   - **Gesture input:** Webcam recognizes hand gestures and opens websites.  
4. Feedback and errors are shown via GUI messages or print statements.

---

## 🌟 Key Features
- Multi-modal control (Text, Voice, Gesture)  
- Hands-free navigation  
- Real-time gesture recognition using webcam  
- Scalable for more gestures and commands  
- User-friendly GUI

---

## ✅ Applications
- Accessibility tools for differently-abled users  
- Smart kiosk systems  
- Hands-free browsing in AR/VR setups  
- Home automation control interface  

---

## 📈 Future Enhancements
- Add support for more gestures and voice commands  
- Use ML for custom gesture training  
- Integrate with browsers for tab control, scrolling, etc.  
- Add speech synthesis for feedback  
- Deploy as a desktop app using PyInstaller  

---

## 👤 Who Will Use This?
- **Differently-Abled Individuals:** Alternative input methods for navigation.  
- **Elderly Users:** Simplifies browsing without complex navigation.  
- **Tech Enthusiasts/Developers:** Build smart interfaces with multi-modal AI.  
- **Smart Home or Kiosk Systems:** Intuitive, hands-free browsing.  
- **Educational Institutions:** Demonstrates HCI, AI, and assistive tech applications.

---

## ✅ Installation

```bash
# Create virtual environment
python -m venv venv

# Activate environment
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
