n=int(input("n="))
i=1
while n>=1 and i<=n:
    print(i,end=" ")
    if i%5==0:
        print()
    i=i+1