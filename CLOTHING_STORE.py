n=int(input())
l=list(map(int,input().split()))
c=0
for i in range(len(l)):
    k=0
    for j in range(i+1,len(l)):
        if l[i]==l[j]:
            k=k+1
    if k%2!=0:
        c=c+1
    else:
        c=c
print(c)
            
            
        