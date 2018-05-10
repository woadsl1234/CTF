import requests
import base64
import re

url='http://120.24.86.145:8002/web6/'
se=requests.session()
ht=se.get(url)
flag=ht.headers['flag']
flag=str(base64.b64decode(flag))
# flag.encode('utf-8')
# print(flag)
reg='(.*)(:)(.*)'
group=re.match(reg,flag)
data={'margin':base64.b64decode(group.group(3)[:-1]).decode('utf-8')}
r=se.post(url,data=data)
print(r.text)
