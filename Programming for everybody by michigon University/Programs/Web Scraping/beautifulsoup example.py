import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

url = input('https://en.wikipedia.org/wiki/Pir_Piai')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html,'html.parser')

tags = soup('a')
for tags in tag:
    print(tag.get('href',None))
