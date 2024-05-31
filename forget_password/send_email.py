import smtplib
from email.mime.text import MIMEText
from django.urls import reverse

def send_email(sender_email, sender_password, recipient_user, content):
    recipient_email = recipient_user.email
    subject = "Password Update Request"
    reset_url = f"http://your-domain.com{reverse('update_password')}?email={recipient_email}"
    message_content = f"{content}\n\nPlease click <a href='{reset_url}'>here</a> to update your password."

    message = MIMEText(message_content, 'html')
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

