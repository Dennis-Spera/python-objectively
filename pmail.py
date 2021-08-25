import traceback, re, sys, os
import pprint, time
import cx_Oracle
from tabulate import tabulate
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
import smtplib
import socket


class Mail:
    
    '''
    '''
    def _sendMailAttachment(self, send_from, send_to, subject, text, file):
        
        
        host = socket.gethostname()
        server = None
        
        if (re.search(r"^([pPsS])",host)):
            server = 'prod network'
        else:
            server = 'localhost' 
        

        msg = MIMEMultipart()
        msg['From'] = send_from
        msg['To'] = send_to
        msg['Date'] = formatdate(localtime=True)
        msg['Subject'] = subject
    
        msg.attach(MIMEText(text))
        Name = None
        files = []
        files.append(file) 
        for f in files:
            with open(f, "rb") as fil:
                part = MIMEApplication(
                    fil.read(),
                    Name=os.path.basename(f)
                )
            #--------------------------------
            part['Content-Disposition'] = 'attachment; filename="%s"' % Name
            msg.attach(part)
    
        smtp = smtplib.SMTP(server)
        smtp.sendmail(send_from, send_to, msg.as_string())
        smtp.close()       
        
        
        
    def _sendSimpleMail(self, send_from, send_to, subject, text):
    
        host = socket.gethostname()
        server = None
        
        if (re.search(r"^([pPsS])",host)):
            server = 'prod network'
        else:
            server = 'localhost' 
            
        msg = MIMEMultipart()
        msg['From'] = send_from
        msg['To'] = send_to
        msg['Date'] = formatdate(localtime=True)
        msg['Subject'] = subject
        msg.attach(MIMEText(text))
    
        smtp = smtplib.SMTP(server)
        smtp.sendmail(send_from, send_to, msg.as_string())
        smtp.close()     
        
