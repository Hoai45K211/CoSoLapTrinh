a=float(input("a="))
b=float(input("b="))
c=float(input("c="))
max=a
if b>max:
     max=b
if c>max:
     max=c
print("SLN=",max,sep=(""))
min=a
if b<min:
    min=b
if c<min:
    min=c
print("SBN=",min,sep=(""))