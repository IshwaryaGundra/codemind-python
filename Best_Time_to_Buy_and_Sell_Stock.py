n=int(input())
l=list(map(int,input().split()))
k=[]
for i in range(n):
    for j in range(i+1,n):
        if l[i]-l[j]<0:
            k.append(abs((l[i]-l[j])))
if k!=[]:
    print(max(k))
else:
    print(0)