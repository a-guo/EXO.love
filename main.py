import urllib, urllib2
import re

urls = ["http://all-twice.com", "http://teamtwice.com/", "http://twicestudio1020.com/xe/data"]
regex = '<img src=(.+?)>'
pattern = re.compile(regex)

for url in urls:
    req = urllib2.Request(url, headers={'User-Agent' : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.30 (KHTML, like Gecko) Ubuntu/11.04 Chromium/12.0.742.112 Chrome/12.0.742.112 Safari/534.30"})
    con = urllib2.urlopen(req)
    htmltext = con.read()
    titles = re.findall(pattern,htmltext)
    print titles
    
    
    print
