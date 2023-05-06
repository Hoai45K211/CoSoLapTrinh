L=[]
M=[]
n=int(input("n="))
for i in range(1,n+1):
    x=int(input())
    L.append(x)
for i in L:
    if i not in M:
        M.append(i)
for i in M:
    print(i,end=" ")