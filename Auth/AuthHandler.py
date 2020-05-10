from getpass import getpass
from GetObjects import UrlOpener
from re import search
from urllib import urlencode
from pickle import HIGHEST_PROTOCOL, load, dump
from os import path
from Constants import *

class AuthHandler:
    def __init__(self):
        self.urlOpenerObject = UrlOpener()
        self.urlOpener = self.urlOpenerObject.getOpener()
        self.authenticated = False

    def getCredentials(self):
        self.userName = raw_input("Username: ").strip()
        self.password = getpass("Password: ")
    
    def doLogin(self):
        print "Authenticating user " + self.userName
        self.urlOpener.open(FACEBOOK_LOGIN_URL)
        login_data = urlencode({"email" : self.userName, "pass" : self.password})
        self.urlOpener.open(FACEBOOK_LOGIN_URL, login_data)
        print "Authentication successfull for user " + self.userName
        self.authenticated = True
    
    def printErrorMessages(self):
        for errorMessage in self.validationErrorMessages:
            print errorMessage

    def authenticateUser(self):
        self.getCredentials()
        self.validateCredential()
        if len(self.validationErrorMessages) == 0:
            self.doLogin()
        else:
            self.printErrorMessages()
        
    def validateUsername(self):
        validationErrorMessages = []
        match = search(FACEBOOK_USERNAME_PATTERN, self.userName)
        if (not match):
            print "Validating passed for username, password..."
            validationErrorMessages.append(USERNAME_PATTERN_MISMATCH_ERROR)
        if ((len(self.userName) < FACEBOOK_USERNAME_MIN_LENGTH) or (len(self.userName) > FACEBOOK_USERNAME_MAX_LENGTH)):
            validationErrorMessages.append(USERNAME_LENGTH_MISMATCH_ERROR)
        return validationErrorMessages

    def validatePassword(self):
        validationErrorMessages = []
        if (len(self.password) < 8):
            validationErrorMessages.append(PASSWORD_LENGTH_MISMATCH_ERROR)
        return validationErrorMessages

    def validateCredential(self):
        print "Validating username, password..."
        self.validationErrorMessages = self.validateUsername()
        self.validationErrorMessages += self.validatePassword()
        return self.validateCredential

    def getUrlOpener(self):
        return self.urlOpener

def loadObject():
    with open(PICKEL_FILENAME, 'rb') as input:
        authHandlerObject = load(input)
    return authHandlerObject
    
def dumpObject(authHandlerObject):
    with open(PICKEL_FILENAME, 'wb') as output:
        dump(authHandlerObject, output, HIGHEST_PROTOCOL)

def getAuthHandlerObject():
    return AuthHandler()