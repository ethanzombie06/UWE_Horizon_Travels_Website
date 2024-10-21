from flask import Flask

app = Flask(__name__)

@app.route('/')
def Homepage():
    return 'home.html'

@app.route('/hello/<username>')
def hello(username):
    exec(username)
    return f'hi {username}'