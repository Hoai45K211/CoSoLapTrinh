#Viết chương trình nhập vào 3 số a, b và c; cho biết số lớn nhất trong 3 số.
#Yêu cầu xây dựng các hàm sau:
#- Hàm nhap()thực hiện việc nhập vào 3 số nguyên a,b và c;
#- Hàm max3(a,b,c) thực hiện việc tìm và trả về qua tên hàm số lớn nhất trong 3 số a,b, c;
#- Hàm inkq(kq) thực hiện in lên màn hình kết quả số lớn nhất theo mẫu sau.

def nhap():
    print("Nhap 3 so nguyen:")
    a = int(input("a="))
    b = int(input("b="))
    c = int(input("c="))
    return a,b,c

def max(a,b,c):
    max=b
    if max<a:
        max=a
    if max<c:
        max=c
        return max
    
def inkq(kq):
    print("So lon nhat la:",kq)

a,b,c=nhap()
kq=max(a,b,c)
inkq(kq)