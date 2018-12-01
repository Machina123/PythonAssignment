import bs4 as bs
import urllib.request

urlTvn = 'https://www.tvn24.pl/najnowsze.xml'

def get_soup(url):
    sauce = urllib.request.urlopen(url).read()
    soup = bs.BeautifulSoup(sauce, 'xml')
    return soup

soup = get_soup(urlTvn)
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
