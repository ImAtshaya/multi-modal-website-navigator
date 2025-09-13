<h1 align="center" style="color:#2F80ED; font-family:Arial, Helvetica, sans-serif;">
 🎯 Multi-Modal Website Navigator Using Voice, Text, and Gesture Recognition 
</h1>

<p align="center">
  <img src="https://img.shields.io/badge/License-MIT-green.svg" />
  <img src="https://img.shields.io/badge/Python-3.9+-blue?logo=python" />
  <img src="https://img.shields.io/badge/OpenCV-Computer%20Vision-orange?logo=opencv" />
  <img src="https://img.shields.io/badge/Tkinter-GUI-lightgrey" />
</p>

---

<h2 style="color:#27AE60;"> 🧠 Abstract </h2>

<p>
This project introduces an intelligent system that enables users to navigate websites using 
<b style="color:#E67E22;">Voice, Text, and Gesture Recognition</b>.  
It combines <b>Speech Recognition</b>, <b>Computer Vision</b>, and <b>GUI Navigation</b> to create an accessible and hands-free browsing experience.  
</p>

---

<h2 style="color:#9B51E0;"> 🛠️ Technologies & Tools Used </h2>

<table>
<tr><td><b>Programming Language</b></td><td>Python</td></tr>
<tr><td><b>GUI Framework</b></td><td>Tkinter</td></tr>
<tr><td><b>Voice Recognition</b></td><td>speech_recognition, pyaudio</td></tr>
<tr><td><b>Gesture Recognition</b></td><td>MediaPipe, OpenCV</td></tr>
<tr><td><b>Web Automation</b></td><td>webbrowser module</td></tr>
<tr><td><b>ML Framework</b></td><td>TensorFlow Lite</td></tr>
<tr><td><b>IDE</b></td><td>VS Code / PyCharm</td></tr>
<tr><td><b>Operating System</b></td><td>Windows</td></tr>
</table>

---

<h2 style="color:#F2994A;"> 🧩 Modules & Components </h2>

- 🎤 <b style="color:#EB5757;">Voice Recognition Module</b> → Microphone input → Speech to text → Open site.  
- ⌨️ <b style="color:#2D9CDB;">Text Command Module</b> → Type website → Open in browser.  
- ✋ <b style="color:#6FCF97;">Gesture Recognition Module</b> → Webcam + MediaPipe → Detect gestures:  
  - 👍 Thumbs Up → YouTube  
  - ✊ Fist → Google  
  - ✌️ Peace → GitHub  
  - 🖐️ Open Hand → Wikipedia  
- 🖥️ <b style="color:#9B51E0;">Main GUI Interface</b> → Central panel with buttons for each feature.  

---

<h2 style="color:#56CCF2;"> 🧪 Implementation Flow </h2>

```mermaid
flowchart TD
    A[Launch main_gui.py] --> B{Choose Mode}
    B -->|Text| C[Open site via text input]
    B -->|Voice| D[Speech → Text → Browser]
    B -->|Gesture| E[Camera + MediaPipe → Detect Gesture → Open site]
    C --> F[Website Opened]
    D --> F
    E --> F
<h2 style="color:#BB6BD9;"> 🌟 Key Features </h2>

✅ Multi-modal control (Text, Voice, Gesture)
✅ Real-time gesture recognition
✅ No mouse/keyboard required
✅ Scalable & extendable
✅ Accessibility-focused

<h2 style="color:#EB5757;"> ⚠️ Known Issues </h2>

Gesture recognition accuracy depends on lighting & camera quality.

<h2 style="color:#2F80ED;"> 🚀 Installation & Setup </h2>
# Clone this repository
git clone https://github.com/username/multi-modal-navigator.git
cd multi-modal-navigator

# Install dependencies
pip install -r requirements.txt

# Run the app
python main_gui.py

<h2 style="color:#9B51E0;"> ✅ Conclusion </h2>

This project demonstrates how Voice, Gesture, and Text inputs can be integrated for website navigation,
paving the way for next-gen Human-Computer Interaction and accessibility-focused systems.

<h2 style="color:#F2994A;"> 📜 License </h2>

This project is licensed under the MIT License.

<h2 style="color:#27AE60;"> 👨‍💻 Author </h2>

<b>Your Name</b>
🌐 GitHub
 | 🔗 LinkedIn
