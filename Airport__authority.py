n=int(input())
c=0
k=[]
#print(n)
for i in range(n):
    z=int(input())
    k.append(z)
    #print(z)
y=int(input())
for i in k:
    if i<=y:
        c=c+1
    else:
        c=c+2
print(c)