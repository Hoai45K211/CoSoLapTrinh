#Nhập từ bàn phím 2 số nguyên x, k;
#- Nhập một số nguyên n và n số nguyên lưu vào list L;
#- Xây dựng các hàm sau, thực hiện gọi hàm để trở thành 
# các chương trình hoàn chỉnh. 
#Bài 2. Hàm search(L, x) tìm x trong List L, nếu tìm thấy 
# thì trả về index của x trong L, còn lại trả về None;


def Nhap():
    x=int(input("x="))
    k=int(input("k="))
    n=int(input("n="))
    L=[]
    for i in range(n):
        z=int(input())
        L=L + [z]
    return x,k,L

def search(L,x):
    for i in range (len(L)):
        if L[i]==x:
            return i
    return None 
        
x,k,L=Nhap()
pos=search(L,x)
print("Ket qua tim kiem:",pos)