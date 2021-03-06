from flask import Flask, render_template, url_for, request, jsonify
app = Flask(__name__)


@app.route('/')
def webapp():
    return render_template('index.html')

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        print(data)
        return "Thank you for your message"
    else:
        return 'something went wrong. Try again!.'

# @app.route('/<string:page_name>')
# def html_page(page_name):
#   return render_template(page_name)

def write_to_file(data):
  with open('database.txt', mode='a') as database:
    email = data["email"]
    subject = data["subject"]
    message = data["message"]