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
                        

    def _error(self, error_text='not defined', error_code='not defined', file_name='not defined', current_line_no='not defined', current_funtion_name='not defined', disposition='terminate', notify='mail'):
        
        if disposition not in {'teminate','no-tereminate'}:
           disposition='terminate' 
        
        print ('Error Analysis')
        print ('---------------')
        print ('error text    : ' + error_text)
        print ('error code    : ' + error_code)
        print ('file name     : ' + file_name)
        print ('line number   : ' + current_line_no)
        print ('function name : ' + current_funtion_name)
        print ('disposition   : ' + disposition)
        print ('notify        : ' + notify)
        
        self._setTracing('file')
        self._trace(text='error text    : ' + error_text, tabs=0, level=0, severity='error')
        self._trace(text='error code    : ' + error_code, tabs=0, level=0, severity='error')
        self._trace(text='file name     : ' + file_name, tabs=0, level=0, severity='error')
        self._trace(text='line number   : ' + current_line_no, tabs=0, level=0, severity='error')
        self._trace(text='function name : ' + current_funtion_name, tabs=0, level=0, severity='error')
        self._trace(text='disposition   : ' + disposition, tabs=0, level=0, severity='error')
        self._trace(text='notify        : ' + notify, tabs=0, level=0, severity='error')
        
        host = socket.gethostname()
        domain = None
        
        if (re.search(r"^([pPsS])",host)):
            domain = 'planetpayment.net'
        else:
            domain = 'planetpayment.com'      
        
        if notify == 'mail':
           self._sendSimpleMail( host + '@' + domain, 'system email account', '!! ' + host + ' - ' + error_text, error_code)
           
           
        if disposition == 'terminate':
           sys.exit(0)   
           
        if disposition == 'no-terminate':
           print('setting trace output to both because of an error being encountered') 
           self._setTracing('both')       
        
      
