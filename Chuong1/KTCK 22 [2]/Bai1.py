#Đoạn code yêu cầu người dùng nhập vào một số nguyên n.
#Sau đó, nó yêu cầu người dùng nhập vào n giá trị.
#Chương trình đếm và tính tổng các giá trị số đã được nhập vào.
#Nếu không có giá trị số nào được nhập, in ra màn hình chuỗi "0".
#Nếu có giá trị số được nhập, tính trung bình của các giá trị số 
# và in ra màn hình với định dạng làm tròn đến 2 chữ số thập phân.
#Ví dụ:
#Nếu người dùng nhập số n = 4 và nhập các giá trị 
# 5, 8, "hello", 10, kết quả sẽ là 7.67.

n=int(input())
sum=0
count= 0
for i in range (1,n+1):
    value = input()
    if value.isdigit():
        count+=1
if count ==0:
    print('0')
else:
    total = sum/count
    print(round(total,2))
    

#n=int(input()): 
# Lấy đầu vào từ người dùng thông qua 
# hàm input() và chuyển đổi nó thành một số nguyên 
# bằng cách sử dụng hàm int(). Kết quả được gán cho biến n.

#sum=0 và count=0: 
# Khởi tạo biến sum với giá trị ban đầu 
# là 0 và biến count đếm số lượng giá trị số được nhập vào.

#for i in range(1,n+1):: 
# Bắt đầu vòng lặp for từ 1 đến n 
# (bao gồm n).
# value = input(): 
# Lấy đầu vào từ người dùng thông qua hàm input() và gán cho biến value.
# if value.isdigit():: Kiểm tra xem value có phải là một chuỗi số không.
# Nếu value là một chuỗi số, tăng biến count lên 1.

#if count == 0:: 
# Kiểm tra xem giá trị của biến count 
# có bằng 0 không.
# Nếu count bằng 0, tức là không có giá trị số nào 
# được nhập vào.
# In ra màn hình chuỗi "0".

#else::
# Nếu count khác 0, tức là có ít nhất một giá trị số 
# được nhập vào.
# Tính tổng các giá trị số đã nhập vào và gán cho biến total.
# Tính trung bình bằng cách chia tổng cho count.
# In giá trị trung bình total làm tròn đến 2 chữ số thập phân
# và hiển thị ra màn hình.
