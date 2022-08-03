#send a plain text email
import smtplib
from email.mime.text import MIMEText
smtp_ssl_host = 'smtp.gmail.com'  # smtp.mail.yahoo.com
smtp_ssl_port = 465
username = 'user name or sender email'
password = 'password' # read how to get thids password in readme text
sender = 'sender email'
targets = ['target email']
msg = MIMEText('Hi, Im your bot it is a automatic message please do not reply')
msg['Subject'] = 'yur message subject'
msg['From'] = sender
msg['To'] = ', '.join(targets)

server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
server.login(username, password)
server.sendmail(sender, targets, msg.as_string())
server.quit()

#Solve smtplib.SMTPAuthenticationError: Username and Password not accepted Error
