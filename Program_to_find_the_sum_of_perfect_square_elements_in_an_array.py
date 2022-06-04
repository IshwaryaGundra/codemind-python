n=int(input())
s=0
a=list(map(int,input().split()))
for i in a:
    for j in range(1,i+1):
        if i==j*j:
            s=s+i
print(s)
    