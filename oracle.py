import traceback, re, sys, os
import pprint, time
import cx_Oracle
from tabulate import tabulate


class Oracle:
    
    def __init__(self):
       '''
         to connect to local oracle database 
         
         from oracle import Oracle

         obj = Oracle()
         dbh = obj._dbh()
         
         user handle for executing query
       '''


    def _dbh(self):
       d = self._get_tuple()
       self.username = 'clradmin'  
       self.password = d['dbm.dbpassword']
       self.tnsname = d['dbm.dbname']
       self.encoding = 'utf-8'
       dh = cx_Oracle.connect(self.username, self.password, self.tnsname, encoding=self.encoding)
       return dh
    
    def _get_tuple(self):
        
        d = {}
        reading = False
        m = None
        
        fh = open('/apps/clearing/pdir/ositeroot/cfg/istparam.cfg')
        for line in fh:   
        
           if (re.search(r"(GROUP DATABASE)",line)):
              reading = True 
           
           if (reading):
              if  re.match(r"^([A-Za-z0-9_.]+)(\s)([A-Za-z0-9_.]+)$", line):
                  m = re.match(r"^([A-Za-z0-9_.]+)(\s)([A-Za-z0-9_.]+)$", line) 
                  d[m.group(1).strip()] = m.group(3).strip()
                  
           if (re.search(r"(END_GROUP)",line)):
              reading = False
        
        fh.close()
        return d
        