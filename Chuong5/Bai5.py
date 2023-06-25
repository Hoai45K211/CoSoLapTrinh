#Nhập từ bàn phím 2 số nguyên x, k;
#- Nhập một số nguyên n và n số nguyên lưu vào list L;
#- Xây dựng các hàm sau, thực hiện gọi hàm để trở thành 
# các chương trình hoàn chỉnh. 
#Hàm replace(L, x, y) tìm tất cả các phần tử có giá trị 
# bằng x trong List L và thay thế bằng y;


def Nhap():
    x=int(input("x="))
    k=int(input("k="))
    n=int(input("n="))
    L=[]
    for i in range(n):
        z=int(input())
        L=L + [z]
    return x,k,L

def replace(L,x,y):
    for i in range (len(L)):
        if L[i]==x:
            L[i]=y
    return L

x,k,L=Nhap()
y=int(input("y="))
L=replace(L,x,y)
print(L)