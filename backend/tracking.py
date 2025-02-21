from flask import Flask, request, jsonify
from database import db, UserAction

app = Flask(__name__)

@app.route("/track-click", methods=["POST"])
def track_click():
    data = request.json
    email = data.get("email")

    user = UserAction.query.filter_by(email=email).first()
    if user:
        user.clicked = True
    else:
        user = UserAction(email=email, clicked=True)
        db.session.add(user)

    db.session.commit()
    return jsonify({"message": "Click tracked successfully"})

@app.route("/track-submission", methods=["POST"])
def track_submission():
    data = request.json
    email = data.get("email")

    user = UserAction.query.filter_by(email=email).first()
    if user:
        user.submitted_data = True
    else:
        user = UserAction(email=email, clicked=True, submitted_data=True)
        db.session.add(user)

    db.session.commit()
    return jsonify({"message": "Data submission tracked successfully"})
