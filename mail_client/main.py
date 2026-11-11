import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart



with open('password.txt', 'r') as f:
    password = f.read().strip()

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)

server.login('junaid.alam2@gmail.com', password)

msg = MIMEMultipart()
msg['From'] = 'Junaid Alam <junaid.alam2@gmail.com>'
msg['To'] = 'alamobile@gmail.com'
msg['Subject'] = 'Just A Test'

with open('message.txt', 'r') as f:
    message = f.read()


msg.attach(MIMEText(message, 'plain'))

filename = 'image.avif'
with open(filename, 'rb') as attachment:
    p = MIMEBase('application', 'octet-stream')
    p.set_payload(attachment.read())

encoders.encode_base64(p)

p.add_header(
    'Content-Disposition', 
    f'attachment; filename="{filename}"')

msg.attach(p)

server.send_message(msg)

server.quit()
