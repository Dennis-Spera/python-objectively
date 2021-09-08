#!/usr/bin/env python
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------
# Name: 
# Purpose: clearing debug class
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
from inspect import currentframe, getframeinfo, getouterframes
import logging, logging.handlers


class Debug:
    
    def __init__(self):
       '''

       '''
       
       
    def _trace(self, text, tabs=0, level=0, severity='info'):
         cf = currentframe()
         calframe = getouterframes(cf, 2)        
         
         logger = self._setLoggingFile()
         
         
         try:
           if self.traceOutput == 'un-defined':       
              pass
         except:
              print ('traceOutput not set defaulting to terminal and loggingLevel of 5')
              self.traceOutput = 'terminal'
              self.loggingLevel = 5
         
         if self.traceOutput == 'un-defined':
            self._error(self._errors['error_002'], 
                        'err-002', 
                        getframeinfo(cf).filename, 
                        str(cf.f_lineno), 
                        sys._getframe().f_code.co_name, 
                        'terminate', 
                        notify='void')
            
         if self.traceOutput not in {'both','terminal','none','file'}:
            self._error(self._errors['error_003'], 
                       'err-003', 
                       getframeinfo(cf).filename, 
                       str(cf.f_lineno), 
                       sys._getframe().f_code.co_name, 
                       'terminate', 
                       notify='void') 


         if severity not in {'info','debug','critical','error','warning'}:
            self._error(self._errors['error_004'], 
                       'err-004', 
                       getframeinfo(cf).filename, 
                       str(cf.f_lineno), 
                       sys._getframe().f_code.co_name, 
                       'terminate', 
                       notify='void') 
        
         if self.traceOutput == 'terminal' or self.traceOutput == 'both':
            
            if level < self.loggingLevel:
                 
              for i in range(1,tabs+1): 
                  print ("\t",end='')
              print ('% ' +  str(os.path.basename(calframe[1][1]))  + '[' + str(calframe[1][2]) + '] : ' + str(text) )
              
              
              
         if self.traceOutput == 'file' or self.traceOutput == 'both':
            
            if level < self.loggingLevel:  
               optStr = 'logger.setLevel(logging.' + severity.upper() + ')'
               eval(optStr)         
               cmdStr =  'logger.' + severity + '(str(text))'               
               eval(cmdStr)   
               # set back to default of INFO
               logger.setLevel(logging.INFO)

    def _setLoggingLevel(self, level=0):             
        self.loggingLevel = level
        
        
    def _setLoggingFile (self):
        file='/apps/clearing/pdir/log/debug/console.log'
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler = logging.handlers.RotatingFileHandler( file, maxBytes=1048576, backupCount=5)
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
        return self.logger    
        
    def _enableTracing(self):             
        self.trace = True
        self.traceOutput = 'un-defined'
        
    def _disableTracing(self):
        self.trace = False   
        
    def _setTracing(self, output):
        cf = currentframe()
        
        self._enableTracing()
        
        if not self.trace:
           self._error(self._errors['err-001'], 
                       'err-001', 
                       getframeinfo(cf).filename, 
                       str(cf.f_lineno), 
                       sys._getframe().f_code.co_name, 
                       'terminate', 
                       notify='void') 
        
        if  output in ('none','terminal','file','both'):                 
            self.traceOutput = output
        else:
           self._error('trace output method not defined', 
                       'err-002', 
                        getframeinfo(cf).filename, 
                        cf.f_lineno, 
                        sys._getframe().f_code.co_name, 
                        'terminate', 
                        notify='void')          
            
            
            
            