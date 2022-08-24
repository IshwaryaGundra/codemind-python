n=int(input())
l=list(map(int,input().split()))
#print(l)
c=0
for i in l:
    temp=i
    #print(temp,end=" ")
    s=0
    while temp!=0:
        r=temp%10
        s=s*10+r
        temp=temp//10
    #print(s)
    if s==i:
        c=c+1
print(c)
        