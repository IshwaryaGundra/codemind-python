n=int(input())
s=0
k=0
a=list(map(int,input().split()))
for i in range(len(a)):
    if i%2!=0:
        s=s+a[i]
        #print(s)
    else:
        k=k+a[i]
        #print(k)
if(s-k==0):
    print("YES")
else:
    print("NO")
    