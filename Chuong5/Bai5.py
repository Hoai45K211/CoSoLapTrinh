y=int(input('y='))
def update(L,x,y):
    a=[]
    for i in range(len(L)):
        if L[i]==x:
             a=a+[y]
        else: a=a+[L[i]]
    print(a)
update(L,x,y)
