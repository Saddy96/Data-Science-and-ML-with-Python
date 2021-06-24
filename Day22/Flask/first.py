# An object of WSGI application
from flask import Flask, render_template
from flask import redirect, url_for
from flask import *


# Flask app or constructor
app = Flask(__name__)

#which url i need to access
@app.route('/')
def red():
    return render_template('index.html')

@app.route('/courses')
def course():
    return '<h1>Flask basic Deployment</h1>'


@app.route('/submit', methods = ['POST','GET'])
def submit():
    marks = 0
    if request.method == 'POST':
        phy = float(request.form['physics'])
        che = float(request.form['chemistry'])
        math = float(request.form['maths'])

        total = (phy+che+math)/3
    marks = total
    return redirect(url_for('success', marks = marks))

@app.route('/user/<name>')
def user(name):
    return f'<h1>Hello Mr. {name}!! Welcome to the Webpage</h1>'

@app.route('/results/<int:marks>')
def results(marks):
    
    return redirect(url_for('success', marks = marks))

@app.route('/success/<int:marks>')
def success(marks):
    final = ''
    if marks  < 45:
        final = 'Fail'
    else:
        final = 'Pass'

    exp = {'numbers': marks, 'result':final}
    return render_template('result.html', result = exp)

    

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
