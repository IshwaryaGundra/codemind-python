def OctToBin(num):
    return bin(int(num, 8))
onum = input()
bnum = OctToBin(onum)
print( bnum[2:])