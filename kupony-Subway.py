from bs4 import BeautifulSoup
import urllib.request
import json

def subway():
    with urllib.request.urlopen('https://www.qpony.pl/subway') as response:
        webpage = response.read()
        soup = BeautifulSoup(webpage, 'html.parser')
        nazwaCenaSubway = []
        fotoKuponu = []
        kuponySubwayEl = {}
        kuponySubway = []
        for x in soup.find_all('div', {'class': 'layout-with-sidebar__content'}):
            for y in x.find_all('div', {'class': 'section__qpons'}):
                for z in y.find_all('div', {'class': 'qpon-horizontal'}):
                    for a in z.find_all('div', {'class': 'qpon-horizontal__name'}):
                        nazwaCenaSubway.append(a.get_text())
                    for b in z.find_all('div', {'class': 'qpon-horizontal__thumb'}):
                        fotoKuponu.append(b.get('data-original'))


    for i in nazwaCenaSubway:
        for j in fotoKuponu:
            kuponySubwayEl = {
                "name": i,
                "picture": j
            }
        kuponySubway.append(kuponySubwayEl)

    with open('kuponySubway.json', 'w') as outfile:
        for i in kuponySubway:
            print(i)
            json.dump(i, outfile)

subway()