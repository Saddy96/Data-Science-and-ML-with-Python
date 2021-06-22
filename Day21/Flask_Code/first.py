# An object of WSGI application
from flask import Flask, render_template

# Flask app or constructor
app = Flask(__name__)

#which url i need to access
@app.route('/')
def hello():
    return 'Hello World'

@app.route('/courses')
def course():
    return '<h1>Flask basic Deployment</h1>'

@app.route('/<name>')
def user(name):
    return f'<h1>Hello Mr. {name}!! Welcome to the Webpage</h1>'

@app.route('/about')
def about():
    return render_template('about.html')




if __name__ == '__main__':
    app.run(debug=True)
