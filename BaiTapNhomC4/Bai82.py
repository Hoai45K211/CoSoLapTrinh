#Viết hàm lấy độ dài hai cạnh ngắn hơn của một tam giác vuông thành
#thông số của nó. Trả về cạnh huyền của tam giác, được tính bằng Pythagore
#định lý, là kết quả của hàm. Bao gồm một chương trình chính đọc độ dài của
#các cạnh ngắn hơn của một tam giác vuông từ người dùng, sử dụng chức năng của bạn để tính toán
#chiều dài của cạnh huyền và hiển thị kết quả.


def Nhap():
    km=float(input("km="))
    return km
def tinh(km):
    codinh=4
    them=0.25
    dv=140
    tien = codinh + them*(km*1000//dv)
    return tien
def InKQ(kq):
    print('The total fare ', kq, '$', sep = '')
km=Nhap()
kq = tinh(km)
InKQ(kq)

