n=int(input())
temp=n
s=0
for i in range(1,n):
    if n%i==0:
        s=s+i
        #print(s)
if s>temp:
    print("True")
else:
    print("False")