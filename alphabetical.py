a=int(input("Enter the number of names"))
names=[]
for i in range(a):
    k=input("Enter the names")
    names.append(k)
#arrange into alphabetical order
print(names)
print(sorted(names))