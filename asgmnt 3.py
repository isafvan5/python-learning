'''def expanding(l):
    lis=[]
    for i in range(len(l)-1):
        n=abs(l[i+1]-l[i])
        lis.append(n)
    for i in range(len(lis)-1):
        if lis[i+1] < lis[i]:
            return False
    return True
print(expanding([1,3,7,2,9])) '''

# def sumsquare(l):
#     le=[]
#     lo=[]
#     for i in l:
#         if i % 2==0:
#            le.append(i*i)
#         else:
#             lo.append(i*i)
#     b=sum(lo)
#     a=sum(le)
#
#
#     return [b,a]
# print(sumsquare([1,3,5]))


def transpose(l):
    c=[]
    for i in l:
        for j in i:
            print(j,end=" ")
        print("")
    for i in l:
        for j in i:
            c[j][i]=l[i][j]
    for i in c:
        for j in i:
            print(j, end=" ")
        print("")


print(transpose([[1,2,3],[4,5,6]]))




