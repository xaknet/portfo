from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def inde():
    return 'Hello, World!'