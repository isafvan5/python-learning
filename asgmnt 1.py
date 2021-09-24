def shuffle(l1,l2):
    lf=[]
    for i,j in zip(l1,l2):
        lf.append(i)
        lf.append(j)
    if len(l1) >len(l2):
        for i in l1[len(l2):]:
            lf.append(i)
    elif len(l1)<len(l2):
        for i in l2[len(l1):]:
             lf.append(i)
    return lf

print(shuffle([1,3,5,7,9],[]))