def add(L,x,k):
    if k<=len(L):
         L=L[:k]+[x]+L[k:]
    else:
         L=L+[x]
    print(L)
L=[1,2,3,4,5,6,7]
k=int(input('k='))
x=int(input('x='))
add(L,x,k)