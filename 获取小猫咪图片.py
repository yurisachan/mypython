#get
import urllib.request as u
url="http://placekitten.com/500/600"

getcat=u.urlopen(url).read()

#save
with open("D:\\getcat.jpg","wb") as f:
    f.write(getcat)
