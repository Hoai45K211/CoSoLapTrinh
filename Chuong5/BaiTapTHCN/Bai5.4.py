L=[]
n=int(input("n="))
for i in range(0,n):
    x=int(input())
    L=L+[x]
L.reverse()
print(L)
L.sort()
print(L)