# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 15:34:54 2018

@author: Ayush Sharma
"""
# =============================================================================
# adding support for html rendering and enhancing msg templating
# =============================================================================
from smtplib import SMTP
from email.mime.multipart import MIMEMultipart as MP
from email.mime.text import MIMEText as MT
host= "smtp.gmail.com"
port= 587
username=""
password=""
fromu=""
tou=""

conn=SMTP(host,port)
conn.ehlo()
conn.starttls()
#to login
conn.login(username,password)
#using mime data to format the text alternative is the content-type
mimeobj= MP("alternative")
mimeobj['Subject'] = "Hello There"
mimeobj['From']= fromu
mimeobj['To']= tou
#mimeobj.__dict__ use this to know more abt mime object
htmlmsgtext="""
<html>
<head></head>
<body>
<br>
<b>Hello there!</b> 
<br>using python with html formatting to send you an <a href="mailto:abc@bcd.com" target="_top"> email!</a>
<img src="https://res.cloudinary.com/teepublic/image/private/s--GSPyTYha--/t_Preview/b_rgb:c62b29,c_limit,f_jpg,h_630,q_90,w_630/v1515385863/production/designs/2262607_1.jpg">
</body>
</html>
"""
msg=MT(htmlmsgtext,"html")
mimeobj.attach(msg)
conn.sendmail(fromu,tou,msg.as_string())

conn.quit()