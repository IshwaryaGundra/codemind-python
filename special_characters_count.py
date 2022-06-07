n=input()
#print(n)
c=0
for i in range(len(n)):
    ch=n[i]
    if n[i].isalpha():
        continue
    elif n[i].isdigit():
        continue
    elif n[i]==chr(32):
        continue
    else:
        c=c+1
        
print(c)