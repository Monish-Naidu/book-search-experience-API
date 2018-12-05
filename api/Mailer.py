from flask_mail import Mail, Message
import os

mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": os.environ['iheartjewart@gmail.com'],
    "MAIL_PASSWORD": os.environ['monishnaidu']
}

class Mailer:
    def __init__(self, app):
        self.app = app
        self.app.config.update(mail_settings)

    def mail_this(self, email):
        mail = Mail(self.app)
        msg = Message(subject = "Your book is due soon.",
                      sender = self.app.config.get("MAIL_USERNAME"),
                      recipients = [email],  # need a way to find the emails...but her emails.....
                      body = "Your book is due soon")
        mail.send(msg)