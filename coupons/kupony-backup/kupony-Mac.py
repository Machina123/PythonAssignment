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

                if len(anchor.find_all('div', {'class': 'price'})) < 1:
                    cenaKuponu.append(' ')
                else:
                    for ceny in anchor.find_all('div', {'class': 'price'}):
                        for u in ceny.find_all('span', {'class': 'pln'}):
                            cenaKuponuTMP = u.get_text()
                        for v in ceny.find_all('span', {'class': 'gr'}):
                            nowaCena = cenaKuponuTMP + "." + v.get_text()
                            cenaKuponu.append(nowaCena)
                for img in anchor.find_all('img'):
                    fotoKuponu.append(img.get('src'))  # pobranie zawartości alt'a

    # cenaKuponu.reverse()
    # fotoKuponu.reverse()
    # for i in nazwaKuponu:
    #     for j in cenaKuponu:
    #         for k in fotoKuponu:
    #             kuponyMacEl = {
    #                 "name": i,
    #                 "value": j,
    #                 "picture": k
    #             }
    #     # print(kuponyMacEl)
    #         fotoKuponu.remove(k)
    #         cenaKuponu.remove(j)

    for i in range(len(nazwaKuponu)):
        kuponyMacEl = {
            "name": nazwaKuponu[i],
            "price": cenaKuponu[i],
            "picture": fotoKuponu[i]
        }
        kuponyMac.append(kuponyMacEl)

    for i in kuponyMac:
        print(i)
    #return HttpResponse(json.dumps(kuponyMac))

mac()