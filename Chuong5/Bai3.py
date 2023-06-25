#Nhập từ bàn phím 2 số nguyên x, k;
#- Nhập một số nguyên n và n số nguyên lưu vào list L;
#- Xây dựng các hàm sau, thực hiện gọi hàm để trở thành 
# các chương trình hoàn chỉnh. 
#Hàm delete(L, x) xóa tất cả phần tử có giá trị bằng x 
# trong List L;


def Nhap():
    x=int(input("x="))
    k=int(input("k="))
    n=int(input("n="))
    L=[]
    for i in range(n):
        z=int(input())
        L=L + [z]
    return x,k,L

def delete(L,x):
    M=[]
    for z in L:
        if z!=x:
            M=M+[z]
    return M
   
x,k,L=Nhap()
M=delete(L,x)
print(M)