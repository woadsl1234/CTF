import requests

url='http://www.wechall.net/challenge/training/programming1/index.php?action=request'
se=requests.session()
head={
'Cookie':'WC=10328286-40028-tu6FxK2pkLIiGJUy',
'Host':'www.wechall.net',
'Referer':'http://www.wechall.net/challenge/training/programming1/index.php'
}
ht=se.get(url,headers=head)
# print(ht.text)
url1='http://www.wechall.net/challenge/training/programming1/index.php?answer='+ht.text
ht1=se.get(url1,headers=head)
print(ht1.text)