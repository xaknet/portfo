from flask import Flask, render_template, url_for
app = Flask(__name__)


@app.route('/')
def webapp():
    print(url_for('static', filename='favicon.ico'))
    return render_template('index.html')
