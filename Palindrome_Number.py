x=int(input())
for i in range(x):
    z=int(input())
    temp=z
    s=0
    while z:
        d=z%10
        z=z//10
        s=s*10+d
    if(s==temp):
        print("True")
    else:
        print("False")