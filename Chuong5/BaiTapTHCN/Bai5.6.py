A=[]
B=[]
for i in range(0,10):
    x=int(input())
    A.append(x)
    B.append(x)
for i in range(0,10,2):
    B[i]=A[i+1]
    B[i+1]=A[i]
for i in range(len(B)):
    print(B[i],end=" ")