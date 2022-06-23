n=int(input())
l=list(map(int,input().split()))
k=int(input())
f=0
for i in range(len(l)):
    if k==l[i]:
        f=1
        print(i)
if f==0:
    print(-1)