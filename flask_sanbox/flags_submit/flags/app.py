from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return(render_template('flags.html'))

@app.route('/myflag', methods=['POST'])
def my_flag():
    x = request.form['flag_button']
    return(x)

if __name__ == '__main__':
    app.run(debug=True)
