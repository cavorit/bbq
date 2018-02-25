from flask import Flask, render_template, request, redirect
import os
from flask_sqlalchemy import SQLAlchemy

pathdir = os.path.dirname(os.path.abspath(__file__))
db_uri = 'sqlite:///' + os.path.join(pathdir, 'DB.sqlite')        


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri

db = SQLAlchemy(app)

class Teilnehmer(db.Model):
    
    member = db.Column(db.String(80), primary_key=True, unique=True)



@app.route('/', methods=['POST', 'GET'])
def home():
    if request.form:
        
        new_Teilnehmer = Teilnehmer(member=request.form.get('member'))
        db.session.add(new_Teilnehmer)
        db.session.commit() 

    x = Teilnehmer.query.all()

    return(render_template('home.html', member_list=x))

@app.route('/update', methods=['POST'])
def update():
    newtitle = request.form.get('newtitle')
    oldtitle = request.form.get('oldtitle')
    kandidat = Teilnehmer.query.filter_by(member=oldtitle).first()
    kandidat.member = newtitle
    db.session.commit()
    return(redirect('/'))  


if __name__ == '__main__':
    app.run(debug=True)


