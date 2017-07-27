from flask import Flask

app = Flask(__name__)

@app.route('/')
def dasIstDieRouteFunk():
    return 'Hallo World'

@app.route('/wdh/')
def wdh():
    return 'Das ist Wdh'

@app.route('/wdh/<jonny>')
def wdh_mit_johnny(jonny):
   return 'das ist %s' % jonny

if __name__ == "__main__":
    app.run(debug=True)

