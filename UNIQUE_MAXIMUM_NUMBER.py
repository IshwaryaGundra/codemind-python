n=input()
l=list(map(int,input().split()))
k=[]
for i in set(l):
    if l.count(i)==1:
        k.append(i)
if k !=  []:
    print(max(k))
if k==[]:
    print("-1")