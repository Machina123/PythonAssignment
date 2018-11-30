from bs4 import BeautifulSoup
import urllib.request
import json

def dagrasso():
    with urllib.request.urlopen('https://www.dagrasso.pl/promocje') as response:
        webpage = response.read()
        soup = BeautifulSoup(webpage, 'html.parser')
        fotoKuponu = []
        nazwaKuponu = []
        kuponyDagrassoEl = {}
        kuponyDagrasso = []
        for u in soup.find_all('div', {'class': 'content'}):
            for w in u.find_all('div', {'class': 'container'}):
                for x in w.find_all('div', {'class': 'row'}):
                    for y in x.find_all('div', {'class': 'col-sm-5 col-sm-push-7'}):
                        for img in y.find_all('img'):
                            fotoKuponu.append(img.get('src'))
                    for z in x.find_all('div', {'class': 'col-sm-7 col-sm-pull-5'}):
                            for nazwa in z.find_all('h1'):
                                nazwaKuponu.append(nazwa.get_text())

    for i in nazwaKuponu:
        for j in fotoKuponu:
            kuponyDagrassoEl = {
                'name': i,
                'image': j
            }
        kuponyDagrasso.append(kuponyDagrassoEl)

    with open('kuponyDagrasso.json', 'w') as outfile:
        for i in kuponyDagrasso:
            print(i)
            json.dump(i, outfile)

dagrasso()