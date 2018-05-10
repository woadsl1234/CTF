import requests
import json
import base64
from PIL import Image
import pytesseract
import subprocess
import cv2

# r = requests.Session()
# while(1):

#
# png=base64.b64decode(base.encode('utf-8'))
# with open("ca.png",'wb') as fp:
#     fp.write(png)

# infile = 'ca.png'
# outfile = 'ca1.png'
# im = Image.open(infile)
# (x, y) = im.size  # read image size
# x_s = x*200  # define standard width
# y_s = y*200  # calc height based on standard width
# out = im.resize((x_s, y_s), Image.ANTIALIAS)  # resize image with high-quality
# out.save(outfile)

url = 'https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic'

data = {}
data['access_token']='24.c945a598696ffc2ef42274149ad47531.2592000.1522333225.282335-10861491'


#读取图片
file=open('C:\\Users\\assu\\Downloads\\A16\\shuju\\data-5\\train\\0012\\1.jpg','rb')
image= file.read()
file.close()

data['image'] = base64.b64encode(image)
headers={
    "Content-Type":"application/x-www-form-urlencoded",
    "apikey":"zR1P2RxG06YoGheGIL1hGCkk"
}

res = requests.post(url=url,headers=headers,data=data)
result = res.json()
print(result)
for line in result["words_result"]:
    x=line["words"]

print(x)

    # url_1=url1+"&submit={}".format(x)
    # requ=r.get(url_1)
    # print(url_1)
    # print(requ.text)

# addr='C:\\Users\\assu\\Downloads\\A16\\shuju\\data-5\\train\\0002\\8.jpg'
# im=cv2.imread(addr,cv2.THRESH_BINARY)
# for i in range(len(im)):
#     for j in range(len(im[i])):
#         print('%4d'%im[i][j],end=' ')
#     print()
# f=open('响.txt','w')
# for i in range(len(im)):
#     for j in range(len(im[i])):
#         print('%4d'%im[i][j],end=' ')
#     print()
