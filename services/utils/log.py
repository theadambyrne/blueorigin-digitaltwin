import logging
from logging import StreamHandler, FileHandler, DEBUG
from colorlog import ColoredFormatter
from utils.config import ConfigParser

config = ConfigParser()


class Log:
    _instance = None

    def __new__(cls, name, level=DEBUG):
        if cls._instance is None:
            cls._instance = super(Log, cls).__new__(cls)
            cls._instance.logger = logging.getLogger(name)
            cls._instance.logger.setLevel(level)

            # Console handler
            console_handler = StreamHandler()
            console_handler.setLevel(level)

            formatter = ColoredFormatter(
                "%(asctime)s %(log_color)s[%(levelname)s]%(reset)s - %(name)s - %(message)s ",
                datefmt="%H:%M:%S",
                log_colors={
                    "DEBUG": "cyan",
                    "INFO": "green",
                    "WARNING": "yellow",
                    "ERROR": "red",
                    "CRITICAL": "red,bg_white",
                },
            )
            console_handler.setFormatter(formatter)

            # File handler
            log_file = config.get("logging", "log_file")
            file_handler = FileHandler(log_file)
            file_handler.setLevel(level)
            file_handler.setFormatter(logging.Formatter("%(asctime)s [%(levelname)s] - %(name)s - %(message)s"))

            # Add both handlers to the logger
            cls._instance.logger.addHandler(console_handler)
            cls._instance.logger.addHandler(file_handler)

        return cls._instance

    def debug(self, msg):
        self.logger.debug(msg)

    def info(self, msg):
        self.logger.info(msg)

    def warning(self, msg):
        self.logger.warning(msg)

    def error(self, msg):
        self.logger.error(msg)

    def critical(self, msg):
        self.logger.critical(msg)
