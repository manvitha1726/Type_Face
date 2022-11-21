m = []
for i in range(4):
    m.append(list(map(int,input().split())))
n = 4
lt,up,rt,down = n-1,n-1,0,0
for i in range(n):
    for j in range(n):
        if m[i][j]==0:
            lt,up,rt,down = min(lt,j),min(up,i),max(rt,j),max(down,i) 
print([(up,lt),(up,rt),(down,lt),(down,rt)]) 
