import urllib2, cookielib
from Constants import *
from os import path

class UrlOpener:

    def __init__(self):
        self.preAutheticated = False
        self.cookieJar = self.getCookieJar()
        self.buildOpener()

    def buildOpener(self):
        urlOpener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cookieJar))
        urlOpener.addheaders = [('User-Agent', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0')]
        self.urlOpener = urlOpener

    def getOpener(self):
        return self.urlOpener

    def getCookieJar(self):
        cookieLibObject = cookielib.LWPCookieJar()
        if (path.exists(PICKEL_FILENAME)):
            self.preAutheticated = True
            return cookieLibObject.load(PICKEL_FILENAME)
        return cookieLibObject

    def isPreAuthenticated(self):
        return self.preAutheticated