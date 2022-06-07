n=input()
c=0
for i in range(len(n)):
    if n[i]==n[i].lower() and n[i]!=chr(32):
        c=c+1
print(c)