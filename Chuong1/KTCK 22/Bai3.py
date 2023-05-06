n1=str(input())
n2=[]
if len(n1)>=2:
    n2 = n2 + [n1[0]] + [n1[1]] + [n1[-2]] + [n1[-1]]
    for i in n2:
        print(i,end="")
else:
    None