from time import asctime, localtime, time
from typing import Optional
# __metaclass__ 


class MyLogger:

    filename : str = "./MyLogs.log"
    filemode : str = "a"
    # file: Optional[file]= None
    file = None

    def __new__(cls):
        if not hasattr(cls, '_logger'):
            cls._logger = super(MyLogger, cls).__new__(cls)
        return cls._logger
    
    @classmethod
    def config(cls, filename=None, filemode=None):
        if filename:    
            cls.filename = filename
        if filemode:    
            cls.filemode = filemode
        
        if cls.file != None:
            cls.file.close()
        
        cls.file = open(cls.filename, cls.filemode)

    
    def baseLogMessage(self, type, message):
        if self.file is None:
            return
        
        preparedString = "[{}] {} : {} \n".format(type, asctime(localtime(time())), message)
        self.file.write(preparedString)
            
    def DEBUG(self, message):
        self.baseLogMessage("DEBUG", message)

    def INFO(self, message):
        self.baseLogMessage("INFO", message)

    def WARNING(self, message):
        self.baseLogMessage("WARNING", message)

    def ERROR(self, message):
        self.baseLogMessage("ERROR", message)

    def CRITICAL(self, message):
        self.baseLogMessage("CRITICAL", message)
    
    def __del__(self):
        if self.file is None:
            return
            
        self.file.close()


if __name__ == "__main__":
    log1 = MyLogger()
    log1.config("./log","w")
    log2 = MyLogger()
    log2.config("./log2","w")
    
    print(log1 == log2)
    print(f"log1:{log1} log2:{log2}")

    log1.CRITICAL("critical loooooog")
    log2.CRITICAL("sdfasdfsdf")