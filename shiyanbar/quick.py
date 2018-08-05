import requests
import base64

url = 'http://ctf5.shiyanbar.com/web/10/10.php'
s = requests.Session()
html = s.get(url)
base = base64.b64decode(html.headers['FLAG'])
data = base[-9:]
html = s.post(url,data=dict(key=data))
print html.text
