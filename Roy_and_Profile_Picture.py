i=int(input())
n=int(input())
while n:
    a,b=map(int,input().split())
    if a<i or b<i:
        print('UPLOAD ANOTHER')
    elif a==b:
        print("ACCEPTED")
    else:
        print('CROP IT')
    n=n=-1