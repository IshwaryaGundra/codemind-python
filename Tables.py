n,r=map(int,input().split())
for i in range(1 ,r+1):
    if(i%2==0):
        continue
    k=n*i
    print(n, 'x', i, '=', k)