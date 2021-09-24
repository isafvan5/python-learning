# def is_prime(n):
#     for i in range(2,n):
#         if n%i==0:
#             return False
#     return True
#
# def factors(n):
#     for i in range(2,n):
#         if n%i==0:
#             a=n//2
#             return (i,a)
# def primeproduct(n):
#     if factors(n)==is_prime(n):
#         return False
#     return True
#
# print(primeproduct(188))

# def delchar(s,c):
#     k=list(s)
#     if len(c) !=1:
#         return s
#     while True:
#         if k.count(c) >0:
#             k.remove(c)
#         else:
#             break
#     return "".join(k)
#
# print(delchar("banana","n"))
#


def devide(n,m):
    try:
        return n/m
    except ZeroDivisionError:
        print("denominater cannot be zero")

while True:
    x=int(input("Enter a number "))
    y=int(input("Enter anthr number"))
    print(devide(x,y))





