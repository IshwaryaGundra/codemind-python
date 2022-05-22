n= int(input())  
nd = len(str(n))  
square = n**2  
ld= square%pow(10,nd)  
if ld==n:  
  print("Automorphic Number".format(n))  
else:  
  print("Not an Automorphic Number".format(n))  