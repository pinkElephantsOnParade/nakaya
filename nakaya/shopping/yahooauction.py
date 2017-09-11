import math
import urllib.parse
import urllib.request
import json
from bs4 import BeautifulSoup
from nakaya.shopping.key import yahooDict

class Goods:
    def __init__(self):
        self.id = ""
        self.title = ""
        self.money = ""
        self.imageurl = ""
        self.condition = ""
        self.imagepath = ""

    def __init__(self, id="", title="", money=0, imageurl=[], condition=""):
        self.id = id
        self.title = title
        self.money = money
        self.imageurl = imageurl
        self.condition = condition

    def getID(self):
        return self.id

    def getTitle(self):
        return self.title

    def getMoney(self):
        return self.money

    def getImageURL(self):
        return self.imageurl

    def getCondition(self):
        return self.condition

    def getImagePath(self):
        return self.imagepath

    def setID(self, asin):
        self.id = id

    def setTitle(self, title):
        self.title = title

    def setMoney(self, content):
        self.money = money

    def setImageURL(self, imageurl):
        self.imageurl = imageurl

    def setCondition(self, condition):
        self.condition = condition

    def setImagePath(self, imagepath):
        self.imagepath = imagepath

    def toString(self):
        text = self.id + "\n"
        text += self.title + "\n"
        text += self.money + "\n"
        text += str(self.image) + "\n"
        text += self.condition + "\n"
        text += self.imagepath
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

