import requests
from bs4 import BeautifulSoup

def gethtml(Url):
    url=Url
    r=requests.get(url,timeout=60,headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.3538.400 QQBrowser/9.6.12501.400'})
    html=r.content
    print(r.status_code)
    return html

def parsehtml(Html):
    html=Html
    soup=BeautifulSoup(html,'html.parser')
    imglist=soup.find_all('div',attrs={'class':'list'})
    return imglist

def save(imglist):
    for i in imglist:
        imgweb=i.find_all('img',attrs={'src':True})
        for i in imgweb:
            print('正在下载')
            print(i['data-original'])
            with open('D:\\Text\\{}.jpg'.format(i['alt']),'wb') as f:
                f.write(requests.get(i['data-original']).content)
                
url='http://699pic.com/sousuo-78927-0-complex-all-0-all-all-2-0-0-0-0-0-0-all-all.html'
html=gethtml(url)
imglist=parsehtml(html)
save(imglist)

        
