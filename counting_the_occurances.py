s=input()
c=input()
k=0
for i in s:
    if i==c:
        k=k+1
if k==0:
    print(-1)
else:
    print(k)
