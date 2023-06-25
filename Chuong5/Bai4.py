#Nhập từ bàn phím 2 số nguyên x, k;
#- Nhập một số nguyên n và n số nguyên lưu vào list L;
#- Xây dựng các hàm sau, thực hiện gọi hàm để trở thành 
# các chương trình hoàn chỉnh. 
#Hàm count(L) trả về số lượng phần tử trong List L;


def Nhap():
    x=int(input("x="))
    k=int(input("k="))
    n=int(input("n="))
    L=[]
    for i in range(n):
        z=int(input())
        L=L + [z]
    return x,k,L

def count(L):
    dem=0
    for x in L:
        dem=dem+1
    return dem
       
x,k,L=Nhap()
soluong=count(L)
print(soluong)