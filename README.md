Flask app to send mail using Gmail SMTP server.

To use,

1. Install: pip3 install -r requirements.txt
2. Configure gmail account by modifying MAIL_USERNAME & MAIL_PASSWORD in `.env`. You can get the MAIL_PASSWORD from `https://myaccount.google.com/apppasswords`.
3. Configure recipients by editing `data/recepients.txt`.
4. Configure email subject and content in `data/email_subject.txt` & `data/email_template.txt`
4. Run the flask server `python3 app.py`
5. Start sending email: Open browser, localhost:5000/send_to_all 