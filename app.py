import os
import sys
import datetime

from dotenv import load_dotenv
from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)
load_dotenv()

def send_mail(target_address, sender, subject):
    mail = Mail(app)

    msg = Message(subject, sender=sender, recipients=[target_address])

    msg.body = ""

    mail.send(msg)
    print("Message sent to " + target_address)

    return None

@app.route('/send_to_all')
def send_to_all():

    app.config['MAIL_SERVER']= os.getenv("MAIL_SERVER")
    app.config['MAIL_PORT'] = os.getenv("MAIL_PORT")
    app.config['MAIL_USERNAME'] = os.getenv("MAIL_USERNAME")
    app.config['MAIL_PASSWORD'] = os.getenv("MAIL_SERVER")
    app.config['MAIL_USE_TLS'] = False
    app.config['MAIL_USE_SSL'] = True

    list_of_address = ["fadhilikurnia@gmail.com", "sukaberkhayal@gmail.com"]
    mail_subject = ""

    try:
        for address in list_of_address:
            send_mail(address)
    finally:
        return "Please watch the server log!"

if __name__ == "__main__":
    app.run(debug=True)
