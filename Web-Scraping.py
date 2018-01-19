import urllib2, time, sys, urllib, cookielib
from getpass import getpass
from bs4 import BeautifulSoup as Soup

reload(sys)
sys.setdefaultencoding("utf-8")

cj = cookielib.CookieJar()

opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
opener.addheaders = [('User-Agent', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0')]

username = sys.argv[1]
password = sys.argv[2]

opener.open('https://www.facebook.com/login')

login_data = urllib.urlencode({'email' : username, 'pass' : password})

opener.open('https://www.facebook.com/login', login_data)

# Done Authenticating till here
arr = []
arr1 = []
baseurl = sys.argv[3]
baseurl = 'https://m.facebook.com/' + baseurl
arr.append(baseurl)

print baseurl

File_name = "Data.csv"
File_name1 = "Data1.csv"
f = open(File_name, "w+")
f.write("Name, B'Day, Gender, Home Town, Curr City, Mobile no. \n")
f.close()

def final(url, Name, f):

    if 'id' in url:
        url1 = url.split("&")[0]
        url = url1 + "&v=info"
    else:
        url1 = url.split("?")[0]
        url = url1 + "/about"

    if url in arr:
        return 1
    else:
        arr.append(url)

    response = opener.open(url)
    Page_Html = response.read()

    Parsed_html = Soup(Page_Html, "html.parser")

    Mobiles = Parsed_html.findAll("div", {"title":"Mobile"})
    Genders = Parsed_html.findAll("div", {"title":"Gender"})
    Birthdays = Parsed_html.findAll("div", {"title":"Birthday"})
    Curr_citys = Parsed_html.findAll("div", {"title":"Current City"})
    Home_towns = Parsed_html.findAll("div", {"title":"Hometown"})

    flag = 0
    temp = ""
    try:

        for Mobile in Mobiles:
            print Mobile
            Number = Mobile.findAll("td")[1].text
            Number = Number.replace(" ", "") + ","
            temp += Number
            flag = 1

    except:
        print "No mob no"

    try:
        Gender = Genders[0].text
        Gender = Gender.split("ender")[1]
    except:
        Gender = "NA"

    try:
        Birthday = Birthdays[0].text
        Birthday = Birthday.split("irthday")[1].replace(',', "-")
    except:
        Birthday = "NA"

    try:
        Curr_city = Curr_citys[0].text
        Curr_city = Curr_city.split("urrent City")[1].replace(',', "-")
    except:
        Curr_city = "NA"

    try:
        Home_town = Home_towns[0].text
        Home_town = Home_town.split("ometown")[1].replace(',', "-")
    except:
        Home_town = "NA"

    print flag
    try:
        if flag == 1:
            print Name, Gender
            f.write(Name + "," + Birthday + "," + Gender + "," + Home_town + "," + Curr_city + "," + temp + "\n" )
    except:
        print "Problem in writing"

    return flag

def urlMaker(url):

    if 'id' in url:
        url = url.split("&")[0] + "&v=friends"
    else:
        url = url.split("?")[0] + "/friends"

    return url

def base(seed):

    flag = 0

    while flag == 0:
        response = opener.open(seed)
        Page_Html = response.read()
        Parsed_html = Soup(Page_Html, "html.parser")

        Parsed_html = Parsed_html.findAll("div", {"id":"root"})[0]

        Details = Parsed_html.findAll("table", {"role":"presentation"})

        for Detail in Details:
            try:
                Friend = Detail.findAll("a")[0]
                print Friend["href"]
                test = final("https://m.facebook.com" + Friend["href"], Friend.text , f)
            except:
                print "Error in finding friend list"

        try:
            See_more = Parsed_html.findAll("div", {"id":"m_more_friends"})
            See_more = See_more[0]
            Next_page = See_more.findAll("a")[0]
            seed = 'https://m.facebook.com' + Next_page["href"]

        except:
            print "Error in finding more friend list"
            flag = 1

# details from 300 friends friendlist
count = 0
while(count < 300):
    f = open(File_name1, "w")
    test = arr[count]
    test = urlMaker(test)
    base(test)
    f.close()
    f1 = open(File_name1, "r")
    test = f1.read()
    f1.close()
    f = open(File_name, "a")
    f.write(test)
    f.close()
    count += 1
    print count , len(arr), len(arr1)
    time.sleep(1)
