 def histogram(l):
     res=[]
     for i in l:
        a=l.count(i)
        res.append((i,a))
    return sorted(list(set(res)),key= lambda x:x[1])

print(histogram([13,12,11,13,14,13,7,7,13,14,12]))

def coursedetails(code,courses):
    for i in courses:
        if code == i[0]:
            return i[1]
def studentdetails(rollnumber,name):
    for i in name:
        if rollnumber== i[0]:
            return i[1]
def getgrades(rollnumber,grades,course):
    res=[]
    for i in grades:
        if rollnumber==i[0]:
            res.append((i[1],coursedetails(i[1],coursedetails(i[1],course),i[2])))
    return res
def transcript(coursedetails,studentdetails,grades):
    r=[]
    for i in studentdetails:
        r.append((i[0],i[1],getgrades()))
