from flask import Flask, render_template, request, escape

app = Flask(__name__)


@app.route('/hello')
def hello_page():
    return render_template('test.html', 
            the_head='test', 
            the_headline = 'welcome!')

    
@app.route('/')
@app.route('/input')
def input_page():
    return render_template(
            'input.html',
            the_head = 'input-Seite',
            the_headline = 'Eingabemaske'
            )

@app.route('/evaluate', methods=['POST'])
def evaluate_page():
    word = request.form['inputWord']
    pattern = request.form['inputPattern']
    result = set(word).intersection(set(pattern))
    log_req(request, result)
    return render_template('output.html', 
            the_head = 'output-Seite',
            the_headline = 'Suchergebnis',
            the_word = word, 
            the_pattern = pattern, 
            the_result = result)

@app.route('/viewlog')
def view_the_log():
    dataframe = []
    with open('log_req.log') as log:
        for zeile in log:
            dataframe.append([])
            for item in zeile.split('|'):
                dataframe[-1].append(escape(item))               


    return render_template('logbuch.html',
                            the_head = 'logbuch',
                            the_headline = 'Logbuch Einträge',
                            dataframe = dataframe)
    #return str(dataframe)

def log_req(request, result):
    with open('log_req.log', 'a') as log:
        print(request.form,
              request.host_url,
              request.user_agent,
              #dir(request), 
              result,
              sep='|',
              file=log)

if __name__ == '__main__':
    app.run(debug=True)


