def Nhap():
    km=float(input("km="))
    return km
def tinh(km):
    codinh=4
    them=0.25
    dv=140
    tien = codinh + them*(km*1000//dv)
    return tien
def InKQ(kq):
    print('The total fare ', kq, '$', sep = '')
km=Nhap()
kq = tinh(km)
InKQ(kq)

