#Chương trình nhập vào một số nguyên là tuổi một sinh viên,
# chương trình kiểm tra và yêu cầu nhập lại nếu dữ liệu
# không phải là số.

while True:
    print("Nhap so tuoi:")
    tuoi = input()
    if tuoi.isdecimal():
        break
    print("Vui lòng nhập lại số tuổi:")