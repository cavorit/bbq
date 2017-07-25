from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World"
@app.route('/hello/<name>')
def hello_name(name):
    msg = 'Hello, %s' %(name)
    return msg

if __name__ == "__main__":
    app.run(debug=True)

