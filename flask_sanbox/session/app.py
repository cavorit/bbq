from flask import Flask, session
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'John Wayne'
# app.secret_key = os.urandom(24)


@app.route('/')
def index():
    #session['user'] = 'Anthony'
    #session['role_A'] = True
    return('Index')

@app.route('/getsession')
def getsession():
    if 'user' in session:
        return(session['user'])
    return('no user found')

@app.route('/popsession')
def popsession():
    if 'user' in session:
        session.pop('user')
        return('session user popped out')
    return('no session user')

if __name__ == '__main__':
    app.run(debug=True)



