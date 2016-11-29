import requests
from bs4 import BeautifulSoup

url="https://www.flipkart.com/search?q=mobi&otracker=start&as-show=on&as=off"
req=requests.get(url)
req.content

soup=BeautifulSoup(req.content)
for links in soup.find_all("link"):
	print links.get("href")

for links in soup.find_all("meta"):
	print links.get("name")

for links in soup.find_all("meta"):
	print links.get("content")

 	s=soup.find_all("p")
	
for links in s:
	print links.text


