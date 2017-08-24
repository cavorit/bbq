import urllib
from bs4 import BeautifulSoup

url = "http://stoney.sb.org/eno/oblique.html"

page = urllib.request.urlopen(url).read()

soup = BeautifulSoup(page,"html.parser")

[s.extract() for s in soup(['style','script','[document]','head','title'])]

print(soup.get_text)