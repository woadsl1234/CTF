# -*- encoding: utf-8 -*-
import btc, rsa, uuid, json, copy
#创世块的hash
genies_hash = "92875ca628cd0890020f6a74f3011b611db814f30300f729f20b5a88c49e3e44"
#黑客转账999999,所用的input和签名
input,signature = ("9018b356-cb1d-44c9-ab4e-bf15a8b2f95c","161ae7eac89f71d50d1019d21288dce23cae6cbb587998df9010e3ff3c80ee8e4c06bd70555604be85ca0869136b3966")
#商店地址
shop_address = "b81ff6d961082076f3801190a731958aec88053e8191258b0ad9399eeecd8306924d2d2a047b5ec1ed8332bf7a53e735"
txout_id = str(uuid.uuid4())
#工作量证明
def pow(b, difficulty, msg=""):
    nonce = 0
    while nonce<(2**32):
        b['nonce'] = msg+str(nonce)
        b['hash'] = btc.hash_block(b)
        block_hash = int(b['hash'], 16)
        if block_hash < difficulty:
            return b
        nonce+=1   
def myprint(b):
    print(json.dumps(b))
    print(len(json.dumps(b)))
#构造一个空块
def empty_block(msg, prevHash):
    b={}
    b["prev"] = prevHash
    b["transactions"] = []
    b = pow(b, btc.DIFFICULTY, msg)
    return b
#从创世块开始分叉，给商店转1000000
block1 = {}
block1["prev"] = genies_hash
tx = {"input":[input],"output":[{"amount":1000000, 'id':txout_id,'addr':shop_address}],'signature':[signature]}
tx["output"][0]["hash"] = btc.hash_utxo(tx["output"][0])
tx['hash'] = btc.hash_tx(tx)
block1["transactions"] = [tx]
block1 = pow(block1, btc.DIFFICULTY)
myprint(block1)
#构造空块增加分叉链长度，使分叉链最长，因为max的结果不唯一，少则一次多则两次
block2 = empty_block("myempty1", block1["hash"])
myprint(block2)
block3 = empty_block("myempty2", block2["hash"])
myprint(block3)
#余额更新成功,系统自动添加块，转走商店钱，钻石+１
#从自己的块，即系统转走钱之前的那个块再次分叉，添加空块
block4 = empty_block("myempty3", block3["hash"])
myprint(block4)
block5 = empty_block("myempty4", block4["hash"])
myprint(block5)
#新的分叉链最长，余额更新成功，钻石+１