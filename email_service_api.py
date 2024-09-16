from flask import Flask, render_template,request
from flask_mail import Mail, Message

app = Flask(__name__, template_folder="templates")

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT']=465
app.config['MAIL_USERNAME']="turntabl80@gmail.com"
app.config['MAIL_PASSWORD']='Turntabl@024'
app.config['MAIL_USE_SSL']=True


mail = Mail(app)

subject = "TNS"
msg = "Thank you for registering with turntabl, you would hear from us soon."

def massage_server(email):
    message = Message(subject, sender="turntabl80@gmail.com", recipients=[email])
    message.body = msg
    mail.send(message)
    return render_template('home.html', results="<script>registration successful</script>")
   
if __name__ =='__main__':
    app.run(debug=True, host='0.0.0.0')