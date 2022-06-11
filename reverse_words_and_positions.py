s=input()
x=s.split()
k=[]
for i in x:
    s=i[::-1]
    k.append(s)
for i in k:
    s=k[::-1]
print(*s)