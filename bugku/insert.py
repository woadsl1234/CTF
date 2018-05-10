import requests
import re

url='http://120.24.86.145:8002/web15/'
s=requests.session()
data={'x-forwarded-for':'111.111.111.111'}
html=s.get(url,data=data)
print(html.text)
