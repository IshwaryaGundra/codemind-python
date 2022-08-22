t=int(input())
for i in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    s1=n*(n+1)/2
    print(int(s1-sum(l)))
    