from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db  = SQLAlchemy(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

class Pet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    # owner bei db.relationship
    owner_id = db.Column(db.Integer, db.ForeignKey('human.id'))

    def __rexp__(self):
        return('<Pet: {}>'.format(self.name))

class Human(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    my_pets = db.relationship('Pet', backref='owner', lazy=True)

    def __rexp__(self):
        return('<Human: {}>'.format(self.name))

# > python3
# >>>> from app import *
# >>>> db.create_all()
# >>>> harald = Human(name='Harald Fiedler')
# >>>> molly = Pet(name='Molly')
# >>>> waldi = Pet(name='Waldi')
# >>>> molly.owner = harald
# >>>> waldi.owner = harald
# >>>> db.session.add(harald)
# >>>> db.session.commit()
# >>>> exit()
# > sqlite3 db.sqlite
# >>> .table
# >>> select * from human;

