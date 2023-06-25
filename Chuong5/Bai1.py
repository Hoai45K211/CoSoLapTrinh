#Nhập từ bàn phím 2 số nguyên x, k;
#- Nhập một số nguyên n và n số nguyên lưu vào list L;
#- Xây dựng các hàm sau, thực hiện gọi hàm để trở thành 
# các chương trình hoàn chỉnh. 
#Bài 1. Hàm add(L, x, k) thêm phần tử x vào List L tại 
# vị trí index k, nếu k lớn hơn số phần tử của L thì
# thêm x vào cuối L;


def Nhap():
    x=int(input("x="))
    k=int(input("k="))
    n=int(input("n="))
    L=[]
    for i in range(n):
        z=int(input())
        L=L + [z]
    return x,k,L


def add(L,x,k):
    L=L[:k] + [x] + L[k:]
    return L


x,k,L=Nhap()
L=add(L,x,k)
print(L)