n=int(input())
m=int(input())
k=[]
for i in range(n+1,m+1):
    c=0
    for j in range(2,(i//2)+1):
        if i %j==0:
            c+=1
    if c==0:
        k.append(i)
for m in range(len(k)):
    print(k[m])