from DataExtraction import ElementExtractor, DataExtractor
from Auth import Constants

elementExtractorForPersonDetails = ElementExtractor.ElementExtractorForPersonDetails()
elementExtractorForFriendList = ElementExtractor.ElementExtractorForFriendList()
dataExtractorForTableFormattedData = DataExtractor.DataExtractorForTableFormattedData()
dataExtractorForHeaderFormattedData = DataExtractor.DataExtractorForHeaderFormattedData()
dataExtractorForFriendsList = DataExtractor.FriendListExtractor()

class UserDetails:
    def __init__(self, rawHtmlTextData):
        self.userDetails = {}
        self.rawHtmlTextData = rawHtmlTextData
        elementExtractorForPersonDetails.setNewHtmlDocument(rawHtmlTextData)

    def getUserBasicInfo(self):
        userBasicInfoElement = elementExtractorForPersonDetails.getBasicInfoElement()
        userBasicInfoData = dataExtractorForTableFormattedData.extractTableFormattedData(userBasicInfoElement)
        self.userDetails.update({"basicInfo": userBasicInfoData})

    def getUserContactInfo(self):
        userContactInfoElement = elementExtractorForPersonDetails.getContactInfoElement()
        userContactInfoData = dataExtractorForTableFormattedData.extractTableFormattedData(userContactInfoElement)
        self.userDetails.update({"contactInfo": userContactInfoData})

    def getUserLivingInfo(self):
        userLivingInfoElement = elementExtractorForPersonDetails.getLivingInfoElement()
        userLivingInfoData = dataExtractorForTableFormattedData.extractTableFormattedData(userLivingInfoElement)
        self.userDetails.update({"livingInfo": userLivingInfoData})

    def getUserFamilyInfo(self):
        userFamilyInfoElement = elementExtractorForPersonDetails.getFamilyInfoElement()
        userFamilyInfoData = dataExtractorForHeaderFormattedData.extractHeaderFormattedData(userFamilyInfoElement)
        self.userDetails.update({"familyInfo": userFamilyInfoData})

    def getAllUserData(self):
        self.getUserBasicInfo()
        self.getUserContactInfo()
        self.getUserLivingInfo()
        self.getUserFamilyInfo()
        return self.userDetails

class UserFriendList:
    def __init__(self):
        self.friendList = []

    def setRawHtmlTextData(self, rawHtmlTextData):
        self.rawHtmlTextData = rawHtmlTextData
        elementExtractorForFriendList.setNewHtmlDocument(rawHtmlTextData)

    def extractFriendList(self):
        parsedFriendListElements = elementExtractorForFriendList.getFriendListElements()
        if parsedFriendListElements:
            self.friendList += dataExtractorForFriendsList.getFriendListAsArray(parsedFriendListElements) 

    def getFriendList(self):
        return self.friendList

    def getUrlForSeeMoreFriends(self):
        parsedSeeMoreFriendsElement = elementExtractorForFriendList.getMoreFriendListElement()
        if parsedSeeMoreFriendsElement:
            return Constants.FACEBOOK_BASE_URL_WITHOUT_SLASH + dataExtractorForFriendsList.getUrlForSeeMoreFriends(parsedSeeMoreFriendsElement)
        return None

    