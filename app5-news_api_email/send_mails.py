import smtplib, ssl
import os

def send_mail(message):
    host = "smtp.gmail.com"
    port = 465
    
    username = "copycatpresentsir@gmail.com"
    password = os.getenv("PASSWORD")
    
    receiver = "copycatpresentsir@gmail.com"
    context = ssl.create_default_context()
    
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
