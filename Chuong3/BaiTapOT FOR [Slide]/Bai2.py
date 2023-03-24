n=int(input("n="))
isOK=False 
for i in range(2,n):
    if n%i==0:
        isOK=True
        break

if isOK:  
    print(n," khong la SNT",sep="")
else:
    print(n," la SNT",sep="")