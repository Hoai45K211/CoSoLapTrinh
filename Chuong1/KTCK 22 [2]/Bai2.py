#Đoạn code yêu cầu người dùng nhập vào một chuỗi giá trị 
# từ bàn phím.

# Nếu giá trị nhập vào là chuỗi 'Q', chương trình dừng 
# và tính tổng các giá trị số nguyên dương đã được nhập.

# Giá trị nhập vào chỉ được tính vào tổng nếu nó là 
# một số nguyên dương.
# 
# Cuối cùng, in tổng các giá trị số nguyên dương ra màn hình.
# 
# Ví dụ:
# Nếu người dùng nhập các giá trị 5, 8, -3, 2, 'Q', 
# kết quả sẽ là 15 (tổng của các giá trị 5 và 8).


#Nhập một dãy số thực, phân tách nhau bởi phím enter
#Cho đến khi nhập chữ cái Q thì kết thúc
#Tính tổng các số nguyên dương


sum=0
while True:
    num = input()
    if num =='Q':
        break
    if float(num)>0 and int(float(num))==float(num):
        sum+=int(float(num))
       
print(sum)


#sum=0: 
# Khởi tạo biến sum với giá trị ban đầu là 0 để tính tổng.

#while True:: 
# Bắt đầu vòng lặp vô hạn bằng cách sử dụng 
# vòng lặp while True, tức là vòng lặp sẽ tiếp tục cho đến
# khi gặp câu lệnh break.

#num = input(): 
# Lấy đầu vào từ người dùng thông qua hàm input() 
# và gán cho biến num.

#if num == 'Q':: 
# Kiểm tra xem giá trị của num có bằng chuỗi 'Q' không.
# Nếu num bằng 'Q', tức là người dùng muốn kết thúc 
# và thoát khỏi vòng lặp.
# Gặp câu lệnh break để thoát khỏi vòng lặp.

#if float(num) > 0 and int(float(num)) == float(num):: 
# Kiểm tra xem giá trị của num có lớn hơn 0 và có phải là
# số nguyên không.
# Sử dụng float(num) để chuyển đổi giá trị num thành số thực.
# Kiểm tra xem số thực float(num) có lớn hơn 0 và 
# có phải là số nguyên không, bằng cách so sánh giá trị 
# số nguyên của float(num) với float(num).
# Nếu cả hai điều kiện đúng, tức là num là một số nguyên dương,
# thì thực hiện các lệnh bên trong khối if.
# Tăng biến sum lên giá trị của num 
# (sau khi được chuyển đổi thành số nguyên) bằng cách
# sử dụng phép cộng (sum += int(float(num))).

#print(sum): In giá trị của biến sum ra màn hình.