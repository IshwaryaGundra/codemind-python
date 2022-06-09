n=input()
k=n.split()
c=0
m=[]
for i in k:
    c=0
    for j in i:
        if j in "aeiou":
            c=c+1
    m.append(c)
print(m.count(max(m)))