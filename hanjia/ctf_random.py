import requests

re=requests.session()
header={"Connection":"Keep-Alive"}
url='http://123.206.203.108:10001/random.php'
html=re.post(url,headers=header)
html_1=re.post(url,headers=header)
print(html.text)
print(html_1.text)