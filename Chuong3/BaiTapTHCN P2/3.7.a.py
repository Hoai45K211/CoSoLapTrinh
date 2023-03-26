while True:
    n=int(input("n="))
    t=1
    i=1
    while i<=n:
        t=t*i
        i=i+1
    if n<0:
        break
    print("n!=",t,sep="")