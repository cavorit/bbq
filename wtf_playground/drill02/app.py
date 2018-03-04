from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'JapanDeutschland'

class LoginForm(FlaskForm):
    username = StringField('username')  


@app.route('/form', methods=['GET', 'POST'])
def form():
    myForm = LoginForm()
    print(myForm.validate_on_submit())
    if myForm.validate_on_submit():
        return('Hi Jonny I got your message!!!!!! ')
    return(render_template('form.html', form=myForm))

if __name__ == '__main__':
    app.run(debug=True)

