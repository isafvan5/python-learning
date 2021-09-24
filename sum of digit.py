a=int(input("enter the number ".upper()))
s=0
while a !=0:
    reminder=a%10
    s +=reminder
    a //=10

print("sum of digit is "+str(s))
