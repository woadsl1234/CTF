import requests
import re
from bs4 import BeautifulSoup

url='http://120.24.86.145:8002/qiumingshan/'
se=requests.Session()
ht=se.get(url)
ht.encoding='utf-8'
bs=BeautifulSoup(ht.text,'lxml')
div=bs.find_all('div')
str=r'<div>(.*?)=?;</div>'
gp=re.findall(str,ht.text)
print(ht.text)
daan=gp[0][:-2]
print(daan)
daan=eval(daan)
print(daan)
data={'value':daan}
x=se.post(url,data=data)
x.encoding='utf-8'
print(x.text)
import re
import requests
#
# s = requests.Session()
# r = s.get("http://120.24.86.145:8002/qiumingshan/")
# searchObj = re.search(r'^<div>(.*)=\?;</div>$', r.text, re.M | re.S)
# d = {
#     "value": eval(searchObj.group(1))
# }
# r = s.post("http://120.24.86.145:8002/qiumingshan/", data=d)
# r.encoding='utf-8'
# print(r.text)