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

st = """<ul class="bycategories">
<li><a href="https://www.uwatchfree.fo/category/action/">Action</a></li>
<li><a href="https://www.uwatchfree.fo/category/adult/">Adult</a></li>
<li><a href="https://www.uwatchfree.fo/category/adventure/">Adventure</a></li>
<li><a href="https://www.uwatchfree.fo/category/animation/">Animation</a></li>
<li><a href="https://www.uwatchfree.fo/category/bengali/">Bengali</a></li>
<li><a href="https://www.uwatchfree.fo/category/biography/">Biography</a></li>
<li><a href="https://www.uwatchfree.fo/category/comedy/">Comedy</a></li>
<li><a href="https://www.uwatchfree.fo/category/crime/">Crime</a></li>
<li><a href="https://www.uwatchfree.fo/category/documentaries/">Documentaries</a></li>
<li><a href="https://www.uwatchfree.fo/category/drama/">Drama</a></li>
<li><a href="https://www.uwatchfree.fo/category/dubbed/">Dubbed</a></li>
<li><a href="https://www.uwatchfree.fo/category/family/">Family</a></li>
<li><a href="https://www.uwatchfree.fo/category/fantasy/">Fantasy</a></li>
<li><a href="https://www.uwatchfree.fo/category/featured/">Featured</a></li>
<li><a href="https://www.uwatchfree.fo/category/gujarati/">Gujarati</a></li>
<li><a href="https://www.uwatchfree.fo/category/hd/">HD</a></li>
<li><a href="https://www.uwatchfree.fo/category/hindi/">Hindi</a></li>
<li><a href="https://www.uwatchfree.fo/category/history/">History</a></li>
<li><a href="https://www.uwatchfree.fo/category/hollywood/">Hollywood</a></li>
<li><a href="https://www.uwatchfree.fo/category/horror/">Horror</a></li>
<li><a href="https://www.uwatchfree.fo/category/kannada/">Kannada</a></li>
<li><a href="https://www.uwatchfree.fo/category/malayalam/">Malayalam</a></li>
<li><a href="https://www.uwatchfree.fo/category/marathi/">Marathi</a></li>
<li><a href="https://www.uwatchfree.fo/category/music/">Music</a></li>
<li><a href="https://www.uwatchfree.fo/category/musical/">Musical</a></li>
<li><a href="https://www.uwatchfree.fo/category/mystery/">Mystery</a></li>
<li><a href="https://www.uwatchfree.fo/category/punjabi/">Punjabi</a></li>
<li><a href="https://www.uwatchfree.fo/category/romance/">Romance</a></li>
<li><a href="https://www.uwatchfree.fo/category/sci-fi/">Sci-Fi</a></li>
<li><a href="https://www.uwatchfree.fo/category/short/">Short</a></li>
<li><a href="https://www.uwatchfree.fo/category/sport/">Sport</a></li>
<li><a href="https://www.uwatchfree.fo/category/tamil/">Tamil</a></li>
<li><a href="https://www.uwatchfree.fo/category/telugu/">Telugu</a></li>
<li><a href="https://www.uwatchfree.fo/category/thriller/">Thriller</a></li>
<li><a href="https://www.uwatchfree.fo/category/tv-series/">TV-Series</a></li>
<li><a href="https://www.uwatchfree.fo/category/urdu/">Urdu</a></li>
<li><a href="https://www.uwatchfree.fo/category/war/">War</a></li>
<li><a href="https://www.uwatchfree.fo/category/western/">Western</a></li>
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
f = open("uwatchfree" + ".json", 'w')
ii = 0
for i2 in elts:
    a = str(i2)
    print(a)
    #if not 'href="' in a:
      #  continue
    g = Genre(i2.get_text(),a.split('href="')[1].split('"')[0] + "page/linkkader/")
    #g.url = "https://animeindo.one/daftar-anime/page/linkkader/?genre%5B0%5D=" + g.url
    # print(g.url)
    s = s + json.dumps(g.__dict__)
    if ii < len(elts):
        s = s + ",\n\t"
s = s + "\n]"
f.write(s)