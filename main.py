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

st = """<select id="mangas-category" title="category" name="category" class="input-jr">
<option value="null"> Catégorie </option>
<option value="4-koma"> 4-koma </option>
<option value="action" selected=""> Action </option>
<option value="adulte"> Adulte </option>
<option value="amitie"> Amitié </option>
<option value="amour"> Amour </option>
<option value="arts-martiaux"> Arts martiaux </option>
<option value="aventure"> Aventure </option>
<option value="combat"> Combat </option>
<option value="comedie"> Comédie </option>
<option value="drame"> Drame </option>
<option value="ecchi"> Ecchi </option>
<option value="fantastique"> Fantastique </option>
<option value="gender-bender"> Gender Bender </option>
<option value="guerre"> Guerre </option>
<option value="harem"> Harem </option>
<option value="hentai"> Hentai </option>
<option value="historique"> Historique </option>
<option value="horreur"> Horreur </option>
<option value="josei"> Josei </option>
<option value="mature"> Mature </option>
<option value="mecha"> Mecha </option>
<option value="mystere"> Mystère </option>
<option value="one-shot"> One Shot </option>
<option value="parodie"> Parodie </option>
<option value="policier"> Policier </option>
<option value="psychologique"> Psychologique </option>
<option value="romance"> Romance </option>
<option value="science-fiction"> Science-fiction </option>
<option value="seinen"> Seinen </option>
<option value="shojo"> Shôjo </option>
<option value="shojo-ai"> Shôjo Ai </option>
<option value="shonen"> Shônen </option>
<option value="shonen-ai"> Shônen Ai </option>
<option value="smut"> Smut </option>
<option value="sports"> Sports </option>
<option value="surnaturel"> Surnaturel </option>
<option value="tragedie"> Tragédie </option>
<option value="tranches-de-vie"> Tranches de vie </option>
<option value="vie-scolaire"> Vie scolaire </option>
<option value="webtoons"> Webtoons </option>
<option value="yaoi"> Yaoi </option>
<option value="yuri"> Yuri </option>
</select>"""

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


elts = BeautifulSoup(st).find_all("option")

s = "[\n\t"
f = open("bentomanga" + ".json", 'w')
ii = 0
for i2 in elts:
    a = str(i2)
    print(a)
    #if not 'href="' in a:
      #  continue
    g = Genre(i2.get_text(),"https://bentomanga.com/manga_list?category=" + a.split('value="')[1].split('"')[0] + "&limit=linkkader")
    #g.url = "https://animeindo.one/daftar-anime/page/linkkader/?genre%5B0%5D=" + g.url
    # print(g.url)
    s = s + json.dumps(g.__dict__)
    if ii < len(elts):
        s = s + ",\n\t"
s = s + "\n]"
f.write(s)