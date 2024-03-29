import os
import sys
import datetime

from dotenv import load_dotenv
from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)
load_dotenv()

# reading mail template from data directory
data_mail_template = ""
with open('data/email_template.txt', 'r') as file:
    data_mail_template = file.read()

# reading mail subject from data directory
data_mail_subject = ""
with open('data/email_subject.txt', 'r') as file:
    data_mail_subject = file.read().replace('\n', '')

def send_mail(target_address, sender, subject, body_data):
    mail = Mail(app)

    msg = Message(subject, sender=sender, recipients=[target_address])

    msg.body = data_mail_template
    msg.body = msg.body.replace('{{EMAIL}}', target_address)
    msg.body = msg.body.replace('{{NAME}}', body_data[target_address])

    mail.send(msg)
    print("Message sent to " + target_address)

    return None

@app.route('/send_to_all')
def send_to_all():

    app.config['MAIL_SERVER']= os.getenv("MAIL_SERVER")
    app.config['MAIL_PORT'] = os.getenv("MAIL_PORT")
    app.config['MAIL_USERNAME'] = os.getenv("MAIL_USERNAME")
    app.config['MAIL_PASSWORD'] = os.getenv("MAIL_PASSWORD")
    app.config['MAIL_USE_TLS'] = False
    app.config['MAIL_USE_SSL'] = True

    # load recepients from data directory
    list_of_address = []
    with open ("data/recepients.txt", "r") as myfile:
        list_of_address=myfile.readlines()

    # load body data from data directory.
    # Modify this section according to desired email template.
    body_data = {}
    with open ("data/body_data.csv", "r") as myfile:
        next(myfile)
        for line in myfile.readlines():
            line = line.strip().split(',')
            address = line[0]
            name = line[1]
            body_data[address] = name

    sender = os.getenv("MAIL_USERNAME")
    mail_subject = data_mail_subject

    failed_sent = []

    print("Starting to send email ...")
    for address in list_of_address:
        try:
            send_mail(address, sender, mail_subject, body_data)
        except:
            failed_sent.append(address)
            print("failed to send email to " + address)

    print("All emails sent!")

    # store failed sent data
    with open("data/failed_recepients.txt", "w") as txt_file:
        for line in failed_sent:
            txt_file.write(line + "\n")

    return "Please watch the server log!"

if __name__ == "__main__":
    app.run(debug=True)
