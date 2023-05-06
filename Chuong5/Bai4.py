def Nhap():
    x=int(input("x="))
    k=int(input("k="))
    n=int(input("n="))
    L=[]
    for i in range(n):
        z=int(input())
        L=L + [z]
    return x,k,L

def count(L):
    dem=0
    for x in L:
        dem=dem+1
    return dem
       
x,k,L=Nhap()
soluong=count(L)
print(soluong)