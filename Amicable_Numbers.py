a=int(input())
b=int(input())
t1=a
t2=b
s=0
k=0
for i in range(1,a):
    if t1%i==0:
        s=s+i
for j in range(1,b):
    if t2%j==0:
        k=k+j
if a==k and b==s:
    print("Amicable")
else:
    print("Not Amicable")