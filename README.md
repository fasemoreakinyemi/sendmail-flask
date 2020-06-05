Flask app to send mail using Gmail SMTP server.

To use,

1. Install: pip3 install -r requirements.txt
2. Configure gmail account by modifying MAIL_USERNAME & MAIL_PASSWORD  
3. Configure recipients by modifying list_of_address in function send_to_all.
4. flask run 
5. Start sending email: Open browser, localhost:5000/send_to_all 