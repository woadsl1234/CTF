#coding:utf-8
import re
import requests
while(1):
    url='http://120.24.86.145:8002/qiumingshan/'
    r=requests.session()
    txt=r.get(url)
    txt.encoding='utf-8'
    txt=txt.text
    ans=re.findall('(.*?)=.*?',txt)
    ans=eval(ans[1][5:])
    payload={'value':ans}
    txt=r.post(url,data=payload)
    txt.encoding='utf-8'
    txt=txt.text
    if 'flag' in txt:
        break

# import hashlib
# for i in range(1000000000):
#     hashl=hashlib.md5()
#     hashl.update(str(i).encode('utf-8'))
#     if hashl.hexdigest()[:6] == '09a522':
#         print(i)
#         break