n=int(input("Enter the number of students"))
heights=[]
for i in range(n):
    y=int(input("Enter the height of students "))
    heights.append(y)

s=sum(heights)
mean=s/n
print(mean)

