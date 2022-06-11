s=input()
x=s.split()
k=[]
for i in range(len(x)):
    if i %2==0:
        p=x[i]
        k.append((p[::-1]))
    else:
        k.append(x[i])
print(*k)