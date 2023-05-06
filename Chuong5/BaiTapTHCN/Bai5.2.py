def Input():
    L=[]
    global n
    n=int(input("n="))
    for i in range(0,n):
        x=int(input())
        L=L+[x]
    return L
def Search(L):
   max=L[0]
   for i in range(0,n):
       if max<L[i]:
           max=L[i]
   min=L[0]
   for i in range(0,n):
       if min>L[i]:
           min=L[i]
   return max,min
def Output(max,min):
    print(max,min)

L=Input()
max,min=Search(L)
Output(max,min)