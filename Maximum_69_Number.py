n=list(input())
t=n
l=[]
l.append("".join(n))
for i in range(len(n)):
    n=t
    if(n[i]=='6'):
        n[i]='9'
        l.append("".join(n))
        break
print(int(max(l)))