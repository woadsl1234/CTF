#coding=utf-8
import requests
import threading
import Queue

url = "http://39.105.115.217:8888/check.php?name=admin&password=admin&submit=提交查询"
threads = 25
q = Queue.Queue()

for i in range(50):
    q.put(i)

def get():
    while not q.empty():
        q.get()
        r = requests.get(url)
        print(r.text)

if __name__ == '__main__':
    for i in range(threads):
        t = threading.Thread(target=get)
        t.start()

    for i in range(threads):
        t.join() 