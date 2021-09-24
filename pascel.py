a=int(input("enter the number of rows"))
for i in range(a):
    for j in range(a-i):
        print(" ",end=" ")
    for k in range(i):
        if i==0 or k==0:
            flag=1
        else:
            flag=flag*(i-k+1)//k
        print(flag,end=" ")


