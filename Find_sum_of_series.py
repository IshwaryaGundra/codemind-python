n=int(input())
s=0
for i in range (1,n+1):
    s=s+1/i
float=s
format_float="{:.2f}".format(float)
print(format_float)
    