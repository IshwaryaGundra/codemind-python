def prime(i):
    if i==1:
        return 1
    for j in range(2,int(i**0.5+1)):
        if i%j==0:
            return 0
    return 1
x=int(input())
y=int(input())
a=x+y
for i in range(1,10):
    k=a+i
    if prime(k):
        print(i)
        break