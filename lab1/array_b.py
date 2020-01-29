a = int(input())

arr = []
ans = ""
Arr = input().split()

for i in range(len(Arr)):
  Arr[i] = int(Arr[i])

for i in range(0,len(Arr), 1):
  if(Arr[i]%2 == 0):
    ans += (str(Arr[i]) + " ")
print(ans)