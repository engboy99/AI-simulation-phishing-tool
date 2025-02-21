from flask import Flask, request, jsonify
from flask_cors import CORS
from database import db, UserAction
from email_sender import send_email
from tracking import track_click, track_submission
from ai_analysis import analyze_email

app = Flask(__name__)
CORS(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///phishing_sim.db"
db.init_app(app)

@app.route("/send-phishing", methods=["POST"])
def send_phishing():
    data = request.json
    target_email = data.get("email")
    result = send_email(target_email)
    return jsonify(result)

@app.route("/analyze-email", methods=["POST"])
def analyze():
    data = request.json
    email_text = data.get("text")
    prediction = analyze_email(email_text)
    return jsonify({"prediction": prediction})

if __name__ == "__main__":
    app.run(debug=True)
