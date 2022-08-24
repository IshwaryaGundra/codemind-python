n=int(input())
l=list(map(int,input().split()))
for i in l:
    s=0
    while i!=0:
        r=i%10
        s=s*10+r
        i=i//10
    print(s,end=" ")
