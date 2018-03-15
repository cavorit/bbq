from flask import Flask, render_template

from flask_sqlalchemy import SQLAlchemy
from pandas import read_csv 


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

db = SQLAlchemy(app)


df = read_csv('http://bit.ly/uforeports')
meine_Tabelle = df.to_html()

@app.route('/')
def home():
    return(render_template('index.html', the_title='Meine H1 Überschrift', the_table = meine_Tabelle))

if __name__ == '__main__':
    app.run(debug=True)


