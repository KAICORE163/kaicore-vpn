from flask import Flask, jsonify
import random, uuid, json

app = Flask(__name__)

with open("fake_ip_pool.json") as f:
    ip_pool = json.load(f)

current_session = {
    "ip": None,
    "location": None,
    "ghost_id": None
}

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
