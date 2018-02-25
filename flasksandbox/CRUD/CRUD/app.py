from flask import Flask, render_template, redirect, request
import os 
from flask_sqlalchemy import SQLAlchemy

project_dir = os.path.dirname(os.path.abspath(__file__))
db_uri = 'sqlite:////' + os.path.join(project_dir, 'data.sqlite')        


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri

db = SQLAlchemy(app)

class TabelleA(db.Model):
    ID = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    Vorname = db.Column(db.String(30))
    Nachname = db.Column(db.String(30))

@app.route('/', methods=['GET', 'POST']) 
@app.route('/C', methods=['GET', 'POST'])
def C_of_CRUD():
    if request.form:
        # get vars from form
        vn = request.form.get('vorname')
        nn = request.form.get('nachname')

        # put vars into db
        Person = TabelleA(Vorname=vn, Nachname=nn)  
    
        db.session.add(Person)
        db.session.commit()
    
    return(render_template('home.html'))

@app.route('/R')
def R_of_CRUD():
    
    DF = TabelleA.query.all()
        
    return('R of CRUD')



if __name__ == '__main__':
    app.run(debug=True)

