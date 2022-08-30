n,k=map(int,(input().split()))
l=list(map(int,input().split()))
c=0
for i in range(0,n):
    s=0
    for j in range(i,n):
        p=l[i:j+1]
        if sum(p)==k:
            c=c+1
print(c)

    
   