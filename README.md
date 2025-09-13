<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <title>Multi‑Modal Website Navigator — README</title>
  <style>
    :root{--bg:#0f1724;--card:#0b1220;--muted:#9aa4b2;--accent:#7c3aed;--glass:rgba(255,255,255,0.03);--glass-2:rgba(255,255,255,0.02)}
    *{box-sizing:border-box;font-family:Inter,ui-sans-serif,system-ui,-apple-system,'Segoe UI',Roboto,'Helvetica Neue',Arial}
    body{margin:0;background:linear-gradient(180deg,#071022 0%, #071526 100%);color:#e6eef6;line-height:1.5}
    .wrap{max-width:980px;margin:32px auto;padding:24px}
    header{display:flex;align-items:center;gap:18px}
    .logo{width:76px;height:76px;border-radius:14px;background:linear-gradient(135deg,var(--accent),#3b82f6);display:grid;place-items:center;box-shadow:0 8px 30px rgba(2,6,23,0.6)}
    .logo svg{width:44px;height:44px}
    h1{margin:0;font-size:22px}
    .sub{color:var(--muted);margin-top:6px;font-size:13px}
    .badges{margin-left:auto;display:flex;gap:8px}
    .badge{background:var(--glass);padding:6px 10px;border-radius:999px;font-size:12px;color:var(--muted)}

    .grid{display:grid;grid-template-columns:1fr 340px;gap:18px;margin-top:20px}
    .card{background:linear-gradient(180deg,var(--card),#071424);border-radius:12px;padding:18px;box-shadow:0 6px 28px rgba(2,6,23,0.6)}

    pre{background:var(--glass-2);padding:12px;border-radius:8px;overflow:auto;color:#d6e6ff}
    code{font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,'Liberation Mono',monospace;font-size:13px}
    .meta{display:flex;gap:10px;flex-wrap:wrap}
    .btn{display:inline-flex;align-items:center;gap:8px;padding:8px 12px;border-radius:8px;border:0;background:linear-gradient(90deg,var(--accent),#4f46e5);color:white;cursor:pointer}
    .outline{background:transparent;border:1px solid rgba(255,255,255,0.06)}

    .section{margin-top:16px}
    .h2{font-size:16px;margin-bottom:8px}
    .list{padding-left:18px}

    .right .toc{position:sticky;top:24px}
    .toc h3{margin:0 0 8px 0;font-size:14px}
    .toc a{display:block;color:var(--muted);text-decoration:none;padding:6px;border-radius:6px}
    .toc a:hover{background:var(--glass)}

    .feature-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:10px}
    .chip{background:linear-gradient(90deg,rgba(255,255,255,0.02),rgba(255,255,255,0.01));padding:8px;border-radius:8px;font-size:13px;color:var(--muted)}

    .code-head{display:flex;justify-content:space-between;align-items:center;margin-bottom:8px}
    .copy{background:transparent;border:1px solid rgba(255,255,255,0.04);padding:6px;border-radius:8px;color:var(--muted);cursor:pointer}

    footer{margin-top:24px;text-align:center;color:var(--muted);font-size:13px}

    /* responsive */
    @media (max-width:920px){.grid{grid-template-columns:1fr}.right{order:2}.toc{position:static}}
  </style>
</head>
<body>
  <div class="wrap">
    <header>
      <div class="logo" aria-hidden>
        <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><rect width="24" height="24" rx="6" fill="white" opacity="0.06"/><path d="M6 12h12M12 6v12" stroke="white" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round" opacity="0.9"/></svg>
      </div>
      <div>
        <h1>Multi‑Modal Website Navigator — README</h1>
        <div class="sub">Voice • Text • Gesture — Python • MediaPipe • SpeechRecognition • OpenCV • Tkinter</div>
      </div>

      <div class="badges">
        <div class="badge">Python</div>
        <div class="badge">Accessibility</div>
        <div class="badge">HCI</div>
      </div>
    </header>

    <div class="grid">
      <main class="card left">
        <section class="section">
          <div class="h2">Project Overview</div>
          <p>This project provides a desktop GUI which lets users open and navigate websites using three input modes: <strong>typed text</strong>, <strong>voice commands</strong>, and <strong>hand gestures</strong> detected using the webcam. It is intended as an accessibility and HCI demo built with Python.</p>
        </section>

        <section class="section">
          <div class="h2">Features</div>
          <div class="feature-grid">
            <div class="chip">Text command parsing & quick launch</div>
            <div class="chip">Speech → text using microphone</div>
            <div class="chip">Real‑time hand gesture mapping</div>
            <div class="chip">Tkinter GUI for unified control</div>
          </div>
        </section>

        <section class="section">
          <div class="h2">Quick Demo</div>
          <p>Try these interactive buttons locally after you download the repository. They simulate common actions and open the specified URLs using <code>webbrowser.open()</code>.</p>
          <div class="meta" style="margin-top:10px">
            <button class="btn" onclick="openExample('https://www.youtube.com')">Open YouTube</button>
            <button class="btn outline" onclick="openExample('https://www.google.com')">Open Google</button>
            <button class="btn outline" onclick="openExample('https://github.com')">Open GitHub</button>
          </div>
        </section>

        <section class="section">
          <div class="h2">Installation</div>
          <pre><code>python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt</code></pre>
          <div style="margin-top:8px;color:var(--muted)">Requirements (example): <code>opencv-python</code>, <code>mediapipe</code>, <code>SpeechRecognition</code>, <code>pyaudio</code>, <code>tensorflow</code> (or <code>tflite-runtime</code>), <code>tkinter</code>.</div>
        </section>

        <section class="section">
          <div class="h2">Run the App</div>
          <pre><code># from project root
default: python main_gui.py
# For gesture debugging: python gesture_debug.py
# For voice test: python voice_test.py</code></pre>

          <div style="margin-top:8px;color:var(--muted)">Note: On Windows, <code>pyaudio</code> may require installing wheel files or using <code>pipwin</code>.</div>
        </section>

        <section class="section">
          <div class="h2">Project Structure</div>
          <pre><code>├─ README_interactive.html
├─ requirements.txt
├─ main_gui.py
├─ modules/
│  ├─ voice_module.py
│  ├─ text_module.py
│  ├─ gesture_module.py
│  └─ utils.py
└─ assets/
   └─ icons/
</code></pre>
        </section>

        <section class="section">
          <div class="h2">Core Implementation Snippets</div>

          <div class="code-head"><strong>Gesture detection (simplified)</strong><button class="copy" data-snippet="gesture">Copy</button></div>
          <pre id="snippet-gesture"><code>import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.6)
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret: break
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)
    if result.multi_hand_landmarks:
        for handLms in result.multi_hand_landmarks:
            # compute finger states and map to gestures
            pass
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release(); cv2.destroyAllWindows()</code></pre>

          <div class="code-head"><strong>Voice command (simplified)</strong><button class="copy" data-snippet="voice">Copy</button></div>
          <pre id="snippet-voice"><code>import speech_recognition as sr
r = sr.Recognizer()
with sr.Microphone() as source:
    audio = r.listen(source)
text = r.recognize_google(audio)
print('Heard:', text)
# parse and open webbrowser
</code></pre>

          <div class="code-head"><strong>Text module (simplified)</strong><button class="copy" data-snippet="text">Copy</button></div>
          <pre id="snippet-text"><code>import webbrowser

def open_site_from_text(inp):
    cmd = inp.lower()
    if 'youtube' in cmd:
        webbrowser.open('https://www.youtube.com')
    elif 'google' in cmd:
        webbrowser.open('https://www.google.com')
</code></pre>

        </section>

        <section class="section">
          <div class="h2">Gesture Accuracy — Troubleshooting & Tips</div>
          <ul class="list">
            <li>Ensure good lighting and high contrast between hand and background.</li>
            <li>Keep camera at eye/shoulder level and avoid backlight.</li>
            <li>Tune MediaPipe thresholds (min_detection_confidence / min_tracking_confidence).</li>
            <li>Use smoothing or simple temporal filters (e.g., require N consecutive frames) before triggering an action.</li>
            <li>Provide a calibration step so users can capture a few examples of their gestures.</li>
          </ul>
        </section>

        <section class="section">
          <div class="h2">Extending the Project</div>
          <ol class="list">
            <li>Add more gesture mappings and allow users to customize them via a settings file.</li>
            <li>Integrate browser automation (Selenium/pyppeteer) for tab switching and scrolling.</li>
            <li>Use a small classifier (TFLite) to learn user‑specific gestures for higher accuracy.</li>
            <li>Expose a REST API so other apps can send commands to the navigator.</li>
          </ol>
        </section>

        <section class="section">
          <div class="h2">Contributing</div>
          <p>Contributions are welcome. Open an issue describing the improvement or file a PR. For code style, use <code>black</code> and type hints where possible.</p>
        </section>

        <section class="section">
          <div class="h2">License</div>
          <p>Choose an appropriate license (e.g., MIT). Add a <code>LICENSE</code> file to the repo.</p>
        </section>

      </main>

      <aside class="card right">
        <div class="toc">
          <h3>Table of contents</h3>
          <a href="#">Overview</a>
          <a href="#">Features</a>
          <a href="#">Installation</a>
          <a href="#">Run the App</a>
          <a href="#">Structure</a>
          <a href="#">Code Snippets</a>
          <a href="#">Troubleshooting</a>
          <a href="#">Contributing</a>
        </div>

        <div style="margin-top:14px">
          <div class="h2">Quick actions</div>
          <div style="display:flex;flex-direction:column;gap:8px;margin-top:8px">
            <button class="btn" onclick="downloadHTML()">Download README (HTML)</button>
            <button class="btn outline" onclick="toggleTheme()">Toggle Theme</button>
          </div>
        </div>

        <div style="margin-top:14px">
          <div class="h2">Who will use this?</div>
          <div class="list">
            <p style="margin:6px 0;color:var(--muted);">Differently-abled users, elderly, HCI researchers, kiosks, and smart home systems.</p>
          </div>
        </div>

        <div style="margin-top:14px">
          <div class="h2">Acknowledgements</div>
          <div style="color:var(--muted);font-size:13px">MediaPipe, OpenCV, SpeechRecognition, TensorFlow Lite</div>
        </div>
      </aside>
    </div>

    <footer>Created with ❤️ — Multi‑Modal Website Navigator. Edit this README to match your repo details.</footer>
  </div>

  <script>
    function openExample(url){ window.open(url, '_blank'); }

    document.querySelectorAll('.copy').forEach(btn => {
      btn.addEventListener('click', () => {
        const pre = btn.closest('.code-head').nextElementSibling;
        const text = pre.innerText;
        navigator.clipboard.writeText(text).then(()=>{
          btn.innerText = 'Copied!';
          setTimeout(()=> btn.innerHTML = 'Copy',1200);
        }).catch(()=>{ btn.innerText = 'Failed'; setTimeout(()=> btn.innerHTML = 'Copy',1200); });
      });
    });

    function downloadHTML(){
      const blob = new Blob([document.documentElement.outerHTML],{type:'text/html'});
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a'); a.href = url; a.download = 'README_interactive.html'; document.body.appendChild(a); a.click(); a.remove();
      URL.revokeObjectURL(url);
    }

    function toggleTheme(){
      const root = document.documentElement;
      if(root.style.getPropertyValue('--bg') === ''){
        // noop
      }
      // swap simple bright theme
      if(root.style.getPropertyValue('--accent') === 'var(--accent)') return;
      // quick theme: invert colors
      if(root.style.getPropertyValue('--accent') === 'rgb(124, 58, 237)'){
        // already default
      }
      // simple visual feedback
      alert('Theme toggle available when editing the file. Use your own CSS variables to customize.');
    }
  </script>
</body>
</html>
