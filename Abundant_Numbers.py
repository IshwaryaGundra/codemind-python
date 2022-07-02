n=int(input())
temp=n
s=0
#print(n)
for i in range (1,n):
    if temp%i==0:
        s=s+i
#print(s)
if n<s:
    #print(n)
    print("True")
else:
    print("False")