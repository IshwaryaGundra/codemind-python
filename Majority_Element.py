n = int(input()) 
a = list(map(int,input().split()))
for i in a:
    #print(a)
    if n//2<a.count(i):
        print(i)
        break