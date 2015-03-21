__author__ = 'dougcampbell'

import ConfigParser


class CTApy:

    def _init_(self):
        #Read config file and get API key
        config = ConfigParser.ConfigParser()
        config.read("api.conf")
        self.apikey = config.get("API", "apikey")





