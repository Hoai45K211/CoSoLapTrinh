def Nhap():
    x=int(input("x="))
    k=int(input("k="))
    n=int(input("n="))
    L=[]
    for i in range(n):
        z=int(input())
        L=L + [z]
    return x,k,L


def add(L,x,k):
    L=L[:k] + [x] + L[k:]
    return L


x,k,L=Nhap()
L=add(L,x,k)
print(L)