def Nhap():
    x=int(input("x="))
    k=int(input("k="))
    n=int(input("n="))
    L=[]
    for i in range(n):
        z=int(input())
        L=L + [z]
    return x,k,L

def delete(L,x):
    M=[]
    for z in L:
        if z!=x:
            M=M+[z]
    return M
   
x,k,L=Nhap()
M=delete(L,x)
print(M)