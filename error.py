#!/usr/bin/env python
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------
# Name: 
# Purpose: clearing error class
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
from tabulate import tabulate
import socket
        
class Error():
    
    def __init__(self):

       self._errors = dict()       
       self._errors['error_001'] = 'err-001: trace instance variable not defined is init class inherited to base class'
       self._errors['error_002'] = 'err-002: valid trace output not selected' 
       self._errors['error_003'] = 'err-003: trace output method not defined' 
       self._errors['error_004'] = 'err-004: undefined trace message severity level'
       self._errors['error_005'] = 'err-005: error reading from directory'

       
    def _error(self, error_text='not defined', error_code='not defined', file_name='not defined', current_line_no='not defined', current_funtion_name='not defined', disposition='terminate', notify='mail'):
        
        super().__init__()
        if disposition not in {'teminate','no-tereminate'}:
           disposition='terminate' 
        
        print ('Error Analysis')
        print ('---------------')
        print ('error text    : ' + str(error_text))
        print ('error code    : ' + str(error_code))
        print ('file name     : ' + str(file_name))
        print ('line number   : ' + str(current_line_no))
        print ('function name : ' + str(current_funtion_name))
        print ('disposition   : ' + str(disposition))
        print ('notify        : ' + str(notify))
        
        self._setTracing('file')
        self._trace(text='error text    : ' + str(error_text), tabs=0, level=0, severity='error')
        self._trace(text='error code    : ' + str(error_code), tabs=0, level=0, severity='error')
        self._trace(text='file name     : ' + str(file_name), tabs=0, level=0, severity='error')
        self._trace(text='line number   : ' + str(current_line_no), tabs=0, level=0, severity='error')
        self._trace(text='function name : ' + str(current_funtion_name), tabs=0, level=0, severity='error')
        self._trace(text='disposition   : ' + str(disposition), tabs=0, level=0, severity='error')
        self._trace(text='notify        : ' + str(notify), tabs=0, level=0, severity='error')
        
        host = socket.gethostname()
        domain = None
        
        if (re.search(r"^([pPsS])",host)):
            domain = '?????'
        else:
            domain = '?????'      
        
        if notify == 'mail':
           self._sendSimpleMail( host + '@' + domain, self.notificationGroup, '!! ' + host + ' - ' + error_text, error_code)
           
           
        if disposition == 'terminate':
           sys.exit(0)   
           
        if disposition == 'no-terminate':
           print('setting trace output to both because of an error being encountered') 
           self._setTracing('both')       
        
      
