import mimetypes
from email.message import EmailMessage
import os
import smtplib


def generate_email(sender, receiver, sub_line, body, attach):
    message = EmailMessage()

    message['From'] = sender
    message['To'] = receiver
    message['Subject'] = sub_line
    message.set_content(body)

    attach_path = attach
    attach_filename = os.path.basename(attach_path)

    mime_type, _ = mimetypes.guess_type(attach_path)
    mime_type, mime_subtype = mime_type.split('/', 1)

    with open(attach_path, 'rb') as pd:
        message.add_attachment(pd.read(),
                               maintype=mime_type,
                               subtype=mime_subtype,
                               filename=attach_filename
                               )

    return message


def generate_error_report(sender, receiver, sub_line, body):
    message = EmailMessage()

    message['From'] = sender
    message['To'] = receiver
    message['Subject'] = sub_line
    message.set_content(body)

    return message


def send_email(message):
    mail_server = smtplib.SMTP_SSL('localhost')
    mail_server.send_message(message)
    mail_server.quit()
