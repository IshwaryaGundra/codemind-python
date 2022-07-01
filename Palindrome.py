n=int(input())
temp=n
s=0
while(n!=0):
    k=n%10
    s=s*10+k
    n=n//10
if(temp==s):
    print(True)
else:
    print(False)
    