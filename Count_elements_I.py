a,b=map(int,input().split())
x=list(map(int,input().split()))
y=list(map(int,input().split()))
c=0
for i in set(x):
    if i in set(y):
        c=c+1
    
print(c)
    
