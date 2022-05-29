m=list(map(int,input().split()))
k=[]
for i in range(len(m)):
    for j in range(i+1,len(m)):
        l=(m[i]-1)*(m[j]-1)
        k.append(l)
print(max(k))