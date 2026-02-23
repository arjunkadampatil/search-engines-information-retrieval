# ------------------------------------------------------
# Assignment 2 - Word Frequency + Rolling Hash + Simhash
# ------------------------------------------------------


import requests
import re
from bs4 import BeautifulSoup

# fetch webpage body
def get_body(url):
    r=requests.get(url)
    soup=BeautifulSoup(r.text,'html.parser')
    if soup.body:
        return soup.body.get_text(separator=' ',strip=True)
    return ""

# word frequency
def word_freq(text):
    words=re.findall(r'[A-Za-z0-9]+',text.lower())
    freq={}
    for w in words:
        if w in freq:
            freq[w]+=1
        else:
            freq[w]=1
    return freq

# polynomial rolling hash
P=53
M=2**64
def rolling_hash(word):
    h=0
    for i,ch in enumerate(word):
        h+=ord(ch)*(P**i)
    return h%M

# simhash
def simhash(freq):
    vec=[0]*64
    for word,count in freq.items():
        h=rolling_hash(word)
        for i in range(64):
            bit=(h>>i)&1
            if bit==1:
                vec[i]+=count
            else:
                vec[i]-=count
    final=0
    for i in range(64):
        if vec[i]>0:
            final|=(1<<i)
    return final

# compare two urls
url1=input("1st URL: ")
url2=input("2nd URL: ")
text1=get_body(url1)
text2=get_body(url2)
freq1=word_freq(text1)
freq2=word_freq(text2)
s1=simhash(freq1)
s2=simhash(freq2)
xor=s1^s2
same_bits=64-bin(xor).count('1')
print("Common bits = ",same_bits)
