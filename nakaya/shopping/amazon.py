#coding:utf-8
import bottlenose
from bs4 import BeautifulSoup
from nakaya.shopping.key import amazonDict

class Goods:

    def __init__(self):
        self.asin_ = ""
        self.title_ = ""
        self.money_ = ""
        self.imageurl_ = ""
        self.imagepath_ = ""
        self.soldout_ = False
        self.detailpageurl_ = ""

    def __init__(self, asin="", title="", money=0, imageurl=[]):
        self.asin_ = asin
        self.title_ = title
        self.money_ = money
        self.imageurl_ = imageurl
        self.imagepath_ = ""
        self.soldout_ = False
        self.detailpageurl_ = ""

    def __str__(self):
        return self.toString()

    def __repr__(self):
        return self.toString()

    def getAsin(self):
        return self.asin_

    def getTitle(self):
        return self.title_

    def getMoney(self):
        return self.money_

    def getImageURL(self):
        return self.imageurl_

    def getImagePath(self):
        return self.imagepath_

    def getSoldout(self):
        return self.soldout_

    def getDetailPageUrl(self):
        return self.detailpageurl_

    def setAsin(self, asin):
        self.asin_ = asin

    def setTitle(self, title):
        self.title_ = title

    def setMoney(self, content):
        self.money_ = money

    def setImageURL(self, imageurl):
        self.imageurl_ = imageurl

    def setImagePath(self, imagepath):
        self.imagepath_ = imagepath

    def setSoldout(self, soldout):
        self.soldout_ = soldout

    def setDetailPageUrl(self, url):
        self.detailpageurl_ = url

    asin = property(getAsin, setAsin)
    title = property(getTitle, setTitle)
    money = property(getMoney, setMoney)
    imageURL = property(getImageURL, setImageURL)
    imagePath = property(getImagePath, setImagePath)
    soldout = property(getSoldout, setSoldout)
    detailpageurl = property(getDetailPageUrl, setDetailPageUrl)

    def toString(self):
        text = self.asin + "\n"
        text += self.title + "\n"
        text += str(self.money) + "\n"
        text += str(self.imageURL) + "\n"
        text += self.imagePath + "\n"
        text += str(self.soldout) + "\n"
        text += self.detailpageurl
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

def getSearch(keyword, page=1, title=""):
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

