def rev(val):
    r=0
    while val!=0:
        d=val%10
        r=r*10+d
        val=val//10
    return r
def adam(n):
    a=n**2
   # print(a)
    b=rev(n)
   # print(b)
    c=b**2
    if(a==rev(c)):
        return 1
    else:
        return 0
    
k=int(input())
if adam(k):
    print("True")
else:
    print("False")