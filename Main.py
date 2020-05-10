from bs4 import BeautifulSoup as Soup
from Auth import AuthHandler
from UserDetails import UserDetails
from DataExtraction import DataExtractor
from Utils import UrlBuilder
import sys, random

reload(sys)
sys.setdefaultencoding("utf-8")
testEnv = False if len(sys.argv) < 2 else True

authHandlerObject = AuthHandler.getAuthHandlerObject()
if not testEnv:
    authHandlerObject.authenticateUser()
opener = authHandlerObject.getUrlOpener()
urlBuilderObject = UrlBuilder.UrlBuilder()

def testGetHtmlAsTextForGivenUrl(url):
    if "rhythmpathak" in url:
        with open("TestData/test.html", "r") as reader:
            return reader.read()
        
    with open("TestData/test1.html", "r") as reader:
        return reader.read()

def getHtmlAsTextForGivenUrl(url):
    if (testEnv):
        return testGetHtmlAsTextForGivenUrl(url)
    response = opener.open(url)
    return response.read()

def getDetailsAboutGivenUser(id):
    url = urlBuilderObject.buildUrlForAboutSection(id)
    Page_Html = getHtmlAsTextForGivenUrl(url)
    newUser = UserDetails.UserDetails(Page_Html)
    return newUser.getAllUserData()
    
def getAllFriendsOfGivenUser(id):
    url = urlBuilderObject.buildUrlForFriendListSection(id)
    tempUserFriends = UserDetails.UserFriendList()
    while url:
        Page_Html = getHtmlAsTextForGivenUrl(url)
        tempUserFriends.setRawHtmlTextData(Page_Html)
        tempUserFriends.extractFriendList()
        url = tempUserFriends.getUrlForSeeMoreFriends()
    return tempUserFriends.getFriendList()

def runTest():
    print getDetailsAboutGivenUser({'isCustomUrl': True, 'userId': u'rhythmpathak'})
    print getAllFriendsOfGivenUser({'isCustomUrl': True, 'userId': u'rhythmp'})

if __name__ == "__main__":
    if testEnv:
        runTest()
    else:
        print getDetailsAboutGivenUser({'isCustomUrl': True, 'userId': u'narendra.pandey.9480'})
        print getAllFriendsOfGivenUser({'isCustomUrl': True, 'userId': u'narendra.pandey.9480'})