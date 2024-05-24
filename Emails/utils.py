# email_utils.py

import smtplib
from email.mime.text import MIMEText

def send_email(sender_email, sender_password, recipient_email, subject, content):
    message = MIMEText(content)
    message['From'] = sender_email
    message['To'] = recipient_email
    message['Subject'] = subject

    try:
        with smtplib.SMTP('smtp.example.com', 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipient_email, message.as_string())
    except Exception as e:
        raise RuntimeError('An error occurred while sending the email: ' + str(e))

