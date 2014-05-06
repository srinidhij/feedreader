import requests
from pymongo import MongoClient
import simplejson as json
from xml.etree import ElementTree

def getFeedLinks():
    
    client = MongoClient('mongodb://localhost:27017/')
    db = client.feedreader
    collection = db.feedlinks
    flc = collection.find({})
    feedlinks = []
    
    for flob in flc:
        link = {}
        '''
        link['link'] = flob['link'].encode('ascii','ignore')
        link['title'] = flob['title']
        feedlinks.append(link)
        '''
        print flob
    return feedlinks



def addFeedLink(link,title=None):

    error = None    
    if title is None:
        title = ''

    client = MongoClient('mongodb://localhost:27017/')
    db = client.feedreader
    collection = db.feedlinks
    
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

def getFeeds():
    #tree = ElementTree.parse('country_data.xml')
    #root = ElementTree.fromstring(country_data_as_string)
    pass

def test():
    feed = 'http://feeds.arstechnica.com/arstechnica/business?format=xml'
    title = 'Ars Technica Tech Labs'
    
    msg = addFeedLink(feed, title)

    if msg is None:
        print 'Error adding feed'
    else:
        print 'Error: ',msg

    feed_links = getFeedLinks()
    print feed_links    

if __name__ == '__main__':
    test()