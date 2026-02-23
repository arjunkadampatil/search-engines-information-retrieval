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
url=sys.argv[1]
try:
    response=requests.get(url)
except:
    print("error in fetching the page")
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
    print(soup.body.get_text(separator='',strip=True))

# links
print("\nLINKS:")
for a in soup.find_all('a'):
    link=a.get('href')
    if link:
        print(link)
