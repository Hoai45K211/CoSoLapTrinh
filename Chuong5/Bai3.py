def delete(L,x):
    a=[]
    for i in range(len(L)):
        if L[i]==x:
            continue
        else: a=a+[L[i]]           
    print(a)
delete(L,x)
