A=[]
n=int(input("n="))
s=0
for i in range(0,n):
    x=int(input())
    A=A+[x]
for i in range(0,n):
    if i%2!=0:
        s=s+A[i]
print("Tong=",s,sep="")