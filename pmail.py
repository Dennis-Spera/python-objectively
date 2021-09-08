#!/usr/bin/env python
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------
# Name: 
# Purpose: clearing email class
#
# Author:      Dennis Spera
#
# Created:     12-June-2018
# RCS-ID:      $Id: $
# Copyright:   (c) 2021 
# Licence:     apache
#
#
#----------------------------------------------------------------------
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
    def __init__(self):
       '''

       '''
    
    def _sendMailAttachment(self, send_from, send_to, subject, text, file):
        
        host = socket.gethostname()
        server = None
        
        if (re.search(r"^([pPsS])",host)):
            server = self.prodMailServer
        else:
            server = self.testMailserver 

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
            server = self.prodMailServer
        else:
            server = self.testMailserver 
            
        msg = MIMEMultipart()
        msg['From'] = send_from
        msg['To'] = send_to
        msg['Date'] = formatdate(localtime=True)
        msg['Subject'] = subject
        msg.attach(MIMEText(text))
    
        smtp = smtplib.SMTP(server)
        smtp.sendmail(send_from, send_to, msg.as_string())
        smtp.close()     
        