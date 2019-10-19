import urllib.request as u
get=u.urlopen("http://placekitten.com")
#print(get.read())
#解码
html=get.read().decode("utf-8")
print(html)

