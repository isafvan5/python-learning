print("electricty bill".upper())
usage=int(input("enter the usage "))


if usage <=100:
    usage=usage*3.50
    tax=usage*.12
elif usage <= 200:
    usage=100 * 3.50+(usage-100)*4
    tax=usage*0.12
elif usage <= 500:
    usage=100*3.50+100*4+(usage-200)*5
    tax=usage*0.12
else:
    usage=100*3.50+100*4+100*5+(usage-300)*8
    tax=usage*0.12

total =usage+tax+40
print("total amount to pay ".upper()+str(total))