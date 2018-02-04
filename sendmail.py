# -*- coding: utf-8 -*-
#use this pre installed library to send emails 


from smtplib import SMTP, SMTPConnectError, SMTPAuthenticationError, SMTPException
host= "smtp.gmail.com"
port= 587
username="xxx@gmail.com"
password="xxx"


fromu="xxx@gmail.com"
tou="xxx@gmail.com"
try:
    email_conn=SMTP(host,port)
    #check if the connection is established or not
    email_conn.ehlo()
    #provides extra security layer or encryption to emails
    email_conn.starttls()
    #to login
    email_conn.login(username,password)
    #to send email
    email_conn.sendmail(fromu,tou,"hi its a python based email")
except SMTPConnectError:
    print ("Error while connecting check internet or host port details")
except SMTPAuthenticationError:
    print ("Error while authenticating login credentials")
except :
    print ("Woopsy! Try Again Later")

#to logout form the server
email_conn.quit()
