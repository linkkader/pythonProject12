# -*- coding: utf-8 -*-
import json
import pprint
from bs4 import BeautifulSoup

lst = ["uwatchfree","gomovies"]


for i in lst:
    print ("import '../Sources/en/linkkader.dart' as linkkader;".replace('linkkader',i))
print ('\n\n\n')
for i in lst:
    print ('else if(episode.source == "linkkader") return await linkkader.getServers(episode);'.replace('linkkader',i))
print ('\n\n\n')
for i in lst:
    print ('else if(genre.source == "linkkader") return await linkkader.getLibrairies(genre.url,genre.source);'.replace('linkkader',i))
print ('\n\n\n')
for i in lst:
    print ('else if(_animeInfo.source == "linkkader") return await linkkader.getAnimeInfo(_animeInfo);'.replace('linkkader',i))
print ('\n\n\n')