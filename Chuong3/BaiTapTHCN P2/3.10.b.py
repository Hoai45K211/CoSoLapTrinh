n=int(input("n="))
i=1
while n>=1 and i<=n:
    print(i,end=" ")
    if i%5==0:
        print()
    i=i+1
    
#cach lam FOR
n=int(input("n="))
for i in range (1,n+1,1):
    print(i,end=" ")
    if i%5==0:
        print()
    i=i+1