n=int(input())
l1=list(map(int,input().split()))
ind=int(input())
l2=list(map(int,input().split()))
k=[]
for n,ind in zip(l1,l2):
    k.insert(ind,n)
print(*k)