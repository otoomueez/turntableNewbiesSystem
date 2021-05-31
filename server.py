import numbers
import sqlite3
import string

from flask import Flask, render_template, request, url_for
from werkzeug.utils import redirect
from flask_mail import Mail, Message

import Database

db = Database.Database()
db.create_table()

# db.insert_data_to_db(data)
# db.clear_db()
app = Flask(__name__, template_folder='')

# Mailing system
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = "turntabl80@gmail.com"
app.config['MAIL_PASSWORD'] = 'Turntabl@024'
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

subject = "Turntabl - Software Engineering Application"
msg = """Dear Applicant,
            Thank you very much for applying for the Software engineering internship program at Turntabl. I'd like to let you know that we have received your application. 

            Our hiring team has begun reviewing all applications and shortlisting candidates for a telephone interview.   
            We will at every stage of the interview process keep you posted on the status of your application.

            Thank you, again, for taking the time to apply for this role at Turntabl.

            --
            Regards,
            Review Team,

            Turntabl Ghana.
    """


def massage_server(email):
    message = Message(subject, sender="turntabl80@gmail.com", recipients=[email])
    message.body = msg
    mail.send(message)
    return 0


@app.route("/homepage")
def display_homepage():
    return render_template("html/home.html")


@app.route("/admin_panel")
def display_admins_panel():
    details = db.get_data()
    print(details)
    return render_template('html/adminPage.html', details=details)


@app.route("/admin_panel", methods=['POST', 'GET'])
def display_search():
    if request.method == 'POST':
        column = request.form['column']
        value = request.form['record']
        details = db.search_data(column, value)
        if value == '':
            return redirect(url_for('display_admins_panel'))
        return render_template('html/adminPage.html', details=details)


@app.route("/adminlogin")
def display_admins_log():
    return render_template("html/adminLogin.html")


@app.route("/adminlogin", methods=['POST', 'GET'])
def admins_log():
    if request.method == 'POST':
        if request.form['username'] == "Admin" and request.form['password'] == "admin1234":
            details = db.get_data()
            return render_template("html/adminPage.html", details=details)
    return render_template("html/adminLogin.html", msg="Incorrect Details")


@app.route('/register')
def display_form():
    return render_template('html/register.html')


@app.route('/register', methods=['POST', 'GET'])
def registration_details():
    try:
        if request.method == 'POST':
            #    value = request.form
            fn = request.form['fname']
            mn = request.form['mname']
            ln = request.form['lname']
            gdr = request.form['gender']
            email = request.form['email']
            phone = request.form['phone']
            year = request.form['year']
            school = request.form['school']
            app_type = request.form['apptype']
            resume = request.form['resume']
            for i in string.digits:
                if fn.__contains__(i) or mn.__contains__(i) or ln.__contains__(i) or school.__contains__(i):
                    return render_template("html/register.html", msg="Some inputs do not have to contain numbers")
            data = (fn, mn, ln, gdr, email, phone, year, school, app_type, resume)
            db.insert_data_to_db(data)
            massage_server(email)
            return redirect(url_for('display_homepage'))
    except sqlite3.IntegrityError:
        return render_template("html/register.html", msg="Already registered")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
