n=int(input())
l=list(map(int,input().split()))
#print(l)
for i in l:
    i=abs(i)
    c=0
    if i==0:
        c=1
    while i!=0:
        r=i%10
        i=i//10
        c=c+1
    print(c,end=' ')