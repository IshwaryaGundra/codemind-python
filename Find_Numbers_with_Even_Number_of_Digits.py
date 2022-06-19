n=input()
l=list(map(int,input().split()))
k=0
M=[]
for i in l:
    c=0
    while(i!=0):
        d=i%10
        i=i//10
        c=c+1
    M.append(c)
    #print(M)
for i in M:
    if i%2==0:
        k=k+1
print(k)
    