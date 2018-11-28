import bs4 as bs
import urllib.request

url = 'https://www.rmf24.pl/fakty/feed'
sauce = urllib.request.urlopen(url).read()
soup = bs.BeautifulSoup(sauce, 'xml')
tab = []

for url in soup.find_all('item'):
    xd = {
        "title": url.title.text,
        "link": url.link.text,
        "desc": url.description.text,
        "pubDate": url.pubDate.text
    }

    tab.append(xd)

print(tab[0]["title"])
