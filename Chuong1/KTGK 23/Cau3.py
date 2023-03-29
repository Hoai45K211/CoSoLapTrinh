n=int(input())
def LaSoNguyenTo(n): 
  x=0
  for i in range(2,n+1): 
    if n%i==0:
      x=1
  if x==0: 
    return False 
  else: 
    return True
i=n-1
while i>2:
  if LaSoNguyenTo(i)==True:
    print(i) 
    break
  i=i-1