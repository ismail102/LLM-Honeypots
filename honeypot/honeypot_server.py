# honeypot_server.py
from flask import Flask, request, jsonify
from honeypot.prompt_injection import inject_adversarial_prompt
from honeypot.response_logger import log_interaction

app = Flask(__name__)

@app.route("/api/command", methods=["POST"])
def fake_command():
    data = request.get_json()
    prompt = data.get("prompt", "")
    injected = inject_adversarial_prompt(prompt)
    log_interaction(prompt, injected)
    return jsonify({"response": injected})

if __name__ == "__main__":
    app.run(port=5001, debug=True)
