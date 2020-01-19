a=int(input())

i=1
isPower=False

while i<=a:
  if i==a:
    isPower=True
  i*=2
  
if isPower==True:
  print('YES')
else:
  print('NO')