import urllib
import re

url = "http://stoney.sb.org/eno/oblique.html"
page = urllib.request.urlopen(url).read()

pattern = re.compile(r"href=\"?(?P<URL>.+?)\"?>(?P<Description>.+?)<")
match = re.findall(pattern,str(page))
for a_match in match:
    print("URL = %s, Text = %s" %(a_match[0],a_match[1]))
