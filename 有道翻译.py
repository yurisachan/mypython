import urllib.request as u
import urllib.parse
import json
import time

while 1:
    word=input("请输入需要翻译的内容(输入“q!”退出程序)：")
    if word=="q!":
        break
    
    url="http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"

    head={}
    head["User-Agent"]='Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.3538.400 QQBrowser/9.6.12501.400'

    data={'i':word,
    'from':'AUTO',
    'to':'AUTO',
    'smartresult':'dict',
    'client':'fanyideskweb',
    'salt':'1531579942106',
    'sign':'f89e20b54ca3ecfac6ab2d10e9aa8e96',
    'doctype':'json',
    'version':'2.1',
    'keyfrom':'fanyi.web',
    'action':'FY_BY_CLICKBUTTION',
    'typoResult':'false'}
    data=urllib.parse.urlencode(data).encode("utf-8")

    req=urllib.request.Request(url,data,head)
    get=u.urlopen(req)
    html=get.read().decode("utf-8")

    json_get=json.loads(html)

    print("翻译结果：%s"%(json_get["translateResult"][0][0]['tgt']))
    time.sleep(2)

