from flask import Flask, render_template, url_for, request
app = Flask(__name__)


@app.route('/')
def webapp():
    return render_template('index.html')


@app.route('/login', methods=['POST'])

# @app.route('/<string:page_name>')
# def html_page(page_name):
#   return render_template(page_name)
