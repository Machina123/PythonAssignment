from bs4 import BeautifulSoup
import urllib.request
import json


def mac():
    with urllib.request.urlopen('https://mcdonalds.pl/oferty') as response:
        webpage = response.read()
        soup = BeautifulSoup(webpage, 'html.parser')
        kuponyMac = []
        kuponyMacEl = {}
        nazwaKuponu = []
        cenaKuponu = []
        fotoKuponu = []
        for anchor in soup.find_all('div', {'class': 'coupon'}):
            for x in anchor.find_all('a', {'class': 'download-coupon'}):
                for y in x.find_all('h2'):
                    nazwaKuponu.append(y.get_text())

                for ceny in anchor.find_all('div', {'class': 'price'}):
                    for u in ceny.find_all('span', {'class': 'pln'}):
                        cenaKuponuTMP = u.get_text()
                    for v in ceny.find_all('span', {'class': 'gr'}):
                        nowaCena = cenaKuponuTMP+"."+v.get_text()
                        cenaKuponu.append(nowaCena)
                for img in anchor.find_all('img'):
                    # fotoKuponu.append(img)
                    fotoKuponu.append(img.get('src'))# pobranie zawartości alt'a

    for i in nazwaKuponu:
        for j in cenaKuponu:
            for k in fotoKuponu:
                kuponyMacEl = {
                    "name": i,
                    "value": j,
                    "picture": k
                }
        kuponyMac.append(kuponyMacEl)

    with open('kuponyMcDonald.json', 'w') as outfile:
        for i in kuponyMac:
            print(i)
            json.dump(i, outfile)


    # cenaKuponu.reverse()
    # x = len(cenaKuponu)
    # for i in nazwaKuponu:
        # for j in cenaKuponu:
            # kuponyMac[i] = j
        # cenaKuponu.remove(j)
    # for i in nazwaKuponu:
         # print(i, kuponyMac[i])

mac()