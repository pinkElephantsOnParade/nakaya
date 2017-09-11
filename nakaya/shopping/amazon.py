#coding:utf-8
import bottlenose
from bs4 import BeautifulSoup
from nakaya.shopping.key import amazonDict

class Goods:

    def __init__(self):
        self.asin = ""
        self.title = ""
        self.money = ""
        self.imageurl = ""
        self.imagepath = ""
        self.soldout = False

    def __init__(self, asin="", title="", money=0, imageurl=[]):
        self.asin = asin
        self.title = title
        self.money = money
        self.imageurl = imageurl

    def getAsin(self):
        return self.asin

    def getTitle(self):
        return self.title

    def getMoney(self):
        return self.money

    def getImageURL(self):
        return self.imageurl

    def getImagePath(self):
        return self.imagepath

    def getSoldout(self):
        return self.soldout

    def setAsin(self, asin):
        self.asin = asin

    def setTitle(self, title):
        self.title = title

    def setMoney(self, content):
        self.money = money

    def setImageURL(self, imageurl):
        self.imageurl = imageurl

    def setImagePath(self, imagepath):
        self.imagepath = imagepath

    def setSoldout(self, soldout):
        self.soldout = soldout

    def toString(self):
        text = self.asin + "\n"
        text += self.title + "\n"
        text += self.money + "\n"
        text += str(self.image) + "\n"
        text += self.imagepath
        return text

def getSearchPageCount(keyword):
    amazon = bottlenose.Amazon(
        amazonDict["AWSAccessKeyId"],
        amazonDict["AWSSecretKey"],
        amazonDict["AsociateID"],
        Region='JP')
    product = amazon.ItemSearch(Keywords=keyword, SearchIndex="All", ResponseGroup="Large")
    soup = BeautifulSoup(product, "lxml")
    return int(soup.find("items").find("totalpages").text)

def getSearch(keyword, page, title=""):
    amazon = bottlenose.Amazon(
        amazonDict["AWSAccessKeyId"],
        amazonDict["AWSSecretKey"],
        amazonDict["AsociateID"],
        Region='JP')
    product = amazon.ItemSearch(Keywords=keyword, SearchIndex="All", ResponseGroup="Large", ItemPage=page)
    return product

def getlookupWithAsin(asin):
    amazon = bottlenose.Amazon(
        amazonDict["AWSAccessKeyId"],
        amazonDict["AWSSecretKey"],
        amazonDict["AsociateID"],
        Region='JP')
    product = amazon.ItemLookup(ItemId=asin, ResponseGroup="Large")
    return product

def getSearchWithAsin(asin):
    amazon = bottlenose.Amazon(
        amazonDict["AWSAccessKeyId"],
        amazonDict["AWSSecretKey"],
        amazonDict["AsociateID"],
        Region='JP')
    product = amazon.ItemSearch(Keywords=asin, SearchIndex="All", ResponseGroup="Large")
    return product

