import math
import urllib.parse
import urllib.request
import json
from bs4 import BeautifulSoup
from nakaya.shopping.key import yahooDict

class Goods:
    def __init__(self):
        self.id_ = ""
        self.title_ = ""
        self.money_ = ""
        self.imageurl_ = ""
        self.condition_ = ""
        self.imagepath_ = ""

    def __init__(self, id="", title="", money=0, imageurl=[], condition=""):
        self.id_ = id
        self.title_ = title
        self.money_ = money
        self.imageurl_ = imageurl
        self.condition_ = condition
        self.imagepath_ = ""

    def __str__(self):
        return self.toString()

    def __repr__(self):
        return self.toString()

    def getID(self):
        return self.id_

    def getTitle(self):
        return self.title_

    def getMoney(self):
        return self.money_

    def getImageURL(self):
        return self.imageurl_

    def getCondition(self):
        return self.condition_

    def getImagePath(self):
        return self.imagepath_

    def setID(self, asin):
        self.id_ = id

    def setTitle(self, title):
        self.title_ = title

    def setMoney(self, content):
        self.money_ = money

    def setImageURL(self, imageurl):
        self.imageurl_ = imageurl

    def setCondition(self, condition):
        self.condition_ = condition

    def setImagePath(self, imagepath):
        self.imagepath_ = imagepath

    id = property(getID, setID)
    title = property(getTitle, setTitle)
    money = property(getMoney, setMoney)
    imageURL = property(getImageURL, setImageURL)
    condition = property(getCondition, setCondition)
    imagePath = property(getImagePath, setImagePath)

    def toString(self):
        text = self.id + "\n"
        text += self.title + "\n"
        text += str(self.money) + "\n"
        text += str(self.imageURL) + "\n"
        text += self.condition + "\n"
        text += self.imagePath
        return text


def yahaucSearchRequest(keyword,pagecount):
    params = urllib.parse.urlencode(
                {'appid': yahooDict["appid"],
                 'query': keyword,
                 'page': pagecount})
    response = urllib.request.urlopen(yahooDict["searchurl"] + params)
    return response.read().decode("utf-8")

def searchPageCount(keyword):
    req = yahaucSearchRequest(keyword, 1)
    soup = BeautifulSoup(req, "lxml")
    count = int(soup.find("resultset")["totalresultsavailable"])

    return math.ceil(count / 20)

def searchAuctionIDList(keyword,pagecount,alist):
    for i in range(pagecount):
        req = yahaucSearchRequest(keyword, i+1)
        soup = BeautifulSoup(req, "lxml")
        ids = soup.find_all("auctionid")
        for item in ids:
            alist.append(item.text)

def getAuctionItemContents(aid):
    params = urllib.parse.urlencode(
                {'appid': yahooDict["appid"],
                 'auctionID': aid})
    response = urllib.request.urlopen(yahooDict["detailurl"] + params)
    return response.read().decode("utf-8")

def searchRequest(keyword,dic={}):
    conditions = {'appid': yahooDict["appid"],
                 'query': keyword}
    conditions.update(dic)
    params = urllib.parse.urlencode(conditions)
    response = urllib.request.urlopen(yahooDict["searchurl"] + params)
    return response.read().decode("utf-8")