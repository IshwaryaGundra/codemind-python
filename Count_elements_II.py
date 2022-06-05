a,b=map(int,input().split())
x=list(map(int,input().split()))
y=list(map(int,input().split()))
k=0
c=0
for i in set(x):
    if i not in y:
        k=k+1
for j in set(y):
    if j not in x:
        c=c+1
print(c+k)

