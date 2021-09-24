a=int(input(("enter the prime  numbers to print")))
primes=[]
for j in range(a):
    prime=True
    for i in range(2, j):
        if j % i == 0:
            prime = False
            break
    if prime:
        primes.append(j)
primes.remove(0)
primes.remove(1)
print("the list of prime numbers "+str(primes))










