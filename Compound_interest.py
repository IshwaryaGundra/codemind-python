p,r,t = map(float,input().split())
a=p * (pow((1 + r / 100), t)) 

#format_float={:.2f}.format(float)
print('%.2f'%a)

