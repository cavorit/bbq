from flask import Flask, render_template, url_for
from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Debuggingsecret'

class LoginForm(FlaskForm):
    username = StringField('username')
    password = PasswordField('password')

@app.route('/form', methods=['GET', 'POST'])
def form():
    form = LoginForm()
    return(render_template('form.html', form=form))

@app.route('/ziel', methods=['POST'])
def ziel():
    form = LoginForm()
    x = form.username.data
    return('Sie sind am Ziel angekommen '+x)


if __name__ == '__main__':
    app.run(debug=True)

