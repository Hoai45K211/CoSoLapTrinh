def Input():
    L=[]
    n=int(input("n="))
    for i in range(1,n+1):
        z=int(input())
        L=L+[z]
    x=int(input("x="))
    return L,x
def FirstAndLast(L):
    L1=L.copy()
    del(L1[1:len(L1)-1])
    print(L1)
def Search(L,x):
    if x in L:
        return True
    return False

L,x=Input()
FirstAndLast(L)
check=Search(L,x)
print(check)