s1=input()
s2=input()
ans=0
last_c=s2[-1]
for i in s1:
    if i==last_c:
        ans+=1
print(ans)