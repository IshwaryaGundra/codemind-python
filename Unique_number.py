n=input()
n.split()
if len(n)==len(set(n)):
    print("Unique Number")
else:
    print("Not Unique Number")