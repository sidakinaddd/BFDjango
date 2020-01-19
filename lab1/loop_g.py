import math

a=int(input())
minn=300000
i=2
while i<=a:
	if a%i==0 and i<minn:
		minn=i
	i=i+1


print(minn)		