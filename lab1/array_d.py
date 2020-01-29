a = int(input())

arr = []
ans = ""
Arr = input().split()

for i in range(len(Arr)):
  Arr[i] = int(Arr[i])

cnt=0
for i in range(1,len(Arr), 1):
  if(Arr[i] > Arr[i-1]):
    cnt=cnt+1
print(cnt)