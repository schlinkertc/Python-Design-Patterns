class SingletonObject(object):
    class __SingletonObject():
        def __init__(self,file_name):
            self.file_name = file_name
            
        def __str__(self):
            return "{0!r} {1}".format(self,self.val)
        
        def _write_log(self,level,msg):
            """Writes a message to the file_name for a specific Logger instance"""
            with open(self.file_name,'a') as log_file:
                log_file.write("[{0}] {1}\n".format(level,msg))
            
        def critical(self,msg):
            self._write_log('CRITICAL',msg)

        def error(self,msg):
            self._write_log('ERROR',msg)

        def info(self,msg):
            self._write_log('INFO',msg)
            
    instance = None
    
    def __new__(cls):
        if not SingletonObject.instance:
            SingletonObject.instance = SingletonObject.__SingletonObject
        return SingletonObject.instance
    
    def __getattr__(self,name):
        return getattr(self.instance,name)
    
    def __setattr__(self,name):
        return setattr(self.instance,name)
    
    