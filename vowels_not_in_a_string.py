n=input()
k=['a','e','i','o','u']
m=[]
for i in k:
    if i not in n :
        m.append(i)
if(m==[]):
    print(0)
else:
    print(*m)
        