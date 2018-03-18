from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import FormField, StringField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'my secret'

class Innen(FlaskForm):
    alpha = StringField('Heinrich')


@app.route('/', methods=['GET', 'POST'])
def home():
    print('start')
    form = Innen()
    if form.validate_on_submit():
        print('post ist da: ' + form.alpha.data )
    return(render_template('index.html', form=form))    


if __name__ == '__main__':
    app.run(debug=True)




