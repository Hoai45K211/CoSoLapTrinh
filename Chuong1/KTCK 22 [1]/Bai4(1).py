#Hiện nay, với sự bùng nổ của công nghệ thông tin, 
# mỗi cá nhân đều có cho mình một số tài khoản 
# (tài khoản facebook, tài khoản e-mail, 
# tài khoản twitter…). Các tài khoản này đều cần 
# được bảo vệ bằng các mật khẩu. Một vấn đề quan 
# trọng là cần chọn được các mật khẩu “an toàn” 
# để tránh bị đánh cắp tài khoản.

#Giả sử mỗi mật khẩu là một chuỗi ký tự khác rỗng 
# chỉ gồm các chữ cái la-tinh in hoa (A…Z), 
# in thường (a…z) và chữ số (0..9). 
# Ta đánh giá độ “an toàn” của mật khẩu bởi
# hai tiêu chí:

#Độ dài (số ký tự): là một số nguyên trong phạm vi
# từ 0..5: Nếu mật khẩu có độ dài là m thì độ an toàn là:
#min(5,max(m-5),0)
#Loại ký tự(hoa, thường, số):
#Nếu chỉ có 1 loại ký tự: 1
#Có đúng 2 loại ký tự: 2
#Có đủ 3 loại ký tự: 5
#Độ an toàn của mật khẩu là tổng của hai tiêu chí trên.

#Ví dụ: mật khẩu làAbcd123456có độ an toàn là: 
#5 (độ dài) +5 (loại ký tự) = 10

#Bạn được cho một danh sách các mật khẩu,
# hãy viết chương trình để đánh giá “độ an toàn”
# của các mật khẩu đó.

#Dữ liệu vào:
#Dòng đầu chứa số nguyên dương n là số mật khẩu cần
#đánh giá
#n dòng tiếp theo, mỗi dòng chứa 1 mật khẩu là xâu ký
#tự khác rỗng, chỉ chứa các ký tự la-tinh in hoa (A...Z),
#in thường (a..z) và chữ số (0..9), độ dài không quá 15 kt

#giới hạn: 1<=n<=100

#Dữ liệu ra: Ghi trên một dòng n số nguyên là độ an 
# toàn của n mật khẩu (theo đúng thứ tự),
# hai số liên tiếp ghi cách nhau một dấu cách.

#Ví dụ
#Input 
#4
#Password
#security
#A1234
#Abcd123456

#Output 
#5 4 2 10

def tinh_do_an_toan(mat_khau):  #tính toán độ an toàn của mật khẩu dựa trên độ dài và loại ký tự.
    do_dai = len(mat_khau)  # biến do_dai để lưu độ dài của mật khẩu
    loai_ky_tu = set()  #loai_ky_tu để lưu loại ký tự xuất hiện trong mật khẩu
    
    for ky_tu in mat_khau:  #uyệt qua từng ký tự trong mật khẩu và kiểm tra xem ký tự đó thuộc loại nào
        if ky_tu.isupper():
            loai_ky_tu.add("hoa")
        elif ky_tu.islower():
            loai_ky_tu.add("thuong")
        elif ky_tu.isdigit():
            loai_ky_tu.add("so")
    
    do_an_toan_do_dai = min(5, max(do_dai - 5, 0))
    do_an_toan_loai_ky_tu = 1 if len(loai_ky_tu) == 1 else 2 if len(loai_ky_tu) == 2 else 5
    
    return do_an_toan_do_dai + do_an_toan_loai_ky_tu

n = int(input())
mat_khaus = []
for _ in range(n):
    mat_khau = input().strip()
    mat_khaus.append(mat_khau)

do_an_toans = [tinh_do_an_toan(mat_khau) for mat_khau in mat_khaus]
print(*do_an_toans)