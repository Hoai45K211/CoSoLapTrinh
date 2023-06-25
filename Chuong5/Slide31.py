#Viết chương trình nhập từ bàn phím 10 số nguyên, 
# lưu trữ vào 1 List; và nhập một số nguyên x. 
# Yêu cầu sử dụng hàm.

#a. Tìm tất cả các phần tử có giá trị bằng 5 và thay bằng x.
# In kết quả lên màn hình;

# b. Xóa tất cả các phần tử có giá trị bằng x xuất hiện 
# trong tập hợp trên. In kết quả lên màn hình.


def Nhap():
    L=[]
    print("Moi nhap 10 so nguyen:")
    for i in range(10):
        L=L+[int(input())]
       
    x=int(input("Nhap so nguyen x="))
    return L,x

def InKQ(L):
    for x in L:
        print(x,end=", ")
       
def CauA(L,x):
    # Tim va thay the
    for i in range(len(L)):
        if L[i]==5:
            L[i]=x
    InKQ(L)
   
def CauB(L,x):
    i=0 #So chi muc
    while i<len(L):
        if L[i]==x:
            del(L[i])
        else:
            i+=1
           
    print("\nSau khi xoa x khoi tap L:")
    InKQ(L)
   
L,x=Nhap()
CauA(L,x)
CauB(L,x)
