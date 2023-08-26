import smtplib
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText

# def send_email(recipient, subject, body):
  
#   msg = MIMEMultipart()
#   msg['subject'] = subject
#   msg['From'] = 'demo@gmail.com'
#   msg['To'] = recipient
#   msg.attach(MIMEText(body, 'plain'))
  
#   with smtplib.SMTP('smtp.gmail.com', 465) as server:
#     server.starttls()
#     server.login('demo@gmail.com', 'demo')
#     server.sendmail('wjawaid0342@gmail.com', recipient , msg.as_sring()) 
    
# def handle_email(message):  
  
#     subject =message['subject']
#     body =message.get_payload()
    
#     response="Thank you for your email. I will get back to you as soon as possible."
#     send_email(message['From'],subject, response)
    
# server =smtplib.SMTP('smtp.gmail.com', 465)
# server.starttls()
# server.login('demo@gmail.com', '"********')
# server.lister(1025)
  
# while True:
#   message = server.rec()
#   handle_email(message)
  

gmail_user = 'dmeo@gmail.com'
gmail_password = '"********'

sent_from = gmail_user
to = ['demo@gmail.com', '"********']
subject = 'OMG Super Important Message'
body = "Hey, what's up?- You"

email_text = """\
From: %s
To: %s
Subject: %s
%s
""" % (sent_from, ", ".join(to), subject, body)

 
for dest in to:
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("demo@gmail.com", "********")
    message = "Message_you_need_to_send"
    s.sendmail("sender_email_id", dest, message)
    s.quit()
    
# try:
#   server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
#   server.ehlo()
#   server.login(gmail_user, gmail_password)
#   server.sendmail(sent_from, to, email_text)
#   server.close()
#   print("Email sent!")
# except:
#   print("Something went wrong")
  