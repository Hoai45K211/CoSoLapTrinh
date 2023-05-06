#Viết hàm nhận vào hai số nguyên dương làm tử số và
#mẫu số của một phân số là hai tham số duy nhất của nó. Phần thân của hàm
#nên giảm phân số xuống các số hạng thấp nhất và sau đó trả về cả tử số và
#mẫu số của phân số rút gọn là kết quả của nó. Ví dụ, nếu các tham số
#được truyền cho hàm là 6 và 63 thì hàm sẽ trả về 2 và 21. Bao gồm
#một chương trình chính cho phép người dùng nhập tử số và mẫu số. Sau đó
#chương trình của bạn sẽ hiển thị phân số rút gọn.
#Gợi ý: Trong bài tập 75, bạn đã viết một chương trình tính ước chung lớn nhất
#ước của hai số nguyên dương. Bạn có thể thấy mã đó hữu ích khi hoàn thành
#bài tập này.


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