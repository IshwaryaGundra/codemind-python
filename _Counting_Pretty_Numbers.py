t=int(input())
for i in range(t):
    l,m=map(int,input().split())
    flag=0
    for j in range(l,m+1):
        k=j%10
        if k==2 or k==3 or k==9:
            flag+=1
    print(flag)
            