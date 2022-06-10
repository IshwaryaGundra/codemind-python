s=input()
def isisogram(s):
    if len(s)==len(set(s)):
        return 1
    else:
        return 0
if isisogram(s):
    print("True")
else:
    print("False")