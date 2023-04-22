from libs.bflb_utils import printf
from configparser import ConfigParser


class ConfigObj:
    cnf_infile = None
    config = None

    def __init__(self, file):
        self.cfg_infile = file
        self.config = ConfigParser()
        self.config.read([file], 'UTF8')

    def has_option(self, section, key):
        return self.config.has_option(section, key)

    def get(self, section, key):
        return self.config.get(section, key)

    def set(self, section, key, value):
        return self.config.set(section, key, value)


class BFConfigParser:
    cfg_infile = None
    cfg_obj = None

    def __init__(self, file=None):
        self.cfg_infile = file
        if file is not None:
            self.cfg_obj = ConfigObj(self.cfg_infile)

    def read(self, file=None):
        printf('Reading configuration from file: %s' % file)
        self.cfg_infile = file
        if file is not None:
            self.cfg_obj = ConfigObj(self.cfg_infile)
        return self.cfg_obj

    def has_option(self, section, key):
        return self.cfg_obj.has_option(section, key)

    def get(self, section, key):
        ret = self.cfg_obj.get(section, key)
        if ret == '""':
            return ''
        return ret

    def set(self, section, key, value):
        self.cfg_obj.set(section, key, str(value))

    def write(self, file, mode):
        pass  # why would the flasher want to write the config file back?
