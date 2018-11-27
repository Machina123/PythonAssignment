from bs4 import BeautifulSoup
import urllib.request

def mac():
    with urllib.request.urlopen('https://mcdonalds.pl/oferty/?utm_source=mcdonalds.pl&utm_medium=slider&utm_campaign=kupony') as response:
        webpage = response.read()
        soup = BeautifulSoup(webpage, 'html.parser')
        kuponyMac = {}
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
                    fotoKuponu.append(img)

        for i in fotoKuponu:
            print(i)
    cenaKuponu.reverse()
    x = len(cenaKuponu)
    for i in nazwaKuponu:
        for j in cenaKuponu:
            kuponyMac[i] = j
        cenaKuponu.remove(j)
    for i in nazwaKuponu:
         print(i, kuponyMac[i])


def kfc():
    with urllib.request.urlopen('https://kfc.pl/main/home/coupons') as response:
        webpage = response.read()
        soup = BeautifulSoup(webpage, 'html.parser')
        kuponyKFC = {}
        nazwaKuponu = []
        cenaKuponu = []
        fotoKuponu = []

        for anchor in soup.find_all('div', {'class': 'inner-container-bricks'}):
            for x in anchor.find_all('div', {'class': 'coupon-container'}):
                for y in x.find_all('div'):
                    print(y)
                        # nazwaKuponu.append(z.get_text())
    #for i in nazwaKuponu:
     #   print(i)
#print("\t\tMAC\n")
#mac()

print("\n\t\tKFC\n")
kfc()
