Flask app to send mail using Gmail SMTP server.

To use,

1. Install: pip3 install -r requirements.txt
2. Copy environment file `.env.example` to `.env`
`cp .env.example .env`
3. Configure gmail account by modifying MAIL_USERNAME & MAIL_PASSWORD in `.env`. MAIL_PASSWORD is your account's app password. 
 
You can get the MAIL_PASSWORD from:  
a.) Activate two-step verification for your account: `https://myaccount.google.com/u/2/signinoptions/two-step-verification`. 
b.) Setup app-password: `https://myaccount.google.com/apppasswords`.  

4. Configure recipients by editing `data/recepients.txt`.
5. Configure email subject and content in `data/email_subject.txt` & `data/email_template.txt`
6. Run the flask server `python3 app.py`
7. Start sending email: Open browser, localhost:5000/send_to_all 
