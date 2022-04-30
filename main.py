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

st = """<ul class="flex-row">
<li><a href="/genre/action/">Action</a></li>
<li><a href="/genre/aventure/">Aventure</a></li>
<li><a href="/genre/arts-martiaux/">Arts martiaux</a></li>
<li><a href="/genre/combat/">Combat</a></li>
<li><a href="/genre/comedie/">Comédie</a></li>
<li><a href="/genre/drame/">Drame</a></li>
<li><a href="/genre/epouvante/">Epouvante</a></li>
<li><a href="/genre/fantastique/">Fantastique</a></li>
<li><a href="/genre/fantasy/">Fantasy</a></li>
<li><a href="/genre/mystere/">Mystère</a></li>
<li><a href="/genre/romance/">Romance</a></li>
<li><a href="/genre/shonen/">Shonen</a></li>
<li><a href="/genre/surnaturel/">Surnaturel</a></li>
<li><a href="/genre/sci-fi/">Sci-Fi</a></li>
<li><a href="/genre/school-life/">School life</a></li>
<li><a href="/genre/ninja/">Ninja</a></li>
<li><a href="/genre/seinen/">Seinen</a></li>
<li><a href="/genre/horreur/">Horreur</a></li>
<li><a href="/genre/tranchedevie/">Tranche de vie</a></li>
<li><a href="/genre/psychologique/">Psychologique</a></li>
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


elts = BeautifulSoup(st).find_all("a")

s = "[\n\t"
f = open("frenchanime" + ".json", 'w')
ii = 0
for i2 in elts:
    a = str(i2)
    print(a)
    #if not 'href="' in a:
    #    continue
    g = Genre(i2.get_text(),"https://french-anime.com" + a.split('href="')[1].split('"')[0] + "page/linkkader/")
    #g.url = "https://animeindo.one/daftar-anime/page/linkkader/?genre%5B0%5D=" + g.url
    # print(g.url)
    s = s + json.dumps(g.__dict__)
    if ii < len(elts):
        s = s + ",\n\t"
s = s + "\n]"
f.write(s)