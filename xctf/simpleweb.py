x=0x23332333
y=0x100

arr2=[35,51,35,51]
b=x
# for i in range(4):
#     a=b
#     a=b%y
#     print(a)
#     b=(b-a)/y
#     print(b)
#     arr2.append(a)
# print(arr2)

arr1=[15,20,31,4,47]

for i in range(51):
    for j in range(51):
        for k in range(51):
            for u in range(51):
                for y in range(51):
                    if i+j==35 and j+k==51 and k+u==35 and u+y==51:
                        print(i,j,k,u,y)