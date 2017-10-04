from flask import Flask

app = Flask(__name__)

@app.route('/')
def root():
  return 'Ich bin root'

@app.route('/zahl/<int:zahl>')
def square(zahl):
   return 'Das Quadrat wäre dann wohl' + str(zahl**2)

@app.route('/zahl/<float:kommazahl>') # Method Overloading funktioniert!
def dist_to_pi(kommazahl):
    return 'Der Abstand zu Pi beträgt ungefäht ' + str(3.1415 - kommazahl)

@app.route('/pfad/<path:my_path>')
def highway66(my_path):
    return 'Der Pfad lautet ' + my_path


if __name__ == '__main__':
    app.run(debug=True)

