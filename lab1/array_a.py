n=int(input())
arr=[]

i=1
while i<=n:
	k=int(input())
	arr.append(k)
	i=i+1

for j in range(0,len(arr)):
	if j%2==0:
		print(arr[j],' ')