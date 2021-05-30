from flask import Flask, render_template,request
# from flask_wtf import validators
import database
import email_service_api



db = database.Database()
db.create_table()

app = Flask(__name__,template_folder='templates')


# setting rout for home page
@app.route("/homepage")
def display_homepage():
    return render_template("home.html")

# @app.route("/adminpage")
# def display_signup():
#     return render_template("adminLogin.html")

# rout for admins page
@app.route("/adminlogin")
def display_admins_log():
    return render_template("adminLogin.html")

# accepting admins input
@app.route("/adminlogin", methods = ['POST','GET'])
def admins_log():
    if request.method == 'POST':
        if request.form['username']=="Admin" and request.form['password']=="admin1234":
            details = db.get_data()
            return render_template("adminPage.html", details = details)
        return "incorrect details, try again!"
    

#setting route for registeration form
@app.route("/register")
def display_details():                       
    return render_template('register.html') #homepage

# acception registrers inputs
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
       email_service_api.massage_server(email)
       return 'done'
    
    
    


if __name__ == "__main__":
    app.run(debug= True, host = "0.0.0.0")


