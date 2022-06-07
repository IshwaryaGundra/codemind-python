n=input()
c=0
for i in range(len(n)):
    if n[i]==chr(32):
        continue
    c=c+1;
print(c)