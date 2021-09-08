#!/usr/bin/env python
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------
# Name: 
# Purpose: clearing global settings
#
# Author:      Dennis Spera
#
# Created:     01-Sept-2021
# RCS-ID:      $Id: $
# Copyright:   (c) 2021 
# Licence:     apache
#
#
#----------------------------------------------------------------------


import os

class Settings:
    
    '''
    '''
    def __init__(self):
       '''

       '''
        
       self.prodMailServer = ???????
       self.testMailserver = 'localhost' 
       
       self.notificationGroup = ??????
       self.serverConfig = ????????
       
       self.username = ???????
       self.passwordToken = 'dbm.dbpassword'
       self.tnsToken = 'dbm.dbname'
       self.encodingToken = 'utf-8'
       
    @staticmethod   
    def _fisRelease():
        
        output = os.popen('ls -alt /apps/clearing/pdir')
        line = output.readline()
        line = line.rstrip()
        _null, _file = line.split('>')
        release = os.path.basename(_file)
        return( 'fis-clearing-release: '+release)
        

    
    
    

       
       
       
