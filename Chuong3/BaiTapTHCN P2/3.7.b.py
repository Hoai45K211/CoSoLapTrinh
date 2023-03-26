n=int(input("n="))
b=1
while n>=0:
    for i in range(1,n+1):
        if n==0:
            print("n!=1")
            n=int(input("n="))
            continue
        b=b*i
    print("n!=",b,sep="")
    n=int(input("n="))
    b=1
    continue