import bs4 as bs
import urllib.request
import json
from django.http import HttpResponse, HttpResponseRedirect

urlTvn = 'https://www.tvn24.pl/najnowsze.xml'
urlRmf = 'https://www.rmf24.pl/fakty/feed'
urlInteria = 'https://fakty.interia.pl/feed'

tabTvn = []
tabRmf = []
tabInteria = []

def get_soup(url):
    sauce = urllib.request.urlopen(url).read()
    soup = bs.BeautifulSoup(sauce, 'xml')
    return soup

def tvn(soup):
    for url in soup.find_all('item'):
        xd = {
            "title": url.title.text,
            "link": url.link.text,
            "desc": url.description.text,
            "pubDate": url.pubDate.text
        }

        tabTvn.append(xd)

def rmf(soup):
    for url in soup.find_all('item'):
        xd = {
            "title": url.title.text,
            "link": url.link.text,
            "desc": url.description.text,
            "pubDate": url.pubDate.text
        }

        tabRmf.append(xd)

def interia(soup):
    for url in soup.find_all('item'):
        xd = {
            "title": url.title.text,
            "link": url.link.text,
            "desc": url.description.text,
            "pubDate": url.pubDate.text
        }

        tabInteria.append(xd)

soupTvn = get_soup(urlTvn)
soupRmf = get_soup(urlRmf)
soupInteria = get_soup(urlInteria)

tvn(soupTvn)
rmf(soupRmf)
interia(soupInteria)

def getTvn():
    return HttpResponse(json.dumps(tabTvn))

def getRmf():
    return HttpResponse(json.dumps(tabRmf))

def getinteria():
    return HttpResponse(json.dumps(tabIntgeria))

