Flask app to send mail using Gmail SMTP server.

To use,

1. Install all dependencies: `pip3 install -r requirements.txt`.
2. Copy environment file `.env.example` to `.env`.
3. Configure gmail account by modifying `MAIL_USERNAME` & `MAIL_PASSWORD` in `.env`. `MAIL_USERNAME` is your Google email account. `MAIL_PASSWORD` is your account's app password. You can get the `MAIL_PASSWORD` with the following steps:

    a.) Activate two-step verification for your account: `https://myaccount.google.com/signinoptions/two-step-verification`.   
    b.) Setup app-password: `https://myaccount.google.com/apppasswords`.  

4. Configure recipients by editing `data/recepients.txt`.
5. Configure email subject and content in `data/email_subject.txt` & `data/email_template.txt`
6. Run the flask server `python3 app.py`
7. Start sending email: Open browser then go to localhost:5000/send_to_all. Or you can also use curl in your other terminal window/tab with this command: `curl localhost:5000/send_to_all`
