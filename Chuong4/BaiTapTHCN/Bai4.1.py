def nhap():                 #gọi hàm nhap
    n=int(input("n="))      #nhập giá trị n 
    return n                #giá trị n được trả về từ hàm nhap

def giaithua(n):            #họi hàm giaithua
    gt=1                     #biến đếm
    for i in range(1,n+1):   #dùng for để nhân các số từ 1 đến n lại với nhau
       gt=gt*i              #được cập nhật bằng cách nhân với giá trị i sau mỗi lần lặp
    return gt

def inkq(n,X):
    print(n,"!=",X,sep="")

n=nhap()                    #gọi hàm nhap() để lấy giá trị của n từ người dùng
X=giaithua(n)               #gọi hàm giaithua(n) để tính toán giai thừa của n
inkq(n,X)                   #gọi hàm inkq(n,X) để in kết quả tính toán ra màn hình


#Cach2
def nhap():
    n = int(input("n="))
    return n

def giaithua(n):
    if n == 0:
        return 1
    else:
        return n * giaithua(n-1)

def inkq(n, X):
    print(n,"!=",X,sep="")
    
n = nhap()          
X = giaithua(n)     
inkq(n, X)  