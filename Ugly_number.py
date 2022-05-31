n=int(input())
def maxdiv(a,b):
    while a%b==0:
        a=a//b
    return a
def isugly(n):
    n=maxdiv(n,2)
    n=maxdiv(n,3)
    n=maxdiv(n,4)
    if n==1:
        return 1
    else:
        return 0
if isugly(n):
    print("Ugly Number")
else:
    print("Not Ugly Number")