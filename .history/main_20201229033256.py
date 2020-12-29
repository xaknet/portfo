from flask import Flask, render_tempalte
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'