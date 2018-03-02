from flask import Flask, render_template, request
import os
from flask_sqlalchemy import SQLAlchemy
import jinja2

project_dir = os.path.dirname(os.path.abspath(__file__))
db_uri = 'sqlite:///' + os.path.join(project_dir, 'DB.sqlite')


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri

db = SQLAlchemy(app)


class Book(db.Model):
    Titel = db.Column(db.String(80), primary_key=True, unique=True)   


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.form:
        print(request.form)
        ein_buch = request.form.get('x')
        neu = Book(Titel=ein_buch)
        db.session.add(neu)
        db.session.commit()

        alle_buecher = Book.query.all()
        print(alle_buecher)
    return(render_template('input.html', x=alle_buecher)) 



if __name__ == '__main__':
    app.run(debug=True)



