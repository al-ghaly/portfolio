from flask import Flask, render_template, request, redirect
import csv
app = Flask(__name__)

def add_to_database(data):
    file = open('database.csv', 'a', newline='')
    email = data['email']
    subject = data['subject']
    message = data['message']
    writer = csv.writer(file)
    writer.writerow([email, subject, message])


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/<name>')
def home1(name):
    return render_template(name)

@app.route('/contact', methods=['POST', 'GET'])
def send():
    if request.method == 'POST':
        data = request.form.to_dict()
        add_to_database(data)
        return redirect('/thanks.html')
    else:
        return render_template('/error.html')

