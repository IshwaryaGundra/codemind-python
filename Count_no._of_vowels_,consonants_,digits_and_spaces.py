s=input()
c=0
k=0
v=0
w=0
for i in s:
    if i in "aeiou":
        v+=1
for i in s:
    if i.isalpha()==True and i not in "aeiou":
        k+=1
for i in s:
    if i.isnumeric()==True:
        c+=1
for i in s:
    if i==" ":
        w+=1
print("Vowels"":" , v)
print("Consonants:", k)
print("Digits:", c)
print("White spaces:" ,w)