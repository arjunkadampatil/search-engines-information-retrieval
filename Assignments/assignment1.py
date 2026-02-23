# ------------------------------- #
# Assignment 1 - Web Page Fetcher #
# ------------------------------- #


# required libraries
import requests
from bs4 import BeautifulSoup
import sys

# check the input of command line
if len(sys.argv)<2:
    print("give your web url in the command line")
    exit()
weburl=sys.argv[1]
try:
    r=requests.get(weburl)
except:
    print("error in fetching the page")
    exit()
htmls=r.text
s=BeautifulSoup(htmls,'html.parser')

# title
if s.title:
    print("TITLE:")
    print(s.title.get_text().strip())

# body
print("\nBODY:")
if s.body:
    print(s.body.get_text(separator='',strip=True))

# links
print("\nLINKS:")
for i in s.find_all('i'):
    links=i.get('href')
    if links:
        print(links)
