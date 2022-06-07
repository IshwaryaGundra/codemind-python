n=input()
c=0
p=['a','e','i','o','u','A','E','I','O','U']
k=n.split()
#print(k)
for i in k:
    m=len(i)
        #print(i[j])
        #print(i[0],i[m-1],end=' ')
    if i[0] in p and i[m-1] not in k:
        #print(i[0],i[m-1],end='')
        c=c+1
print(c)       