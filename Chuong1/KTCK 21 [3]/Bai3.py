#Viết chương trình để xóa tất cả các ký tự trắng trong một
#chuỗi đã cho

#INPUT: nhập vào 1 chuỗi ký tự
#OUTPUT: in lên màn hình chuỗi ký tự đã được xóa các khoảng
#trống

#INPUT:
# Py t ho n
#OUTPUT:
#Python


def xoa_ky_tu_trang(chuoi):
    return chuoi.replace(" ", "")  #(gt cũ, gt mới)

chuoi = input()
chuoi_da_xoa_ky_tu_trang = xoa_ky_tu_trang(chuoi)
print(chuoi_da_xoa_ky_tu_trang)