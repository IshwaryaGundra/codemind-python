n=int(input())
m=list(map(int,input().split()))
k=[]
for i in m:
    k.append(i*i)
print(*(sorted(k)))