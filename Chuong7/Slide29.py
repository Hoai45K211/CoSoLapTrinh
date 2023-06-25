#Viết chương trình nhập vào họ tên của một sinh viên. 
# Kiểm tra tính hợp lệ của chuỗi nhập vào. Biết rằng họ tên 
# hợp lệ nếu tất cả được viết thường, chỉ viết hoa chữ 
# cái đầu của từ.

#Ví dụ 1:
#Ho ten: NGUYEN VAN AN
#Khong hop le!!!

#Ví dụ 2:
#Ho ten: Nguyen Van An
#Hop le!!!

#Tu giai:
while True:
    hoten=input("Ho ten: ")
    if hoten.istitle():
        print("Hop le!!!")
        break
    else: 
        print("Khong hop le") 
        
#Cach thay giai: 
def NhapHoTen():
    while True:
        hoten=input("Ho ten: ")
        if hoten.istitle():
            print("Hop le!!!")
            return hoten
        else:
            print("Khong hop le!!!")
           
hoten=NhapHoTen()
        
   