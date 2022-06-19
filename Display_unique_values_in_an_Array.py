m=input()
n=list(map(int,input().split()))
k=[]
for i in (n):
    if n.count(i)>1:
        continue
    else:
        k.append(i)
if k!=[]:
    print(*k)
if k==[]:
    print("-1")