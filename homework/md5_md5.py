# import hashlib
#
# list_char="abcdefghijklmopqrstuvwxyz1234567890"
# md5="0e12112312312222222222"
#
# for a in range(32):
#     for b in range(32):
#         for c in range(32):
#             for j in list_char:
#                 md5[i]=list_char
#                 print(md5)
#
# x=hashlib.md5()
# x.update('1'.encode('utf-8'))
# print(x.hexdigest(),len(md5),len(x.hexdigest()))

# import hashlib
# x='a'
# y=hashlib.md5(x.encode(encoding='utf-8'))
# while y.hexdigest()!=x:
#     x=y.hexdigest()
#     y=hashlib.md5(x.encode(encoding='utf-8'))
#     print(y.hexdigest())
# print(y.hexdigest())

str='d4e8e1f4a0f7e1f3a0e6e1f3f4a1a0d4e8e5a0e6ece1e7a0e9f3baa0c4c4c3d4c6fbb9e1b2e2e5e2b5b4e4b8b7e6e1e1b6b9e4b5e3b8b1b1e3e5b5b6b4b1b0e4e6b2fd'
flag=""
for i in range(256):
    for i in range(1,len(str),2):
        flag+=chr(int((str[i-1]+str[i]),16)%128)

print(flag)
