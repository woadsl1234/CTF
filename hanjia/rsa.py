primes=[907, 787, 929, 877, 577, 593, 977, 659, 569, 919, 797, 563, 541, 883, 727, 863, 677, 911, 821, 647, 653, 557, 701, 839, 719, 757, 631, 809, 673, 691, 739, 983, 521, 641, 971, 773, 1019, 643, 683, 937, 761, 1009, 857, 769, 733, 853, 991, 887, 967, 953, 607, 881, 751, 811, 743, 709, 619, 997, 587, 617, 829, 941, 613, 571, 1021, 859, 1013, 523, 823, 599, 547, 661, 947, 1031, 827, 601]
flag=open('flag.txt','w')
# print prime,len(prime)   76
f=[]
with open('cipherx.txt','r') as fp:
	f=fp.readlines()

e=65537
d=0
n=0
r=0
for p in primes[::-1]:
    primes.pop()
    for q in primes:
        if p != q:
            n = p * q
            r=(p-1)*(q-1)
            for n in range(2,r):
                if (e*n)%r==1:
                    d=n
                    break
            for i in f:
                test=pow(int(i),d,n)
                str2='%x'%(int(test))
                try:
                    tflag=str2.decode('hex')
                    tflag+='\n'
                    flag.write(tflag)
                except:
                    pass