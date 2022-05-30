n=int(input())
k=[]
while n!=0:
    d=n%10
    k.append(d)
    n=n//10
print(max(k))