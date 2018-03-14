from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms_sqlalchemy.fields import QuerySelectField

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SECRET_KEY'] = 'aksdjfhalskdjfhaslkdfh' 


db = SQLAlchemy(app)

class Auto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    marke = db.Column(db.String(80))
    marken_label = db.Column(db.String(80))

def choice_query():
    return(Auto.query)

class myForm(FlaskForm):
   options = QuerySelectField(query_factory=choice_query, allow_blank=True, get_label='marken_label' )

@app.route('/', methods=['POST', 'GET'])
def home():
    form = myForm()
    return(render_template('index.html', form=form))


if __name__ == '__main__':
    app.run(debug=True)




