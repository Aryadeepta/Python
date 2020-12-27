import requests
from bs4 import BeautifulSoup
bs=BeautifulSoup(requests.get("https://www.bbc.com/news/10628494").content, "html.parser")
div=bs.find(id="range-top-stories")
s=str(list(div.children)[5]).split(">")
print(s[3][:-3])
print(s[7][:-3])
print(s[11][:-3])
