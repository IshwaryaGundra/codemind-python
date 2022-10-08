n=int(input())
for i in range(n):
    x,a,b,k=map(int,input().split())
    h=x//a
    s=x//b
    if(h+s>=k):
        print("Win")
    else:
        print("Lose")

    