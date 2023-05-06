a=[]
x=0
SND=0
TBC=0
c=0
n=int(input("n="))
for i in range(n):
    b=int(input())
    a.append(b)
for i in range(len(a)):
    if a[i]>=0:
        SND+=1
    if a[i]%2==0:
        x=x+a[i]
        c+=1
if c==0:
    TBC=0
else:
    TBC=x/c
print("SND=",SND,sep="")
print("TBC=",TBC,sep="")
