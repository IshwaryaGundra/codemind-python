n=int(input())
s=0
temp=n
while n!=0:
    n=abs(n)
    r=n%10
    s=s*10+r
    n=n//10
if temp>=0:
    print(s)
else:
    print(-s)