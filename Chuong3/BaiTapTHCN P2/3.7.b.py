n=int(input())
b=1
while n>=0:
    for i in range(1,n+1):
        if n==0:
            print(1)
            n=int(input())
            continue
        b=b*i
    print(b)
    n=int(input())
    b=1
    continue