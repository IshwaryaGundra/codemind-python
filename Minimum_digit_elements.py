n=input()
#print(n)
a=list(map(int,input().split()))
#print(a)
k=[]
for i in range(len(a)):
    c=0
    #print(a[i],end=' ')
    while a[i]!=0:
        d=a[i]%10
        c=c+1
        a[i]=a[i]//10
    k.append(c)
    #print(c,end=' ')
    
print(k.count(min(k)))