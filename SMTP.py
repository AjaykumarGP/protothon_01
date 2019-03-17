import smtplib
from email.mime.text import MIMEText

smtp_host="smtp.gmail.com"
smtp_port=465
user="ajay.19.1@protosem.tech"
password="***********"
sender="ajaykumar.16cs@kct.ac.in"
targets=["gokul.19.1@protosem.tech","ajaykumar11998@gmail.com"]

m=MIMEText("Hey dude, what's happening?")
m["subject"]="padichu paar"
m["from"]=sender
m["to"]=", ".join(targets)

ser=smtplib.SMTP_SSL(smtp_host,smtp_port)
ser.login(user,password)
ser.sendmail(sender,targets,m.as_string())
ser.quit()




