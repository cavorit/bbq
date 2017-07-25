from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/')
def my_root_fun():
    return "Hi there, this is root"

@app.route('/redirect/<int:var1>')
def my_redir1(var1):
    my_result = str(var1 ** 2) 
    return "Mein Quadrat ist " + my_result

@app.route('/redirect/<path:pf>')
def my_redir2(pf):
    return "The path of light is: " + pf


@app.route('/hoho/<my_x>')
def handling(my_x):
    if my_x == "Harald":
        return redirect(url_for('my_redir2', pf = my_x))
    else:
        return "Du bist nicht Harald"

# hier fängt das eigentliche Tutorial an

@app.route('/success/<name>')
def success(name):
    return 'welcome %s' % name

app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('succes', name=user))
    else:
        user = request.args.get('nm')
        return redirect(url_for('success', name = user))

# Also bei mir funktioniert das Beispiel nicht. Ich komme mit localhost:5000/login einfach nicht auf login.html

if __name__ == "__main__":
    app.run(debug=True)


