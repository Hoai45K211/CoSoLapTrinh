import math
def nhap():
    print("Nhap 3 so nguyen:")
    a=int(input("a="))
    b=int(input("b="))
    c=int(input("c="))
    return a,b,c

def giaipt(a,b,c):
    delta=b*b-4*a*c
    if delta==0:
        x1=-b/2*a
        x2=x1
        return x1,x2
    elif delta<0:
        x1="None"
        x2="None"
        return x1,x2
    else:
        x1=((-b+math.sqrt(delta))/(2*a))
        x2=((-b-math.sqrt(delta))/(2*a))
        return x1,x2

def inkq(x1,x2):
    if x1==x2 and x1!="None" and x2!="None":
        print("Phuong trinh co nghiem kep")
        print("x1=x2=",x1,sep="")
    elif x1=="None":
        print("Phuong trinh vo nghiem")
    else:
        print("Phuong trinh co hai nghiem")
        print("x1=",x1,sep="")
        print("x2=",x2,sep="")

a,b,c=nhap()
x1,x2=giaipt(a,b,c)
inkq(x1,x2)