from flask import Flask, render_template, url_for, request
app = Flask(__name__)


@app.route('/')
def webapp():
    return render_template('index.html')


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form(message):
    return render_template('index.html', message: "Thank you for your message.\n I will review it and contact you soon..")

# @app.route('/<string:page_name>')
# def html_page(page_name):
#   return render_template(page_name)
