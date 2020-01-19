import math
a=int(input())
i=1
cnt=0
while i<=a:
	if a%i==0:
		cnt=cnt+1
	i=i+1
print(cnt)
		
