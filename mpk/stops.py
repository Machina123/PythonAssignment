MPK_ENDPOINT_DEPARTS = "http://www.ttss.krakow.pl/internetservice/services/passageInfo/stopPassages/stop"

# ID -> stop name bindings
# credit: https://github.com/jacekkow/mpk-ttss/blob/master/stops/stops.php
MPK_TRAMSTOPS = {
    113: 'AWF',
    462: 'Agencja Kraków Wschód',
    449: 'Bardosa',
    78: 'Batorego',
    130: 'Białucha',
    867: 'Bieńczycka',
    630: 'Bieżanowska',
    84: 'Biprostal',
    461: 'Blokowa',
    747: 'Borek Fałęcki',
    824: 'Borek Fałęcki I',
    612: 'Borsucza',
    451: 'Brama nr 4',
    453: 'Brama nr 5',
    61: 'Bratysławska',
    89: 'Bronowice',
    135: 'Bronowice Małe',
    136: 'Bronowice Wiadukt',
    613: 'Brożka',
    409: 'Centralna',
    3039: 'Centrum Kongresowe ICE',
    2691: 'Chmieleniec',
    87: 'Cichy Kącik',
    3037: 'Cienista',
    621: 'Cmentarz Podgórski',
    124: 'Cmentarz Rakowicki',
    129: 'Cystersów',
    3038: 'Czerwone Maki P+R',
    407: 'Czyżyny',
    392: 'DH Wanda',
    915: 'Dajwór',  # nieczynny - linia muzealna
    435: 'Darwina',
    632: 'Dauna',
    388: 'Dunikowskiego',
    623: 'Dworcowa',
    1173: 'Dworzec Główny Tunel',
    2608: 'Dworzec Główny Zachód',
    2870: 'Dworzec Płaszów Estakada',
    70: 'Dworzec Towarowy',
    370: 'Dąbie',
    464: 'Elektromontaż',
    368: 'Fabryczna',
    322: 'Filharmonia',
    1051: 'Fort Mogiła',
    367: 'Francesco Nullo',
    560: 'Gromadzka',
    2687: 'Grota-Roweckiego',
    1049: 'Głowackiego',
    363: 'Hala Targowa',
    2685: 'Jarzębiny',
    452: 'Jeżynowa',
    319: 'Jubilat',
    624: 'Kabel',
    2690: 'Kampus UJ',
    576: 'Kapelanka',
    429: 'Klasztorna',
    382: 'Kleeberga',
    946: 'Klimeckiego',
    584: 'Kobierzyńska',
    457: 'Koksochemia',
    459: 'Kombinat',
    313: 'Komorowskiego',
    450: 'Kopiec Wandy',
    571: 'Korona',
    63: 'Krowodrza Górka',
    567: 'Kuklińskiego',
    3176: 'Kurdwanów P+R',
    569: 'Limanowskiego',
    2686: 'Lipińskiego',
    561: 'Lipska',
    126: 'Lubicz',
    930: 'M1 Al. Pokoju',
    1263: 'Mały Płaszów',
    454: 'Meksyk',
    362: 'Miodowa',
    375: 'Mistrzejowice',
    2538: 'Miśnieńska',
    460: 'Mrozowa',
    2726: 'Muzeum Inżynierii Miejskiej',  # nieczynny - linia muzealna
    2811: 'Muzeum Lotnictwa',
    3141: 'Muzeum Narodowe',
    2688: 'Norymberska',
    715: 'Nowosądecka',
    3175: 'Nowy Bieżanów P+R',
    71: 'Nowy Kleparz',
    2582: 'Nowy Prokocim',
    369: 'Ofiar Dąbia',
    823: 'Oleandry',
    361: 'Orzeszkowej',
    413: 'Os.Kolorowe',
    424: 'Os.Na Skarpie',
    378: 'Os.Piastów',
    418: 'Os.Zgody',
    377: 'Os.Złotego Wieku',
    466: 'PH',
    614: 'PT',
    960: 'Park Jordana',
    716: 'Piaski Nowe',
    379: 'Piasta Kołodzieja',
    570: 'Plac Bohaterów Getta',
    2744: 'Plac Centralny im. R.Reagana',
    79: 'Plac Inwalidów',
    360: 'Plac Wolnica',
    1360: 'Plac Wszystkich Świętych',
    3033: 'Plaza',
    458: 'Pleszów',
    357: 'Poczta Główna',
    3158: 'Podgórze SKA',
    73: 'Politechnika',
    637: 'Prokocim',
    682: 'Prokocim Szpital',
    72: 'Pędzichów',
    128: 'Rakowicka',
    320: 'Reymana',
    3041: 'Rondo 308. Dywizjonu',
    408: 'Rondo Czyżyńskie',
    365: 'Rondo Grzegórzeckie',
    2539: 'Rondo Hipokratesa',
    2745: 'Rondo Kocmyrzowskie im. Ks. Gorzelanego',
    610: 'Rondo Matecznego',
    125: 'Rondo Mogilskie',
    383: 'Rondo Piastowskie',
    589: 'Ruczaj',
    1262: 'Rzebika',
    611: 'Rzemieślnicza',
    311: 'Salwator',
    615: 'Sanktuarium Bożego Miłosierdzia',
    572: 'Smolki',
    746: 'Solvay',
    358: 'Starowiślna',
    3032: 'Stary Kleparz',
    112: 'Stella-Sawickiego',
    359: 'Stradom',
    423: 'Struga',
    2548: 'Suche Stawy',
    3036: 'Szpital Narutowicza',
    575: 'Szwedzka',
    577: 'Słomiana',
    2871: 'TAURON Arena Kraków Al. Pokoju',
    3040: 'TAURON Arena Kraków Wieczysta',
    77: 'Teatr Bagatela',
    420: 'Teatr Ludowy',
    3242: 'Teatr Słowackiego',
    2859: 'Teatr Variété',
    681: 'Teligi',
    127: 'Uniwersytet Ekonomiczny',
    321: 'Uniwersytet Jagielloński',
    88: 'Uniwersytet Pedagogiczny',
    83: 'Urzędnicza',
    463: 'Walcownia',
    325: 'Wawel',
    2543: 'Wańkowicza',
    133: 'Wesele',
    434: 'Wiadukty',
    718: 'Witosa',
    634: 'Wlotowa',
    442: 'Wzgórza Krzesławickie',
    1154: 'Zabłocie',
    465: 'Zajezdnia Nowa Huta',
    679: 'Ćwiklińskiej',
    922: 'Łagiewniki',
    2821: 'Łagiewniki ZUS',
    2741: 'Św.Gertrudy',
    2742: 'Św.Wawrzyńca',
}