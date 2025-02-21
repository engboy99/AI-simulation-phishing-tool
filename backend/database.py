from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask import Flask

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = Config.DATABASE_URI
db = SQLAlchemy(app)

class UserAction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), nullable=False)
    clicked = db.Column(db.Boolean, default=False)
    submitted_data = db.Column(db.Boolean, default=False)

def init_db():
    with app.app_context():
        db.create_all()

if __name__ == "__main__":
    init_db()
