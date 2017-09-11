from flask import Flask, render_template, request, redirect

def search4letters(phrase:str, letters:str) -> set:
    return set(letters).intersection(set(phrase))



app = Flask(__name__)

@app.route('/')
def hello() -> '302':
    return redirect('/entry')

@app.route('/search4', methods = ['POST'])
def do_search() -> str:
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Hier sind die Ergebnisse'
    results = str(search4letters(phrase, letters))
    return render_template('results.html', the_phrase = phrase, the_title = title, the_letters = letters, the_results= results, )


@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', 
            the_title='Willkommen zur Web-Version von search4letter')


if __name__ == '__main__':
    app.run(debug=True)
