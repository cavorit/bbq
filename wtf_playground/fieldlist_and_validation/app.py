from flask import Flask, render_template, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FieldList, FormField
from wtforms.validators import InputRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'adfgafd'


class SubForm(FlaskForm):
    required_sub = StringField('I am required in sub form', validators=[InputRequired()])
    opt_sub = StringField('I am optional in sub form')
    field_D = SubmitField(' ok ')


class MainForm(FlaskForm):
    required_main = StringField('I am required in main form', validators=[InputRequired()]) 
    opt_main = StringField('I am optional in main form')
    sub = FieldList(FormField(SubForm), min_entries=1)

@app.route('/', methods=['GET','POST'])
def home():
    
    the_form = MainForm()
    if the_form.validate_on_submit():
        print(the_form.required_main.data)

    return(render_template('index.html', form=the_form))

if __name__ == '__main__':
    app.run(debug=True)



