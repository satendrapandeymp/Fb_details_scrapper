from Auth import Constants

class DataExtractorForTableFormattedData:
    def __init__(self):
        pass

    def getTablesContainingData(self, parsedElement):
        tablesContainingData = parsedElement.find_all("table")
        if tablesContainingData and len(tablesContainingData) > 1:
            return tablesContainingData[1:]
        return []

    def getColumsContainingData(self, parsedElement):
        columnsContainingData = parsedElement.find_all("td")
        if columnsContainingData and len(columnsContainingData) > 1:
            return columnsContainingData
        return None


    def findLinkIfExists(self, parsedElement):
        linkvalue = parsedElement.find_all("a")
        if linkvalue and len(linkvalue) > 0:
            return linkvalue[0]["href"]
        return None

    def getDataFromColumns(self, columnsContainingData):
        key = columnsContainingData[0].text
        value = columnsContainingData[1].text
        linkToValue = self.findLinkIfExists(columnsContainingData[1])
        return {key: {"value": value, "linkToValue": linkToValue}}

    def getDataFromTable(self, tableContainingData):
        columnsContainingData = self.getColumsContainingData(tableContainingData)
        if (columnsContainingData):
            return self.getDataFromColumns(columnsContainingData)
        return None

    def extractTableFormattedData(self, parsedElement):
        extractedData = {}
        tablesContainingData = self.getTablesContainingData(parsedElement)
        for tableContainingData in tablesContainingData:
            dataFromTable = self.getDataFromTable(tableContainingData)
            if (dataFromTable):
                extractedData.update(dataFromTable)
        return extractedData  


class DataExtractorForHeaderFormattedData:
    def __init__(self):
        pass

    def getHeadersContainingData(self, parsedElement):
        headersContainingData = parsedElement.find_all("header")
        if headersContainingData and len(headersContainingData) > 1:
            return headersContainingData[1:]
        return []

    def getHeaderSectionsContainingData(self, parsedElement):
        headerSectionsContainingData = parsedElement.find_all("h3")
        if headerSectionsContainingData and len(headerSectionsContainingData) > 1:
            return headerSectionsContainingData
        return None

    def findLinkIfExists(self, parsedElement):
        linkvalue = parsedElement.find_all("a")
        if linkvalue and len(linkvalue) > 0:
            return linkvalue[0]["href"]
        return None

    def getDataFromHeaderSections(self, headerSectionsContainingData):
        key = headerSectionsContainingData[0].text
        value = headerSectionsContainingData[1].text
        linkToValue = self.findLinkIfExists(headerSectionsContainingData[0])
        return {key: {"value": value, "linkToValue": linkToValue}}

    def getDataFromHeader(self, headerContainingData):
        headerSectionsContainingData = self.getHeaderSectionsContainingData(headerContainingData)
        if (headerSectionsContainingData):
            return self.getDataFromHeaderSections(headerSectionsContainingData)
        return None

    def extractHeaderFormattedData(self, parsedElement):
        extractedData = {}
        headersContainingData = self.getHeadersContainingData(parsedElement)
        for headerContainingData in headersContainingData:
            dataFromHeader = self.getDataFromHeader(headerContainingData)
            if (dataFromHeader):
                extractedData.update(dataFromHeader)
        return extractedData  


class FriendListExtractor:
    def __init__(self):
        pass

    def getFriendIdFromUrl(self, urlOfFacebookProfile):
        if "?id=" in urlOfFacebookProfile:
            userId = urlOfFacebookProfile.split("?id=")[1].split("&")[0]
            return {"userId": userId, "isCustomUrl": False}
        userId = urlOfFacebookProfile.split("/")[1].split("?")[0]
        return {"userId": userId, "isCustomUrl": True}

    def getUrlFromElement(self, parsedElement):
        urlHolder = parsedElement.find_all("a")
        if (urlHolder) and len(urlHolder) > 0:
            return urlHolder[0]["href"]
        return None

    def getFriendListAsArray(self, parsedElements):
        listOfFacebookIds = []
        for parsedElement in parsedElements:
            tempFacebookUrl = self.getUrlFromElement(parsedElement)
            if (tempFacebookUrl):
                tempFacebookId = self.getFriendIdFromUrl(tempFacebookUrl)
                listOfFacebookIds.append(tempFacebookId)
        return listOfFacebookIds

    def getUrlForSeeMoreFriends(self, parsedElement):
        return self.getUrlFromElement(parsedElement)

