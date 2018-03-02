from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db  = SQLAlchemy(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

# Pet <--n:1--> Human

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
# >>>> h = Human(name='Harald Fiedler')
# >>>> m = Pet(name='Molly')
# >>>> s= Pet(name='Sosten')
# >>>> m.owner = harald
# >>>> s.owner = harald
# >>>> db.session.add(m)
# >>>> db.session.add(s)
# >>>> db.session.add(h)
# >>>> m.owner = h
# >>>> s.owner = h
# >>>> db.session.commit()
# >>>> exit()
# > sqlite3 db.sqlite
# >>> .table
# >>> select * from human;

# select * from human;
#id|name
#1| Harald

# select * from pet;
#id|name|owner_id
#1|molly|1
#2|sosten|1



