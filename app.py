from flask import Flask, render_template, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/gesture')
def gesture():
    subprocess.Popen(["python", "gesture_command.py"])
    return '', 204

@app.route('/voice')
def voice():
    subprocess.Popen(["python", "voice_command.py"])
    return '', 204

@app.route('/facial')
def facial():
    subprocess.Popen(["python", "facial_command.py"])
    return '', 204

@app.route('/text', methods=['POST'])
def text():
    data = request.get_json()
    command = data.get('command', '')
    if command:
        subprocess.Popen(["python", "text_command.py", command])
        return jsonify({"message": "Command submitted successfully!"})
    return jsonify({"message": "No command received"}), 400

if __name__ == '__main__':
    app.run(debug=True)
