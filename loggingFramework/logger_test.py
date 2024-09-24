
from logger import Logger
from logger_level import LoggerLevel
from logger_file_adapter import FileAdapter
from logger_console_adapter import Console
from logger_config import LoggerConfig

class LoggerTest:
    
    @staticmethod
    def run():
        logger: Logger = Logger.get_instance() #By default Console adapter is assigned

        #console
        logger.debug("Hello world1")
        logger.error("Hello world2")
        logger.critical("Hello world3")
        logger.info("Hello world4")

        logger.set_logLevel(LoggerLevel.DEBUG)
        print("\n")
        logger.debug("Hello world1")
        logger.error("Hello world2")
        logger.critical("Hello world3")
        logger.info("Hello world4")



        #file descriptor
        logger.set_config(LoggerConfig(LoggerLevel.INFO, FileAdapter("./logTest.log")))
        print("\n")
        logger.debug("Hello world1")
        logger.error("Hello world2")
        logger.critical("Hello world3")
        logger.info("Hello world4")

        logger.set_logLevel(LoggerLevel.CRITICAL)
        print("\n")
        logger.debug("Hello world1")
        logger.error("Hello world2")
        logger.critical("Hello world3")
        logger.info("Hello world4")


LoggerTest.run()

