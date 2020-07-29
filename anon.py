
from bs4 import BeautifulSoup
import requests

start = "http://paste.ubuntu.com/p/HnGHwGk4rQ/"

r = requests.get(start)

def getPastebin(url):

    r = requests.get(url)

    if (r.status_code == 200):
        print("URL existe: " + url)
        urls = extractPastebin(r.text)
        print(urls)
        for newUrl in urls:
            getPastebin(newUrl)
    

def extractPastebin(html):
    soup = BeautifulSoup(html, features="html.parser")
    info = soup.findAll("div",{"class":"paste"})[2]
    urls = info.pre.text.split("\n")
    return urls


getPastebin(start)

