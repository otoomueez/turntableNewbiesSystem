from flask import Flask, render_template, request, url_for
from werkzeug.utils import redirect

import Database

db = Database.Database()
db.create_table()

# db.insert_data_to_db(data)
app = Flask(__name__, template_folder='')


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
        if request.form['username'] == "Admin" and request.form['password'] == "adminturntabl2021":
            details = db.get_data()
            return render_template("html/adminPage.html", details=details)
    return '<script>alert("Incorrect login")</script>', render_template("html/adminlogin.html")


@app.route('/register')
def display_form():
    return render_template('html/register.html')


@app.route('/register', methods=['POST', 'GET'])
def registration_details():
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
        appType = request.form['apptype']
        resume = request.form['resume']
        data = (fn, mn, ln, gdr, email, phone, year, school, appType, resume)
        db.insert_data_to_db(data)
        display_homepage()
    return '<script>alert("registration successfull")</script>'


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
