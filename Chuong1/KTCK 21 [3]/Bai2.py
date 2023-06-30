#Viết chương trình để loại bỏ các phẩn tử trong một danh
# sách tại các vị trí có index 1, 3 và 4 cho trước

#INPUT: nhập vào một dãy các từ , mỗi từ cách nhau đúng 1
#ký tự trắng
#OUTPUT: in lên màn hình một danh sách mới đã được xóa đi
#các từ ở vị trí index cho trên

#INPUT: 
# Red Green White Black Pink Yello
# OUTPUT:
# ['Red','White','Yello']

#INPUT:
#An Binh Nam
#OUTPUT:
#['An','Nam']

danh_sach = input().split()

vi_tri_loai_bo = [1, 3, 4]  # Các vị trí index cần loại bỏ

danh_sach_moi = [danh_sach[i] for i in range(len(danh_sach)) if i not in vi_tri_loai_bo]

print(danh_sach_moi)