import urllib.request as u
import random

#url="https://www.bilibili.com"
iplist=['49.83.162.13:808','180.121.133.221:808','219.246.34.59:8118','115.225.55.144：8118']

#设置代理ip地址
proxy_support=u.ProxyHandler({'http':random.choice(iplist)})
opener=u.build_opener(proxy_support)
opener.addheaders=[("User-Agent","Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.3538.400 QQBrowser/9.6.12501.400")]

u.install_opener(opener)
get=u.urlopen(url)
html=get.read().decode("utf-8")

print(html)
