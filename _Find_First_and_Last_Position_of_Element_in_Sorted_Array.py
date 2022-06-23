n=int(input())
l=list(map(int,input().split()))
k=int(input())
m=[]
for i in range(len(l)):
    if l[i]==k:
        m.append(i)
if m!=[]:
    print(m[0],m[len(m)-1])
if m==[]:
    print(-1,-1)