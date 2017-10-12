import urllib
import sys

import urllib.request
from bs4 import BeautifulSoup

images = []
urls = ["https://twitter.com/alltwicecom", "https://twitter.com/DooDoo_22", "https://twitter.com/Chaeng900"]
for theurl in urls:
    thepage = urllib.request.urlopen(theurl)
    soup = BeautifulSoup(thepage, "html.parser")

    print(soup.title.text)
    for link in soup.findAll('img'):
        if str(link.get('src')) not in images:
            print (link.get('src'))
            images.append(str(link.get('src')))
