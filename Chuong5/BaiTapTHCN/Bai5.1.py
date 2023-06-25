#5.1. Viết chương trình có sử dụng hàm thực hiện các 
# yêu cầu sau:
#- Hàm Input(): nhập một số nguyên n (n>0) và n số nguyên 
# lưu vào List L, và một số nguyên x;
#- Hàm FirstAndLast(L) trả về và in lên màn hình List mới 
# chỉ gồm phần tử đầu tiên và cuối cùng của L;
#- Hàm Search(L,x): xác định x có nằm trong L hay không. 
# Trả về True nếu tìm thấy, còn lại trả về False.


#n=4
#3
#5
#3
#7
#x=5
#[3, 7]
#True


def Input():
    L=[]
    n=int(input("n="))
    for i in range(1,n+1):
        z=int(input())
        L=L+[z]
    x=int(input("x="))
    return L,x
def FirstAndLast(L):
    L1=L.copy()
    del(L1[1:len(L1)-1])
    print(L1)
def Search(L,x):
    if x in L:
        return True
    return False

L,x=Input()
FirstAndLast(L)
check=Search(L,x)
print(check)