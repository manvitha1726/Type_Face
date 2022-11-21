valid=[0,1,2,5,6,8,9]
inp=int(input())
i=1
got=0

while got!=inp:
    if i in valid:
        got+=1
    else:
        c=1
        for j in str(i):
            if int(j) not in valid:
                c=0
                break
        if c==1:
            got+=1
    i+=1
print(i-1)