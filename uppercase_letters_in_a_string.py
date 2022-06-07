n=input()
c=0
for i in range(len(n)):
    if n[i]==n[i].upper() and n[i]!=chr(32):
        c=c+1
print(c)