from flask import Flask, render_template, request, redirect
import csv
app = Flask(__name__)


@app.route('/')
def my_home():
    return render_template('index.html')


@app.route('/styles')
def about():
    return render_template('styles.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email}, {subject}, {message}')


def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=' ',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@app.route('/form_submitted', methods=['POST', 'GET'])
def contact_me():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/index.html#contact')
        except:
            return 'did not save to database'
    else:
        return 'something went wrong'
