n=input()
l=list(map(int,input().split()))
k=[]
s1=0
s2=0
for i in range(len(n)):
    for x in l:
        if x not in k:
            k.append(x)
            s1=s1+x
    for y in l: 
        if y not in k:
            k.append(y)
            s2=s2+y
#print(s1)
#print(s2)
if abs(s2-s1)%4==0:
    print("X")
else:
    print("Y")