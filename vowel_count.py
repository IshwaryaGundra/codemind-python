n=(input())
c=0
for i in range(len(n)):
    if n[i] in 'aeiouAEIOU':
        c=c+1
print(c)
