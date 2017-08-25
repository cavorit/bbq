import re
import urllib.request

Zeilen = ['# Eine Zeile mit einem Kommentar ', '<a href="http://www.taz.de">Beschreibung</a>', '<a href="http://www.tagesschau.de">Die Tagesschau</a>', '<a href="https://cavorit.de">Cavorit</a>'] 

#Webseite = "http://cavorit.de"
#Zeilen = urllib.request.urlopen(Webseite)
 

# print("Name: {0}, Link: {1},.format(m.group(2), m.group(1)))
pattern = r"((?<=<a href=[\"\'])(?P<Link>.+)[\'\"]>(?P<Beschreibung>.+)(?=</a>))"

z = 0
for Zeile in Zeilen:
    m = re.search(pattern, string = Zeile)
    z+=1 
    if m:
        #print("Name")#: {0}, Link: {1}".format(m.group(Name), m.group(Link)))
        print("z%s: %s (%s)" % (z, m.group('Beschreibung'), m.group('Link')))
    else:
        print("z%s: --- no entry found" %z)

