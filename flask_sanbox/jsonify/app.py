from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        js = request.json['key']
        return(js)
    else:
        erg = {'meine Botschaft':'hallo huli'}
        return(jsonify(erg))


if __name__ == '__main__':
    app.run(debug=True)

