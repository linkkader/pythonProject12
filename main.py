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

st = """<ul id="main_header" class="main-header">
<li id="menu-item-20" class="genres menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children menu-item-20">
<a href="/film/">FILM</a><ul class="sub-menu">
<li id="menu-item-3482" class="menu-item menu-item-type-taxonomy menu-item-object-genres menu-item-3482"><a href="https://ilgeniodellostreaming.email/genere/animazione/">Animazione</a></li>
<li id="menu-item-3483" class="menu-item menu-item-type-taxonomy menu-item-object-genres menu-item-3483"><a href="https://ilgeniodellostreaming.email/genere/avventura/">Avventura</a></li><li id="menu-item-3484" class="menu-item menu-item-type-taxonomy menu-item-object-genres menu-item-3484"><a href="https://ilgeniodellostreaming.email/genere/azione/">Azione</a></li><li id="menu-item-3485" class="menu-item menu-item-type-taxonomy menu-item-object-genres menu-item-3485"><a href="https://ilgeniodellostreaming.email/genere/commedia/">Commedia</a></li><li id="menu-item-3486" class="menu-item menu-item-type-taxonomy menu-item-object-genres menu-item-3486"><a href="https://ilgeniodellostreaming.email/genere/crime/">Crime</a></li><li id="menu-item-3487" class="menu-item menu-item-type-taxonomy menu-item-object-genres menu-item-3487"><a href="https://ilgeniodellostreaming.email/genere/documentario/">Documentario</a></li><li id="menu-item-3488" class="menu-item menu-item-type-taxonomy menu-item-object-genres menu-item-3488"><a href="https://ilgeniodellostreaming.email/genere/dramma/">Dramma</a></li><li id="menu-item-3489" class="menu-item menu-item-type-taxonomy menu-item-object-genres menu-item-3489"><a href="https://ilgeniodellostreaming.email/genere/famiglia/">Famiglia</a></li><li id="menu-item-3490" class="menu-item menu-item-type-taxonomy menu-item-object-genres menu-item-3490"><a href="https://ilgeniodellostreaming.email/genere/fantascienza/">Fantascienza</a></li><li id="menu-item-3491" class="menu-item menu-item-type-taxonomy menu-item-object-genres menu-item-3491"><a href="https://ilgeniodellostreaming.email/genere/fantasy/">Fantasy</a></li><li id="menu-item-3492" class="menu-item menu-item-type-taxonomy menu-item-object-genres menu-item-3492"><a href="https://ilgeniodellostreaming.email/genere/guerra/">Guerra</a></li><li id="menu-item-3493" class="menu-item menu-item-type-taxonomy menu-item-object-genres menu-item-3493"><a href="https://ilgeniodellostreaming.email/genere/horror/">Horror</a></li><li id="menu-item-3494" class="menu-item menu-item-type-taxonomy menu-item-object-genres menu-item-3494"><a href="https://ilgeniodellostreaming.email/genere/mistero/">Mistero</a></li><li id="menu-item-3495" class="menu-item menu-item-type-taxonomy menu-item-object-genres menu-item-3495"><a href="https://ilgeniodellostreaming.email/genere/musica/">Musica</a></li><li id="menu-item-3496" class="menu-item menu-item-type-taxonomy menu-item-object-genres menu-item-3496"><a href="https://ilgeniodellostreaming.email/genere/romance/">Romance</a></li><li id="menu-item-3497" class="menu-item menu-item-type-taxonomy menu-item-object-genres menu-item-3497"><a href="https://ilgeniodellostreaming.email/genere/sci-fi-fantasy/">Sci-Fi &amp; Fantasy</a></li><li id="menu-item-3498" class="menu-item menu-item-type-taxonomy menu-item-object-genres menu-item-3498"><a href="https://ilgeniodellostreaming.email/genere/storia/">Storia</a></li><li id="menu-item-3500" class="menu-item menu-item-type-taxonomy menu-item-object-genres menu-item-3500"><a href="https://ilgeniodellostreaming.email/genere/thriller/">Thriller</a></li><li id="menu-item-3499" class="menu-item menu-item-type-taxonomy menu-item-object-genres menu-item-3499"><a href="https://ilgeniodellostreaming.email/genere/televisione-film/">televisione film</a></li><li id="menu-item-3501" class="menu-item menu-item-type-taxonomy menu-item-object-genres menu-item-3501"><a href="https://ilgeniodellostreaming.email/genere/western/">Western</a></li></ul></li><li id="menu-item-30" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children menu-item-30"><a href="/serietv/">SERIE TV</a><ul class="sub-menu"><li id="menu-item-26641" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-26641"><a href="/episodi/">Ultimi Episodi</a></li><li id="menu-item-26636" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-26636"><a href="/stagioni/">Ultimi Stagioni</a></li></ul></li><li id="menu-item-29" class="genres menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children menu-item-29"><a href="#">ANNO</a><ul class="sub-menu"><li id="menu-item-3511" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-3511"><a href="/anno/2022/">2022</a></li><li id="menu-item-137333" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-137333"><a href="/anno/2021/">2021</a></li><li id="menu-item-3513" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-3513"><a href="/anno/2020/">2020</a></li><li id="menu-item-3502" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-3502"><a href="/anno/2019/">2019</a></li><li id="menu-item-3503" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-3503"><a href="/anno/2018/">2018</a></li><li id="menu-item-3504" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-3504"><a href="/anno/2017/">2017</a></li><li id="menu-item-3505" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-3505"><a href="/anno/2016/">2016</a></li><li id="menu-item-3506" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-3506"><a href="/anno/2015/">2015</a></li><li id="menu-item-3507" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-3507"><a href="/anno/2014/">2014</a></li><li id="menu-item-3508" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-3508"><a href="/anno/2013/">2013</a></li><li id="menu-item-3509" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-3509"><a href="/anno/2012/">2012</a></li><li id="menu-item-3510" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-3510"><a href="/anno/2011/">2011</a></li></ul></li><li id="menu-item-31" class="menu-item menu-item-type-custom menu-item-object-custom menu-item-31"><a href="/imdb/">IMDb Top 50</a></li></ul>"""

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
f = open("ilgeniodellostreaming" + ".json", 'w')
ii = 0
for i2 in elts:
    a = str(i2)
    print(a)
    #if not 'href="' in a:
    #    continue
    g = Genre(i2.get_text(),a.split('href="')[1].split('"')[0] + "page/linkkader/")
    #g.url = "https://animeindo.one/daftar-anime/page/linkkader/?genre%5B0%5D=" + g.url
    # print(g.url)
    s = s + json.dumps(g.__dict__)
    if ii < len(elts):
        s = s + ",\n\t"
s = s + "\n]"
f.write(s)