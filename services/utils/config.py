import configparser
import os


class ConfigParser:
    _instance = None

    def __new__(
        cls, config_file=os.path.join(os.path.dirname(__file__), "../config.cfg")
    ):
        if cls._instance is None:
            cls._instance = super(ConfigParser, cls).__new__(cls)
            cls._instance.config = configparser.ConfigParser()
            cls._instance.config.read(config_file)
        return cls._instance

    def get(self, section, key, default=None):
        try:
            return self.config.get(section, key)
        except (configparser.NoSectionError, configparser.NoOptionError):
            return default

    def getint(self, section, key, default=None):
        try:
            return self.config.getint(section, key)
        except (configparser.NoSectionError, configparser.NoOptionError):
            return default

    def getfloat(self, section, key, default=None):
        try:
            return self.config.getfloat(section, key)
        except (configparser.NoSectionError, configparser.NoOptionError):
            return default

    def getboolean(self, section, key, default=None):
        try:
            return self.config.getboolean(section, key)
        except (configparser.NoSectionError, configparser.NoOptionError):
            return default
