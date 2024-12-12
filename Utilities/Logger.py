import logging

class log_generator_class:
    @staticmethod
    def loggen_method():
        logger = logging.getLogger() #called the logger method to create logg
        log_file = logging.FileHandler(".\\Logs\\CredKart_Automation_log")  #here are given log files path
        log_format = logging.Formatter("%(asctime)s - %(levelname)s - %(funcName)s - %(lineno)d - %(message)s")# here have given log format
        log_file.setFormatter(log_format) #here set the log format
        logger.addHandler(log_file) #added log file to logger
        logger.setLevel(logging.INFO) #here set the log level
        return logger


    #debug
    #info
    #warning
    #error
    #critical
