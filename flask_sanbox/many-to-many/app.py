from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

association_table = db.Table('p2h',
            db.Column('pet_id', db.ForeignKey('pet.id')),
            db.Column('human_id', db.ForeignKey('human.id'))
        )

class Pet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    owner = db.relationship('Human', secondary='p2h', backref=db.backref('my_owner', lazy='dynamic'))
    

class Human(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)



db.create_all()
m = Pet(name='Molly')
s = Pet(name='Sosstaine')
h = Human(name='Harald')
r = Human(name='Familie Richter')
db.session.add(m)
db.session.add(s)
db.session.add(h)
m.owner.append(h)
m.owner.append(r)
s.owner.append(h)
db.session.commit()



