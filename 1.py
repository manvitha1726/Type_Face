n=int(input())
if n==0:
    print('0')
else:
    ans=''
    while n>=3:
        ans+=str(n%3)
        n=n//3
    ans+=str(n)  
        
    print(ans[::-1])  

