from flask import Flask, redirect, request, render_template

app = Flask(__name__)

@app.route('/')
def home() -> 'txt':    
    return(redirect('/entry'))

@app.route('/entry')
def entry():
    return(render_template('entry.html'))

@app.route('/name/<name>')
def name(name):
    return('hallo' + name)

@app.route('/name/<int:zahl>')
def robot(zahl):
    return('Ich bin ein Roboter')

@app.route('/req', methods=['POST', 'GET'])
def req():
    if request.method == 'POST':
        return(render_template('req.html', the_title=request.form['phrase']))
    if request.method == 'GET':
        return(redirect('/entry'))

if __name__ == '__main__':
    app.run(debug=True)

