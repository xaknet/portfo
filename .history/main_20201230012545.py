from flask import Flask, render_template, url_for, request, jsonify
import datetime
import csv
app = Flask(__name__)


@app.route('/')
def webapp():
    return render_template('index.html')


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        return "Thank you for your message"
    else:
        return 'something went wrong. Try again!.'

# @app.route('/<string:page_name>')
# def html_page(page_name):
#   return render_template(page_name)


def write_to_file(data):
    with open('database.txt', mode='a') as database:
        time = datetime.datetime.now()
        formatted_time = time.strftime("%Y-%m-%d %H:%M:%S")
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(
            f"\n{formatted_time}: \n\tEmail: {email}, \n\tSubject: {subject}, \n\tMessage: {message}")


def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as database2:
        time = datetime.datetime.now()
        formatted_time = time.strftime("%Y-%m-%d %H:%M:%S")
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(
            database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([formatted_time, email, subject, message])
