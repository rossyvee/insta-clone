from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

def send_email(username,receiver):
    subject='Welcome to LikemeU'
    mail_content=render_to_string('emails/welcome.html',{'username':username})
    alt_content=render_to_string('emails/welcome.txt',{'username':username})
    sender='michaelogaye87@gmail.com'
    msg=EmailMultiAlternatives(subject,alt_content,sender,[receiver])
    msg.attach_alternative(mail_content,'text/html')
    msg.send()