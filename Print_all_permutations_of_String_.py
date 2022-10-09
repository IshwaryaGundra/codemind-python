from itertools import *
def per(s):
    k=permutations(s)
    for i in list(k):
        print("".join(i))
n=input()
per(n)