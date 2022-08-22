def f(l):
    p=[]
    for j in l:
        m=[]
        for k in range(1,j+1):
            if(j%k==0):
                m.append(k)
        if sum(m) in l:
            p.append(j)
    s=sorted(p)
    if len(s)!=0:
        print(*s)
    else:
        print("-1")
a=input()
l=[]
for i in a:
    if i.isdigit():
        l.append(int(i))
f(l)
        