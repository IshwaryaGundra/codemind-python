a,b=map(int,input().split())
x=list(map(int,input().split()))
y=list(map(int,input().split()))
k=[]
for i in range(len(x)):
    if x[i] not in y:
        k.append(x[i])
for j in range(len(y)):
    if y[j] not in x:
        k.append(y[j])
print(*k)
    
