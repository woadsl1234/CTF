import requests
import hashlib
import base64

url='http://ef1552d282f14652833420fd14c0de58e5ee47cf407e47d0.game.ichunqiu.com/fl3g_ichuqiu.php'
char='ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz'
se=requests.session()
ht=se.get(url)
temp=123222
print(ht.cookies['user'],ht.text)
def decrypt(txt,key):
    txt=base64.b64encode(txt)
    rnd = txt[0:4]
    txt = txt[4:]
    key=hashlib.md5(rnd.key)
    s=0
    tmp=''
    for i in range(len(txt)):
        if(s == 32):
            s = 0
            tmp += txt[i]^key[++s]
#     for($i=0;$i<strlen($tmp);$i++){
#         $tmp1 .= chr(ord($tmp[$i])-10)
#     return $tmp1


cookie={'user':temp}
