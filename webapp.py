from flask import Flask, render_template,request
import database

db = database.Database()
db.create_table()



app = Flask(__name__,template_folder='templates')

@app.route("/homepage")
def display_homepage():
    pass

@app.route("/register")
def display_details():                        #for the message, javascript alert popup will display
    return render_template('register.html') #homepage


@app.route("/adminpanel")
def display_admins_panel():
    details = db.get_data()
    return render_template('adminPage.html', details = details)

@app.route("/adminlogin")
def display_admins_log():
    return render_template("adminLogin.html")

@app.route("/adminlogin", methods = ['POST','GET'])
def admins_log():
    if request.method == 'POST':
        if request.form['username']=="Admin" and request.form['password']=="admin1234":
            return render_template("adminPage.html")
        return "incorrect details, try again!"

@app.route('/register', methods = ['POST','GET'])
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
       data = (fn,mn,ln,gdr,email,phone,year,school,appType,resume)
       db.insert_data_to_db(data)
       return '<script>alert("registration successfull")</script>'
    


if __name__ == "__main__":
    app.run(debug= True, host = "0.0.0.0")


