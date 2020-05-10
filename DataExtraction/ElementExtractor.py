from bs4 import BeautifulSoup as Soup

class ElementExtractorForPersonDetails:

    def __init__(self):
        pass
    
    def setNewHtmlDocument(self, rawHtmlDocumentAsText):
        self.rawHtmlDocumentAsText = rawHtmlDocumentAsText
        self.parsedHtmlDocument = Soup(rawHtmlDocumentAsText, "html.parser")
        self.parsedRootElement = self.getRootElement()

    def getRootElement(self):
        parsedRootElements = self.parsedHtmlDocument.find_all("div", {"id": "root"})
        if (not parsedRootElements) or len(parsedRootElements) == 0:
            print "Can't find root element"
            return None
        return parsedRootElements[0]

    def getContactInfoElement(self):
        parsedContactInfoElements = self.parsedRootElement.find_all("div", {"id": "contact-info"}) if self.parsedRootElement else []
        if (not parsedContactInfoElements) or len(parsedContactInfoElements) == 0:
            print "Can't find contact info element"
            return None
        return parsedContactInfoElements[0]
    
    def getBasicInfoElement(self):
        parsedBasicInfoElements = self.parsedRootElement.find_all("div", {"id": "basic-info"}) if self.parsedRootElement else []
        if (not parsedBasicInfoElements) or len(parsedBasicInfoElements) == 0:
            print "Can't find basic info element"
            return None
        return parsedBasicInfoElements[0]

    def getFamilyInfoElement(self):
        parsedFamilyInfoElements = self.parsedRootElement.find_all("div", {"id": "family"}) if self.parsedRootElement else []
        if (not parsedFamilyInfoElements) or len(parsedFamilyInfoElements) == 0:
            print "Can't find family info element"
            return None
        return parsedFamilyInfoElements[0]

    def getLivingInfoElement(self):
        parsedLivingInfoElements = self.parsedRootElement.find_all("div", {"id": "living"}) if self.parsedRootElement else []
        if (not parsedLivingInfoElements) or len(parsedLivingInfoElements) == 0:
            print "Can't find living info element"
            return None
        return parsedLivingInfoElements[0]


class ElementExtractorForFriendList:
    def __init__(self):
        pass
    
    def setNewHtmlDocument(self, rawHtmlDocumentAsText):
        self.rawHtmlDocumentAsText = rawHtmlDocumentAsText
        self.parsedHtmlDocument = Soup(rawHtmlDocumentAsText, "html.parser")
        self.parsedRootElement = self.getRootElement()

    def getRootElement(self):
        parsedRootElements = self.parsedHtmlDocument.find_all("div", {"id": "root"})
        if (not parsedRootElements) or len(parsedRootElements) == 0:
            print "Can't find root element"
            return None
        return parsedRootElements[0]

    def getFriendListElements(self):
        parsedFriendListElements = self.parsedRootElement.find_all("table", {"role":"presentation"})
        if (not parsedFriendListElements) or len(parsedFriendListElements) == 0:
            print "Can't find elements for friend list"
            return None
        return parsedFriendListElements

    def getMoreFriendListElementForAllFriends(self):
        ParsedSeeMoreElement = self.parsedRootElement.findAll("div", {"id":"m_more_friends"})
        if (not ParsedSeeMoreElement) or len(ParsedSeeMoreElement) == 0:
            print "Can't find elements for more friend list"
            return None
        return ParsedSeeMoreElement[0]

    def getMoreFriendListElementForMutualFriend(self):
        ParsedSeeMoreElement = self.parsedRootElement.findAll("div", {"id":"m_more_mutual_friends"})
        if (not ParsedSeeMoreElement) or len(ParsedSeeMoreElement) == 0:
            print "Can't find elements for more friend list"
            return None
        return ParsedSeeMoreElement[0]

    def getMoreFriendListElement(self):
        ParsedSeeMoreElement = self.getMoreFriendListElementForAllFriends()
        ParsedSeeMoreMutualElement = self.getMoreFriendListElementForMutualFriend()
        if (not ParsedSeeMoreElement) and (not ParsedSeeMoreMutualElement):
            print "Can't find elements for more friend list"
            return None
        return ParsedSeeMoreElement if (ParsedSeeMoreElement) else ParsedSeeMoreMutualElement