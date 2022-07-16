s=input()
k=0
for i in s:
    if i.isnumeric()==True:
        k+=1
if k==0:
    print("Doesn't contain digit")
else:
    print("Contains",k,"digit")
