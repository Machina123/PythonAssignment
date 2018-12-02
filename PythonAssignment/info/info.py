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

def tvn():
    soup = get_soup(urlTvn)
    for url in soup.find_all('item'):
        xd = {
            "title": url.title.text,
            "link": url.link.text,
            "desc": url.description.text,
            "pubDate": url.pubDate.text
        }

        tabTvn.append(xd)
    return HttpResponse(json.dumps(tabTvn))

def rmf():
    soup = get_soup(urlRmf)
    for url in soup.find_all('item'):
        xd = {
            "title": url.title.text,
            "link": url.link.text,
            "desc": url.description.text,
            "pubDate": url.pubDate.text
        }

        tabRmf.append(xd)
    return HttpResponse(json.dumps(tabRmf))

def interia():
    soup = get_soup(urlInteria)
    for url in soup.find_all('item'):
        xd = {
            "title": url.title.text,
            "link": url.link.text,
            "desc": url.description.text,
            "pubDate": url.pubDate.text
        }

        tabInteria.append(xd)
    return HttpResponse(json.dumps(tabInteria))