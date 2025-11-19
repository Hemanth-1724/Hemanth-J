a=int(input())
if a%2==0:
  limit=a-1
else:
  limit=a
for i in range(limit):
  print(2*i+1,end=" ")
  if i<limit-1:
    print(",",end=" ")
