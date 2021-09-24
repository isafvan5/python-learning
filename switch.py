print("enter option 1 or 2 \n 1 for area of rectangle \n 2 for area of triangle")
option=int(input())
if option==1:
    l=int(input("enter the height o rectangle".title()))
    b=int(input("enter the  beadth of rectangle".title()))
    area=l*b
    print("the area o rectangle "+str(area))
elif option==2:
    l = int(input("enter the height o rectangle".title()))
    b = int(input("enter the  readth of rectangle".title()))
    area=1/2 *l*b
    print(f"the area of triangle {area}")

