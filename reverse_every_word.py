s=input()
x=s.split()
k=[]
for i in range(len(x)):
        p=x[i]
        k.append((p[::-1]))
print(*k)