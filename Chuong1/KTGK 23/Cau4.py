n=int(input()) 
d=0
for i in range (1,n+2): 
  if i%2==0 and i%3==0: 
    d=d+1
print(d)