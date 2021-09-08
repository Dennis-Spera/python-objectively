#!/usr/bin/env python
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------
# Name: 
# Purpose: clearing base class
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

from pmail import Mail
from error import Error
from debug import Debug
from oracle import Oracle
from settings import Settings
import re

'''
    to do:
    
    add is_server booleans
    add environmental class

    init class is a base class that inherits from other system functions
    from a clearing perspective as follows:
    
    from init import Init
    
    obj = Init()
    
    # get a database handle
    dbh = obj._dbh()
    
    # send an email with and attachment
    obj._sendMailAttachment(send_from, send_to, subject, text, file)
    obj._sendSimpleMail(send_from, send_to, subject, text)
    
    # raise error
    obj._error( error_text, error_code, file_name, current_line_no, current_funtion_name, dispostion,[send mail flag])
    
    # 
    obj._setTracing('both')
    obj._setLoggingLevel(5)
    obj._trace(text='test3',tabs=0,level=3)

'''


class Init(Oracle, Debug, Mail, Error, Settings):
    
    def __init__(self):
        
        classesTuple = Init.__mro__
        for className in classesTuple:
            m = re.match(r"^(.*)(['])(.*)(['])(.*)", str(className))           
            if m.group(3).strip() not in {'object'} and not re.search(r"^__main__", m.group(3).strip()) and not re.search(r"^init", m.group(3).strip()):
               file, cls = m.group(3).strip().split('.')
               instantiate=cls+'.__init__(self)'               
               eval(instantiate)
 

    
        
          