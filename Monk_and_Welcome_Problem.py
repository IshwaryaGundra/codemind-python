n=int(input())
l=list(map(int,input().split()))
k=list(map(int,input().split()))
m=[]
for i in range(len(l)):
    m.append(l[i]+k[i])
print(*m)
