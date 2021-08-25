from pmail import Mail
from error import Error
from debug import Debug
from oracle import Oracle

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


class Init(Oracle, Debug, Mail, Error):
    
    def __init__(self):
       '''
         
       '''

       super(Oracle,self).__init__()
       super(Debug,self).__init__()
       super(Mail,self).__init__()
       super(Error,self).__init__()
        
    def _bootStrap(self):
        pass
        

        
        