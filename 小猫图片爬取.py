import requests
from bs4 import BeautifulSoup
import os

def gethtml(Url):
    url=Url
    r=requests.get(url,headers={"user-agent":"Mozilla/5.0"})
    html=r.content
    print(r.status_code)
    return html

def parsehtml(Html):
    html=Html
    soup=BeautifulSoup(html,"html.parser")
    cat=soup.find_all('img',attrs={})
    return cat

os.mkdir("D:\\Text")

def saveimg(cat):
    for i in cat:
        caturl="http://placekitten.com/{}".format(i['src'])
        print('正在下载')
        print(caturl)
        with open("D:\\Text\\{}.jpg".format(i['id']),'wb') as f:
            f.write(requests.get(caturl).content)

html=gethtml("http://placekitten.com")
cat=parsehtml(html)
saveimg(cat)
    
