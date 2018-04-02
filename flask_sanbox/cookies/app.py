from flask import Flask, make_response, request

app = Flask(__name__)


@app.route('/')
@app.route('/set')
def setcookie():
    resp = make_response('Setting cookie!')
    resp.set_cookie('framework', 'flask')


@app.route('/get')
def getcookie():
    framework = request.cookies.get('framework')
    allC = request.cookies
    print(allC)
    return(framework)



if __name__ == '__main__':
    app.run(debug=True)

