#!/usr/bin/env python
# https://schedule.readthedocs.io/en/stable/
import time
import requests
from bs4 import BeautifulSoup as BS

#from termux import API as api

# from datetime import datetime, timedelta, time

#path=os.getcwd() + r'/*.MP3'
#def hello_world:
#	print("Hello World")


VOL_URL = r'http://epics.iipfn.tecnico.ulisboa.pt/volume.html'

try:
    page = requests.get(VOL_URL)
    soup = BS(page.content, 'html.parser')

# Catch exceptions  
except (Exception, ConnectionError) as e:
    template = "An exception of type {0} occurred. Arguments:\n{1!r}"
    message = template.format(type(e).__name__, e.args)
    print (message)

# print(soup)
print(soup.title)
# <title>The Dormouse's story</title>

print(soup.title.name)
# u'title'

soup.title.string
# u'The Dormouse's story'
soup.title.parent.name
# u'head'

soup.p
# <p class="title"><b>The Dormouse's story</b></p>

# soup.p['class']
# u'title'
vol = soup.find(id="volume")
print(vol)
print(vol.text)
soup.a


# pps = soup.find_all('a')
#print(pps)
#print(pps[0].text)
