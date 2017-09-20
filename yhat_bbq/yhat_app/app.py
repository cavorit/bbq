from flask import Flask

app = Flask(__name__)


@app('/output')
@app('/out')
def mdelPredict():
    return '{'feld1' : 'Hallo Welt'}

if __name__ == '__main__':
    app.run()


