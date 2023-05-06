A=[]
B=[]
n=input()
for i in n:
    if i not in A:
        A+=[i]
    else:
        B+=[i]
if B!=[]:
    kq=B[0]
    print(kq)
else:
    print("None")