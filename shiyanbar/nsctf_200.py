import base64
import rot13

ciper = 'a1zLbgQsCESEIqRLwuQAyMwLyq2L5VwBxqGA3RQAyumZ0tmMvSGM2ZwB4tws'
ciper = rot13.de_rot13(ciper)
ciper = base64.b64decode(ciper[::-1])

flag = ''
for i in ciper:
    flag+=chr(ord(i)-1) 

print(flag[::-1])