t=int(input())
for i in range(t):
    n,k=map(int,input().split());
    l=list(map(int,input().split()))
    print(*(l[n-k::]+l[0:n-k]))