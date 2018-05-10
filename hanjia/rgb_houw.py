from PIL import Image
import numpy
fp=open('rgb.txt','r')
line=fp.readlines()
for i,j in enumerate(line):
    line[i]=j[:-1]
print(line)
pict=[]
array=[]
j=0
f=open('flag.txt','w')
print(len(line))
for i in range(len(line)):
    array.append(int(line[i][0]))
    array.append(int(line[i][2]))
    array.append(int(line[i][4]))
    j+=1
    f.write(line[i])
    f.write(" ")
    if j ==280:
        for i,j in enumerate(array):
            if array[i]==1:
                array[i]=255
        j=0
        pict.append(array)
        f.write("\n")
        array=[]

pict=numpy.array(pict).reshape((280,840))
print(pict)
im=Image.fromarray(pict)
im.show()

