#Hiện nay, với sự bùng nổ của công nghệ thông tin, 
# mỗi cá nhân đều có cho mình một số tài khoản 
# (tài khoản facebook, tài khoản e-mail, tài khoản twitter…).
# Các tài khoản này đều cần được bảo vệ bằng các mật khẩu.
# Một vấn đề quan trọng là cần có biện pháp bảo vệ các 
# mật khẩu đó “an toàn” để tránh bị đánh cắp tài khoản.

#Tèo luôn chọn cho mình những mật khẩu gồm một số chữ cái
# la-tinh đứng đầu không quá 10 chữ cái) và đem ghép vào
# cuối một số nguyên dương trong hệ thập phân (không quá 
# 6 chữ số). Ví dụ: `Abcd12`. Sau đó Tèo mã hóa mật khẩu 
# bằng cách tách phần số ở cuối, giữ lại phần chữ cái ở 
# đầu và đem chèn vào giữa các chữ cái đó (có thể cả ở 
# đầu và ở cuối) một số chữ số từ 0 đến 9 sao cho tổng 
# các chữ số được chèn đúng bằng số ở cuối của mật khẩu.
# Ví dụ: `A1b23c4d2` là một cách mã hóa của mật khẩu 
# `Abcd12` (các chữ số được dùng để chèn là 1+2+3+4+2=12).
# 
# Bạn hãy giúp Tèo viết một chương trình giải mã mật khẩu
# nhé?

#Dữ liệu vào
# Một dòng duy nhất chứa xâu ký tự mật khẩu đã mã hóa chỉ
# gồm các chữ cái la-tinh và chữ số.
# Giới hạn:
# Độ dài xâu mã hóa không quá 10^5 ký tự trong đó có chứa
# ít nhất một chữ cái la-tinh và ít nhất một chữ số khác0.

#Dữ liệu ra
# Ghi ra một dòng duy nhất là mật khẩu giải mã được.

#Ví dụ
# Input 
# A1b23c4d2
# Output 
# Abcd12

def giai_ma_mat_khau(mat_khau_ma_hoa):  #thực hiện quá trình giải mã mật khẩu.
    chu_cai = ""    #chu_cai để lưu các chữ cái
    so = 0  #so để tính tổng các chữ số.

    for ky_tu in mat_khau_ma_hoa:   #Duyệt qua từng ký tự trong mật khẩu đã mã hóa và kiểm tra xem ký tự đó thuộc loại chữ cái hay chữ số 
        if ky_tu.isalpha():
            chu_cai += ky_tu    #Nếu là chữ cái, chúng ta thêm ký tự đó vào chu_cai
        elif ky_tu.isdigit():
            so += int(ky_tu)    # nếu là chữ số, chúng ta cộng giá trị số đó vào so.

    so_cuoi = str(so)   # chuyển giá trị của so thành chuỗi so_cuoi.
    mat_khau_giai_ma = chu_cai + so_cuoi    #ết hợp chu_cai và so_cuoi để tạo mật khẩu đã giải mã mat_khau_giai_ma.

    return mat_khau_giai_ma

mat_khau_ma_hoa = input().strip()
mat_khau_giai_ma = giai_ma_mat_khau(mat_khau_ma_hoa)
print(mat_khau_giai_ma)