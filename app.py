from flask import Flask, jsonify, send_from_directory
import random
import json
import uuid
import os

app = Flask(__name__)

# Load IP pool
with open('fake_ip_pool.json') as f:
    ip_pool = json.load(f)

# Track current session
current_session = {
    "ip": None,
    "location": None,
    "ghost_id": None
}

@app.route("/")
def serve_ui():
    return send_from_directory('.', 'jsvpn.html')

@app.route("/vpn.css")
def serve_css():
    return send_from_directory('.', 'vpn.css')

@app.route("/vpn.js")
def serve_js():
    return send_from_directory('.', 'vpn.js')

@app.route("/api/start-session")
def start_session():
    selected = random.choice(ip_pool)
    current_session['ip'] = selected['ip']
    current_session['location'] = selected['location']
    current_session['ghost_id'] = f"Ghost-{str(uuid.uuid4())[:4]}"
    return jsonify(current_session)

@app.route("/api/rotate-ip")
def rotate_ip():
    selected = random.choice(ip_pool)
    current_session['ip'] = selected['ip']
    current_session['location'] = selected['location']
    return jsonify({
        "ip": current_session['ip'],
        "location": current_session['location']
    })

if __name__ == "__main__":
    app.run(debug=True)

