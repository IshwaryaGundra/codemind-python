n=int(input())
flag=0
for i in range(1,n+1):
    if n==i*(i+1):
        flag=1
        break
if flag==1:
    print("YES")
else:
    print("NO")
    