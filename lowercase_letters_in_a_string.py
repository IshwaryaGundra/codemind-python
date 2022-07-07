s=input()
l="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
c=0
for i in s:
    if i in l.lower():
        c+=1
print(c)