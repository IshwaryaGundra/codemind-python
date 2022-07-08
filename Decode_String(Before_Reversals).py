def f(k,s):
    for i in range(k,0,-1):
        s=s[k-1::-1]+s[k::]
        k=k-1
    print(s)
n=int(input())
for t in range(n):
    l,k=map(int,input().split())
    s=input()
    f(k,s)