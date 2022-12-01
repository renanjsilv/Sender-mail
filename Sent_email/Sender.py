from email.message import EmailMessage
import ssl
import smtplib
#----------------------------------------------------------------------------------------------------------------------
def SentEmail(sender, password, receiver, subject, body):
    print()

    email_sender = sender
    email_password = password
    email_receiver = receiver

    Subject = subject
    Body    = body

    em = EmailMessage()
    em['From']    = email_sender
    em['To']      = email_receiver
    em['Subject'] = Subject
    em.set_content(Body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())
#----------------------------------------------------------------------------------------------------------------------

email_sender = input('From: ')
email_receiver = input('To: ')
email_password = input('Token: ')
Subject = input('Subject: ')
Body = input('Body: ')
Sender = SentEmail(email_sender, email_password, email_receiver, Subject, Body)
