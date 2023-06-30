#Cho một chuỗi ký tự, viết chương trình để tính tổng các 
# chữ số có 1 chữ số trong chuỗi. Nếu dấu trừ đứng trước
# 1 số thì số đó vẫn tính là số âm

#INPUT: nhập vào một chuỗi ký tự
#OUTPUT: in lên màn hình tổng các số có 1 chữ số xuất hiện
#trong chuỗi

#IN:
# 123abcd45
#OUT:
# 15

#IN:
# 1-2-3abcd45
#OUT:
# 5


def tinh_tong_chu_so(chuoi):
    tong = 0
    for ky_tu in chuoi:
        if ky_tu.isnumeric() and int(ky_tu) < 10:
            tong += int(ky_tu)
    return tong

chuoi = input()
tong_chu_so = tinh_tong_chu_so(chuoi)
print(tong_chu_so)
