L=[1,2,3,4,5,5,6,5,7,5]
# Xoa tat ca cac phan tu co gia tri bang x
# x duoc nhap tu ban phim
# List sau khi xoa len man hinh
x=int(input("x="))
while x in L:
    L.remove(x)
print(L)