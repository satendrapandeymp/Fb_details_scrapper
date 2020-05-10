from Auth import Constants

class UrlBuilder:
    def __init__(self):
        pass

    def buildUrlForFriendListSection(self, id):
        if (id["isCustomUrl"]):
            return Constants.FACEBOOK_FRIENDS_URL.format(id["userId"])
        return Constants.OTEHR_FACEBOOK_FRIENDS_URL.format(id["userId"])

    def buildUrlForAboutSection(self, id):
        if (id["isCustomUrl"]):
            return Constants.FACEBOOK_ABOUT_URL.format(id["userId"])
        return Constants.OTEHR_FACEBOOK_ABOUT_URL.format(id["userId"])