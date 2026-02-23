# ------------------------------------------------------
# Assignment 2 - Word Frequency + Rolling Hash + Simhash
# ------------------------------------------------------


# required libraries
import requests
import re
from bs4 import BeautifulSoup

# rolling hash (polynomial)
a=53
b=2**64
def rollingHash(w):
    c=0
    for i,j in enumerate(w):
        c+=ord(j)*(a**i)
    return c%b

# simhash function
def simhashing(f):
    v=[0]*64
    for i,j in f.items():
        h=rollingHash(i)
        for k in range(64):
            bt=(h>>k)&1
            if bt==1:
                v[k]+=j
            else:
                v[k]-=j
    f=0
    for l in range(64):
        if v[l]>0:
            f|=(1<<l)
    return f

# frequency of the words
def wordFreq(txt):
    word=re.findall(r'[A-Za-z0-9]+')
    f={}
    for i in word:
        if i in f:
            f[i]+=1
        else:
            f[i]=1
    return f

# fetching the body of webpage
def getBody(weburls):
    r=requests.get(weburls)
    s=BeautifulSoup(r.text,'html.parser')
    if s.body:
        return s.body.get_text(separator='',strip=True)
    return ""

# comparision of the two urls
url1=input("1st url")
url2=input("2nd url")
txt1=getBody(url1)
txt2=getBody(url2)
f1=wordFreq(txt1)
f2=wordFreq(txt2)
s1=simhashing(f1)
s2=simhashing(f2)
x=s1^s2
sameBits=64-bin(x).count('1')
print("Common bits=",sameBits)
