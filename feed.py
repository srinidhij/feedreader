import requests
from pymongo import MongoClient
import simplejson as json
from xml.etree import ElementTree
from bs4 import BeautifuSoup

class FeedManager:
    
    def __init__(self):
        client = MongoClient('mongodb://localhost:27017/')
        db = client.feedreader
        self.collection = db.feedlinks


    def getFeedLinks(self,):
        flc = self.collection.find({})
        feedlinks = []
        
        for flob in flc:
            link = {}
            link['link'] = flob['link']
            link['title'] = flob['title']
            feedlinks.append(link)


        return feedlinks

    def addFeedLink(self,link,title=None):

        error = None    
        if title is None:
            title = ''

        collection = self.collection

        flc = collection.find_one({'link':link})
            
        if flc:
            error = 'Feed already added'
            return error

        fl = {
            'link':link, 
            'title':title
            }

        feed_id = collection.insert(fl)

        if feed_id is None:
            error = 'Failed inserting into DB'

        return error

    def fetchparseFeed(self, url):
        res = requests.get(url)
        fxml = res.text

        #Use BeautifuSoup to parse XML


        #Returned feed data is of format {link,title,description,data}



    def getFeeds(self):

        feedData = []
        for feed in self.getFeedLinks():
            feedData.append(self.fetchparseFeed(feed['link']))

        return feedData
        #tree = ElementTree.parse('country_data.xml')
        #root = ElementTree.fromstring(country_data_as_string)
        pass

def test():
    feed = 'http://feeds.arstechnica.com/arstechnica/business?format=xml'
    title = 'Ars Technica Tech Labs'
    fmg = FeedManager()
    msg = fmg.addFeedLink(feed, title)

    if msg is None:
        print 'Feed added Successfully'
    else:
        print 'Error: ',msg

    feed_links = fmg.getFeedLinks()
    print feed_links

if __name__ == '__main__':
    test()