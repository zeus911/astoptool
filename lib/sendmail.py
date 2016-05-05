#!/usr/local/bin/python 
#-*- coding:utf-8 -*-
import sys,os
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders
def sendmail(html,emailaddress,mailSubject,from_address="monitor@game-reign.com",files=[]):
        mail_list=emailaddress.split(",")
        msg=MIMEMultipart()
        msg['Accept-Language']='zh-CN'
        msg['Accept-Charset']= 'ISO-8859-1,utf-8'
        msg['From']=from_address
        msg['to']=";".join(mail_list)
        msg['Subject']=mailSubject.decode("utf-8")
        txt=MIMEText(html,'html','utf-8')
        txt.set_charset('utf-8')
        msg.attach(txt)
        smtp=smtplib.SMTP("mail.game-reign.com")
        #添加附件
        for f in files:
            part = MIMEBase('application', 'octet-stream') #'octet-stream': binary data   
            part.set_payload(open(f, 'rb').read())   
            encoders.encode_base64(part)   
            part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(f))   
            msg.attach(part)   
        smtp.sendmail(msg["From"],mail_list,msg.as_string())
        smtp.close()


