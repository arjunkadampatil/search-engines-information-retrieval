# -------------------------------
# Assignment 1 - Web Page Fetcher
# -------------------------------


import requests
from bs4 import BeautifulSoup
import sys

# check command line input
if len(sys.argv)<2:
    print("give web url in command line")
    exit()
url=sys.argv[1]
try:
    response=requests.get(url)
except:
    print("error fetching page")
    exit()
html=response.text
soup=BeautifulSoup(html,'html.parser')

# title
if soup.title:
    print("TITLE:")
    print(soup.title.get_text().strip())

# body
print("\nBODY:")
if soup.body:
    print(soup.body.get_text(separator=' ',strip=True))

# links
print("\nLINKS:")
for a in soup.find_all('a'):
    link=a.get('href')
    if link:
        print(link)
