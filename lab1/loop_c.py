import math
a=int(input())
b=int(input())
j=0

while a<=b:
	j=int(math.sqrt(a))
	if a==j*j:
		print(str(a)+' ')
	a=a+1	