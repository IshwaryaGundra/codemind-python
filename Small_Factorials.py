def fact(z):
    k=z
    for i in range(z-1,1,-1):
        k=k*i
    return k
n=int(input())
for i in range(n):
    z=int(int (input()))
    print(fact(z))