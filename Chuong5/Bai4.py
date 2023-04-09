def count(L):
        a=[]
        i=0
        while True:
                a=a+[L[i]]
                if L==a:
                         break
                else:i=i+1
        print(i+1)
count(L)