n=int(input())
l=list(map(int,input().split()))
m=int(input())
for i in l:
    if i+m>=max(l):
        print("True",end=' ')
    else:
        print("False",end=' ')