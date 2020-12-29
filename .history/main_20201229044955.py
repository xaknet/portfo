from flask import Flask, render_template, url_for, request
app = Flask(__name__)


@app.route('/')
def webapp():
    return render_template('index.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('login.html', error=error)

# @app.route('/<string:page_name>')
# def html_page(page_name):
#   return render_template(page_name)
