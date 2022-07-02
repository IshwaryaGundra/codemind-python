n=int(input())
k=1
s=0
k=1
l=0
temp=n
while n!=0:
    d=n%10
    n=n//10
    s=s*10+d
while s!=0:
    m=s%10
    s=s//10
    l=l+m**k
   # print(l)
    k=k+1
if l==temp:
    print("True")
else:
    print("False")
