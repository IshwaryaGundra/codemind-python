s=input()
s2=input()
for i in range(len(s)):
    if s2==s[i]:
        print("True")
        print(i)
        break
if s2 not in s:
    print("False")