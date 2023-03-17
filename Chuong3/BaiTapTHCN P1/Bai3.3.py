x=float(input("x="))
y=float(input("y="))
ch=str(input("Phep toan:"))
if ch=="+":
    print(x,"+",y,"=",round((x+y),1),sep="")
elif ch=="-":
    print(x,"-",y,"=", round((x-y),1),sep="")
elif ch=="*":
    print(x,"*",y,"=",round((x*y),1),sep="")
elif ch=="/":
    if y==0:
        print("Khong hop le")
    else:
        print(x,"/",y,"=",round((x/y),1),sep="")
else:
    print("Khong hop le")