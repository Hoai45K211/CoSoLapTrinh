def Nhap():
    x=int(input("x="))
    k=int(input("k="))
    n=int(input("n="))
    L=[]
    for i in range(n):
        z=int(input())
        L=L + [z]
    return x,k,L

def replace(L,x,y):
    for i in range (len(L)):
        if L[i]==x:
            L[i]=y
    return L

x,k,L=Nhap()
y=int(input("y="))
L=replace(L,x,y)
print(L)