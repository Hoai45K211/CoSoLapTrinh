def Nhap():
    global tu,mau
    tu=int(input("Nhap tu so cua phan so:"))
    mau=int(input("Nhap mau so cua phan so:"))
    if mau==0: 
        print("Khong hop le! Mau so phai khac 0! Vui long nhap lai.")
        tu=int(input("Nhap tu so cua phan so:"))
        mau=int(input("Nhap mau so cua phan so:"))
    return tu,mau
def uoc(t, m):
    u = min (t,m)
    while   t%u !=0 or m%u != 0:
        u=u-1
    return u
def rut(tu,mau):
    if tu == 0:
        return  (0,None)
    nn =  uoc(tu, mau)
    return  (tu // nn,mau // nn)
tu,mau=Nhap()
(t,m)=rut(tu,mau)
def inkq(t,m):
    if tu==0: print(tu,"/",mau,"co the rut gon thanh 0",sep="")
    else:
        print (tu,"/",mau," co the rut gon thanh ",t,"/",m,sep="")
inkq(t,m)