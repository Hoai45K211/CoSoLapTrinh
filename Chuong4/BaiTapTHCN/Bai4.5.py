#Viết chương trình đếm số nguyên tố:
#Yêu cầu xây dựng các hàm sau:
#- Hàm LaSoNguyenTo(x): trả về True nếu x là số nguyên tố, còn lại trả về False;
#- Hàm SoHopLe(x): trả về True nếu x<=1, còn lại trả về False;
#- Hàm NhapVaDem(): thực hiện nhập liên tục các số nguyên cho đến khi số được nhập vào là
#số <=1 thì dừng. Sử dụng hàm SoHopLe(x) ở trên để kiểm tra một số x có <=1 hay không. Sử
#dụng hàm LaSoNguyenTo(x) ở trên để kiểm tra và đếm có bao nhiêu số nguyên đã được
#nhập là số nguyên tố. Kết quả được trả về qua tên hàm.
#- Hàm InKQ(kq): in lên màn hình kết quả theo mẫu sau.


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