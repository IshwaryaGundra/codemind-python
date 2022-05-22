n=int(input())
flag=0
for i in range(1,n//2):
    if n==i**2:
        flag=1
if flag==1:
    print("True")
else:
    print("False")