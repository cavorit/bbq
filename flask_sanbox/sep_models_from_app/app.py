from flask import Flask
from models import db, Auto


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

db.init_app(app)



A = Auto(name='BigBully')
db.session.add(A)
db.commit()

@app.route('/')
def home():
    return('hi')

if __name__ == '__main__':
    app.run(debug=True)




