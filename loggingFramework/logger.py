
from logger_config import LoggerConfig
from logger_level import LoggerLevel
from logger_console_adapter import Console
from log_message import LogMessage

class Logger:
    _instance = None

    def __init__(self) -> None:
        if Logger._instance is not None:
            raise Exception("Logger object can't create multiple times")
        else:
            Logger._instance = self
            self.config = LoggerConfig(LoggerLevel.INFO, Console())

    @staticmethod
    def get_instance():
        if Logger._instance is None:
            Logger()

        return Logger._instance
    
    def set_config(self, config):
        self.config = config
    
    def set_logLevel(self, level):
        self.config.set_log_level(level)

    def log(self, level, message):
        if level.value == self.config.get_log_level().value or self.config.get_log_level() == LoggerLevel.DEBUG: #Value take from Enum 
            log_message = LogMessage(level, message)
            self.config.get_adapter().append(log_message)

    def debug(self, message):
        self.log(LoggerLevel.DEBUG, message)

    def info(self, message):
        self.log(LoggerLevel.INFO, message)
    
    def warning(self, message):
        self.log(LoggerLevel.WARNING, message)
    
    def error(self, message):
        self.log(LoggerLevel.ERROR, message)
    
    def critical(self, message):
        self.log(LoggerLevel.CRITICAL, message)
    
    def fatal(self, message):
        self.log(LoggerLevel.FATAL, message)

