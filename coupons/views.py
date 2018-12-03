from django.http import HttpResponse
from bs4 import BeautifulSoup
import urllib.request
import json


def mac(request):
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
                    fotoKuponu.append(img.get('src'))# pobranie zawartości alt'a

    cenaKuponu.reverse()
    fotoKuponu.reverse()
    for i in nazwaKuponu:
        for j in cenaKuponu:
            for k in fotoKuponu:
                kuponyMacEl = {
                    "name": i,
                    "value": j,
                    "picture": k
                }
        # print(kuponyMacEl)
        cenaKuponu.remove(j)
        fotoKuponu.remove(k)
        kuponyMac.append(kuponyMacEl)

    return HttpResponse(json.dumps(kuponyMac))


def subway(request):
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

    fotoKuponu.reverse()
    for i in nazwaCenaSubway:
        for j in fotoKuponu:
            kuponySubwayEl = {
                "name": i,
                "picture": j
            }
        fotoKuponu.remove(j)
        kuponySubway.append(kuponySubwayEl)

    return HttpResponse(json.dumps(kuponySubway))


def dagrasso(request):
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
    fotoKuponu.reverse()
    for i in nazwaKuponu:
        for j in fotoKuponu:
            kuponyDagrassoEl = {
                'name': i,
                'picture': j
            }
        fotoKuponu.remove(j)
        kuponyDagrasso.append(kuponyDagrassoEl)

    return HttpResponse(json.dumps(kuponyDagrasso))