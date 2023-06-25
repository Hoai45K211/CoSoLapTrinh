#Nhập vào một chuỗi ký tự làm mật khẩu cho chương trình.
#Yêu cầu:
#-Mật khẩu có tối thiểu 8 ký tự.
#-Bao gồm: chữ cái, chữ số, chữ viết hoa và viết thường.
#Nếu chuỗi mật khẩu không hợp lệ thì yêu cầu nhập lại.

#Ví dụ:
#abc123 --> Không hợp lệ
#aaaaa111111 --> Không hợp lệ
#aaaaBBBBBB --> Không hợp lệ
#1111111111 --> Không hợp lệ
#AAAAA111111 --> Không hợp lệ
#aaaAA111111 --> Hợp lệ

while True:    
    str=input()
    if len(str)<8 or str.islower() or str.isupper() or str.isnumeric() or str.isalpha():
        print("Khong hop le!!!")
    else:
        print("Hop le!!!")
        break