# -*- coding: utf-8 -*-
#use this pre installed library to send emails 

import smtplib 
host= "smtp.gmail.com"
port= 587
username="email@email.com"
password="########"


fromu="email@email.com"
tou="email@email.com"
email_conn=smtplib.SMTP(host,port)
#check if the connection is established or not
email_conn.ehlo()
#provides extra security layer or encryption to emails
email_conn.starttls()
#to login
email_conn.login(username,password)
#to send email
email_conn.sendmail(fromu,tou,"hi its a python based email")
#to logout form the server
email_conn.quit()
