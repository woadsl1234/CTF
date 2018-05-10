import requests

url='http://118.25.18.223:10086/?id=1&&code=sdaf'
re=requests.session()
html=re.get(url)
print(html.text)


