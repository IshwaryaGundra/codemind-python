n=int(input())
l=list(map(int,input().split()))
s=0
c=0
for i in l:
    s=s+i
avg=s//n
for i in l:
    if i>=avg:
        c=c+1
print(c)
    