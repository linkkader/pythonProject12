# -*- coding: utf-8 -*-
import json
import pprint
from bs4 import BeautifulSoup


def save(name):
    s = "[\n\t"
    f = open(name + ".json", 'w')
    test = open("zmovie/test.txt", encoding="utf8").read()
    ge = test.split(name + "linkkader" + "/*")[1].split(name + "linkkader")[0].split("/*")
    i = 0
    for a in ge:
        i = i + 1
        if not "|" in a:
            continue
        print(a)
        print(a.split("|")[0].replace("*",""))
        print(a.split("|")[1].replace("*",""))
        g = Genre(a.split("|")[0].replace("*",""), a.split("|")[1].replace("*",""))
        s = s + json.dumps(g.__dict__)
        if i < len(ge):
            s = s + ",\n\t"
    s = s + "\n]"
    f.write(s)

st = """<ul class="nav-menu">
                                <li><a href="https://www.streameay.net/seriestream/genres/action.html">Action</a></li>
                                <li><a href="https://www.streameay.net/seriestream/genres/comaedie.html">Comédie</a></li>
                                <li><a href="https://www.streameay.net/seriestream/genres/romance.html">Romance</a></li>
                                <li><a href="https://www.streameay.net/seriestream/genres/thriller.html">Thriller</a></li>
                                <li><a href="https://www.streameay.net/seriestream/genres/aventure.html">Aventure</a></li>
                                <li><a href="https://www.streameay.net/seriestream/genres/famille.html">Famille</a></li>
                                <li><a href="https://www.streameay.net/seriestream/genres/fantastique.html">Fantastique</a></li>
                                <li><a href="https://www.streameay.net/seriestream/genres/epouvante-horreur.html">Epouvante-horreur</a></li>
                                <li><a href="https://www.streameay.net/seriestream/genres/drame.html">Drame</a></li>
                                <li><a href="https://www.streameay.net/seriestream/genres/documentaire.html">Documentaire</a></li>
                                <li><a href="https://www.streameay.net/seriestream/genres/biopic.html">Biopic</a></li>
                                <li><a href="https://www.streameay.net/seriestream/genres/animation.html">Animation</a></li>
                                <li><a href="https://www.streameay.net/seriestream/genres/policier.html">Policier</a></li>
                                <li><a href="https://www.streameay.net/seriestream/genres/divers.html">Divers</a></li>
                                <li><a href="https://www.streameay.net/seriestream/genres/guerre.html">Guerre</a></li>
                            </ul>"""

class Genre:
    def __init__(self, name, url):
        self.name = name
        self.url = url



def decodex(x):
    from itertools import chain
    import base64

    x = x.replace('https://www.youtube.com/embed/', '')

    missing_padding = len(x) % 4
    if missing_padding:
        x += '=' * (4 - missing_padding)
    print(x)
    try:
        e = base64.b64decode(x)
        print(e)
        t = ''
        r = "ETEfazefzeaZa13MnZEe"
        a = 0
        px = chain(e)

        i = 0
        for y in list(px):
            if True:
                t += chr(int(175 ^ y) - ord(r[a]))
                print(a)
            else:
                t += chr(int(175 ^ ord(y[0])) - ord(r[a]))
            a = 0 if a > len(r) - 2 else a + 1
        print(t)
        return t
    except:
        return ''
    print(x)


#print(21^2)
#decodex("AmcWeXsbOzpCdnwQbTEIAXEQ3GcbbttkP196ZW54fHtqzssODXw7Mds=")


elts = BeautifulSoup(st).find_all("li")

s = "[\n\t"
f = open("streameay" + ".json", 'w')
ii = 0
for i2 in elts:
    a = str(i2)
    print(a)
    #if not 'href="' in a:
    #    continue
    g = Genre(i2.get_text(),a.split('href="')[1].split('"')[0].replace(".html", "/page-linkkader.html"))
    #g.url = "https://animeindo.one/daftar-anime/page/linkkader/?genre%5B0%5D=" + g.url
    # print(g.url)
    s = s + json.dumps(g.__dict__)
    if ii < len(elts):
        s = s + ",\n\t"
s = s + "\n]"
f.write(s)