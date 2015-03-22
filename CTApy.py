__author__ = 'dougcampbell'

#CTA bus API docs http://www.transitchicago.com/assets/1/developer_center/BusTime_Developer_API_Guide.pdf

import ConfigParser
import requests
from xml.etree import ElementTree

class CTApy:
    def __init__(self, apikey):
        self.api_url_head = "http://www.ctabustracker.com/bustime/api/v1"
        self.api_url_tail = "key=%s" % (apikey)

    #get master time from CTA for syncing
    def get_ctatime(self):
        url = "%s/gettime?%s" % (self.api_url_head, self.api_url_tail)
        response = requests.get(url)
        tree = ElementTree.fromstring(response.content)
        #now do stuff to the tree to get time

    #get vehicle info. Takes a list of route numbers
    def get_vehicles(self, routes):
        routes_str = ','.join(routes)
        url = "%s/getvehicles?%s&rt=%s" %(self.api_url_head, self.api_url_tail, routes_str)
        #add requests and XML parsing

    #gets route info
    def get_routes(self):
        url = "%s/getroutes?%s" %(self.api_url_head, self.api_url_tail)
        #add requests and XML parsing

    #gets a single routes directions (ie: east or west bound)
    def get_route_dir(self, route):
        url = "%s/getdirections?%s&rt=%s" %(self.api_url_head, self.api_url_tail, route)

    #gets a list of stops giving a specific route and direction
    def get_stops(self, route, direction):
        url = "%s/getstops?%s&rt=%s&dir=%s" %(self.api_url_head, self.api_url_tail, route, direction)
        #format url spaces, API docs specify %20 for space
        url = url.replace(' ', '%20')
        #add requests and XML parsing

    #get route patterns
    #Use the getpatterns request to retrieve the set of geo-positional points and stops that when connected
    #can be used to construct the geo-positional layout of a pattern (i.e., route variation).
    def get_patters(self, route):
        url = "%s/getpatterns?%s&rt=%s" %(self.api_url_head, self.api_url_tail, route)

    #get a time prediction for a specifc route and stop. Can request multiple at once. Top will limit results
    def get_predictions(self, routes, stops, top=None):
        url = "%s/getpatterns?%s&rt=%s&stpid=%s" %(self.api_url_head, self.api_url_tail, routes, stops)

if __name__ == "__main__":
    #Read config file and get API key
    config = ConfigParser.ConfigParser()
    config.read("ctapy.conf")
    apikey = config.get("API", "bus_apikey")

    ctapy = CTApy(apikey)
    print ctapy.api_url_tail




