#Viết chương trình nhập từ bàn phím 2 số nguyên a và b.
#- Yêu cầu kiểm tra tính đúng của dữ liệu khi nhập vào. 
# Nếu dữ liệu không hợp lệ thì yêu cầu nhập lại.
#- In lên màn hình kết quả của biểu thức (a+b).


while True:
    a=input()
    b=input()
    if a.isdecimal() and b.isdecimal() :
        tong=int(a)+int(b)
        print(tong)
        break
    print("Moi nhap lai:")
    
    
#Cach 2:
def NhapSo(tb):
    while True:
        a=input(tb)
        if a.isnumeric():
            return int(a)
        else:
            print("Khong hop le!")


a=NhapSo("a=")
b=NhapSo("b=")
print("a=",a,sep="")
print("b=",b,sep="")
