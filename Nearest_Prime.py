def prime(i):
    if i==1:
        return 1
    for j in range(2,int(i**0.5)+1):
        if i%j==0:
            return 0
    return 1
x=int(input())
for j in range(x):
    k=int(input())
    for i in range(k-1,2,-1):
        if prime(i):
            h=i
            break
    for m in range(k,k+100):
        if prime(m):
            z=m
            break
    if (abs(h-k)<=abs(k-z)):
        print(h)
    else:
        print(z)