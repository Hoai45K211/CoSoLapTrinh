def LaSoNguyenTo(x):
    for i in range(2,x):
        if x%i==0:
            return False
    return True

def SoHopLe(x):
    if x<=1:
        return True
    else:
        return False
    
def NhapVaDem():
    print("Nhap day so:")
    d=0
    while True:
        y=int(input(""))
        if y<=1:
            break
        elif LaSoNguyenTo(y):
            d=d+1
    return d

def inkq(kq):
    print("Co",kq,"so nguyen to")

kq=NhapVaDem()
inkq(kq)


#Cach 2
def LaSoNguyenTo(x):
    if x <= 1:
        return False
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False
    return True

def SoHopLe(x):
    return x <= 1

def NhapVaDem():
    count = 0
    while True:
        x = int(input("Nhap mot so nguyen: "))
        if SoHopLe(x):
            break
        if LaSoNguyenTo(x):
            count += 1
    return count

def InKQ(kq):
    print("So luong cac so nguyen to da nhap la:", kq)

kq = NhapVaDem()
InKQ(kq)