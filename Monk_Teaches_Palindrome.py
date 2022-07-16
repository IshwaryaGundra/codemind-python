n=int(input())
for i in range(n):
    z=input()
    if z==z[::-1]:
        if len(z)%2==0:
            print("YES","EVEN")
        else:
            print("YES","ODD")
    else:
        print("NO")
            
        