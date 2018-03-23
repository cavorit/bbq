from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy() # note no "app" hereexi

class Auto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))


