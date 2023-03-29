def Nhap():
    snn=int(input('SNN='))
    return snn
def inkq(snn):
    while True:
        if snn<0:
            snn= int(input('SNN='))
        else:
            break
    if snn==0:
        print("Thuong=500")
    elif 0<snn<=2:
        print("Thuong=300")
    elif 2<snn<=4:
        print("Thuong=150")
    else:
        print("Thuong=0")

snn=int(input("SNN="))
inkq(snn)