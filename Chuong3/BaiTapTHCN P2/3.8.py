#Nhập vào một ký tự bất kỳ và một số nguyên n (1<=n<=20), 
#chương trình in lên màn hình trang trí 
#theo cấu trúc bên dưới.
#Ví dụ: ký tự nhập vào là dấu *, số nguyên n = 6. 
# Kết quả trên màn hình sẽ như sau:
#(Mỗi dấu * cách nhau 1 dấu cách)

#*
#6
#*
#* *
#* * *
#* * * *
#* * * * *
#* * * * * 


y=str(input(""))
n=int(input(""))
i=1 #khởi tạo đếm số lượng ký tự trên mỗi hàng
while i<=n and 1<=n<=20:  #lặp lại cho đến khi giá trị của biến i vượt quá giá trị của biến n hoặc giá trị của biến n không nằm trong khoảng từ 1 đến 20
    j=1 #khởi tạo đếm số lượng ký tự trong mỗi hàng của tam giác
    while j<=i:      #lặp lại cho đến khi giá trị của biến j vượt quá giá trị của biến i
        print(y,end=" ",sep="")  #đặt end=" " để thêm một khoảng trắng giữa các ký tự in ra. Đặt sep="" để không thêm bất kỳ ký tự phân tách nào
        j=j+1   #Tăng giá trị của biến j lên 1 sau mỗi lần lặp vòng lặp while thứ hai
    print("")   #in ra một dòng trống để xuống dòng tiếp theo
    i=i+1   #Tăng giá trị của biến i lên 1 sau mỗi lần lặp vòng lặp while đầu tiên
    
    
#Cach khac (tu lam)
y=str(input(""))
n=int(input(""))

for i in range (1,n+1,1):
    print(i * "* ")