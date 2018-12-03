import webbrowser

def szukajka(klucz):
    webbrowser.open("http://www.google.pl/search?q="+klucz)
    open("link.html", "w").write('<a href="http://www.google.pl/"+klucz+"> Link </a>')

print("Podaj szukaną frazę:\t")
klucz = input()
szukajka(klucz)