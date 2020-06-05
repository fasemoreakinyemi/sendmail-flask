import os
import sys
import datetime

from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)

def send_mail(target_address):
    mail = Mail(app)

    msg = Message("Akses Webinar 'Sekolah PhD itu Gratis?'",
                sender="martinluttap@gmail.com",
                recipients=[target_address])

    msg.body ="""
Hi,

Terimakasih sudah mendaftar untuk webinar "Sekolah PhD itu Gratis? Tanya Jawab Bersama Kakak-Kakak Mahasiswa PhD Indonesia di Amerika Serikat".
Untuk mengakses webinar silahkan gunakan link berikut:

Link Zoom:
Link YouTube:

Link YouTube Alternatif 1: 
Link YouTube Altrenatif 2:

Kami menerima 900 lebih pendaftaran, namun kami tidak bisa menampung semuanya dalam platform yang kami gunakan. Hanya 100 orang saja yang bisa masuk ke dalam room Zoom, sisanya dapat menyaksikan dan mengajukan pertanyaan di Live Youtube.

Kami tunggu kehadiranmu!

Terimakasih
-- Fadhil, Martin, Daniar, Bella, Titan
"""

    mail.send(msg)
    print("Message sent to " + target_address)

    return None

@app.route('/send_to_all')
def send_to_all():
    # Send ticket to the address
    app.config['MAIL_SERVER']='smtp.gmail.com'
    app.config['MAIL_PORT'] = 465
    app.config['MAIL_USERNAME'] = 'martinluttap@gmail.com'
    app.config['MAIL_PASSWORD'] = 'hbhftcdinzjmnapo'
    app.config['MAIL_USE_TLS'] = False
    app.config['MAIL_USE_SSL'] = True

    list_of_address = ["martinluttap@gmail.com", "sukaberkhayal@gmail.com"]

    try:
        for address in list_of_address:
            send_mail(address)
    finally:
        return "Please watch the server log!"

if __name__ == "__main__":
    app.run(debug=True)
