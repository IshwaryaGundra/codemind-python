n=int(input())
l=list(map(int,input().split()))
s=0
c=0
for i in l:
    s=s+i
avg=s//n
#print(avg)
for i in range(len(l)):
    if l[i]>=avg:
        #print(i,end=" ")
        c=c+1
print(c)