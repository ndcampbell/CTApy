__author__ = 'dougcampbell'

import ConfigParser


class CTApy:
    def __init__(self, apikey):
        self.api_url_head = "http://www.ctabustracker.com/bustime/api/v1/"
        self.api_url_tail = "?key=%s" % (apikey)

#Read config file and get API key
config = ConfigParser.ConfigParser()
config.read("api.conf")
apikey = config.get("API", "apikey")
print apikey

ctapy = CTApy(apikey)
print ctapy.api_url_tail




