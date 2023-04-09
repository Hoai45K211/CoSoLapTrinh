def search(L,x):
    a=[]
    for i in range(len(L)):
        if L[i]==x:
            a=a+[i]
    if a!=[]:
        print(a)
    else:
        print('None')
search(L,x)