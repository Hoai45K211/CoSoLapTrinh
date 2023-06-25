#Chương trình nhập vào mật khẩu là một chuỗi ký tự chỉ bao gồm
# chữ cái và chữ số, chương trình kiểm tra và yêu cầu nhập lại
# cho đến khi hợp lệ.

while True:
    print("Hay nhap mat khau:")
    matkhau=input()
    if matkhau.isalnum():
        break
    print("Mat khau chi co so va chu")