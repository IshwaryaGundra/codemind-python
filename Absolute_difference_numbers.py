m,n=map(int,input().split())
s=0
o=0
str1=""
k=[]
a=[]
q=[]
while m!=0:
    d=m%10
    s=s*10+d
    m=m//10
#print(q)
while s!=0:
    l=s%10
    k.append(l)
    s=s//10
#print(k)
for i in range(0,n):
    a.append(k[i])
    b=(''.join(map(str, a)))
#print(b)
y=len(k)
for j in k[y:(y-n)-1:-1]:
    #print([j])
    q.append(j)
    p=''.join(map(str,q))
h=int(p)
#print(p)
while h!=0:
    v=h%10
    o=o*10+v
    h=h//10
print(abs(int(b)-int(o)))
    
    
        