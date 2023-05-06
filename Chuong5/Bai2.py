def Nhap():
    x=int(input("x="))
    k=int(input("k="))
    n=int(input("n="))
    L=[]
    for i in range(n):
        z=int(input())
        L=L + [z]
    return x,k,L

def search(L,x):
    for i in range (len(L)):
        if L[i]==x:
            return i
    return None 
        
x,k,L=Nhap()
pos=search(L,x)
print("Ket qua tim kiem:",pos)