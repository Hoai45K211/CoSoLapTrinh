#Đoạn code yêu cầu người dùng nhập vào hai chuỗi từ bàn phím, 
# và mỗi chuỗi được tách thành một danh sách các từ, sử dụng hàm split().

#Chuỗi đầu tiên nhập vào được gán cho biến st1, 
# và chuỗi thứ hai nhập vào được gán cho biến st2.

#Khởi tạo một biến đếm dem với giá trị ban đầu là 0.

#Sử dụng vòng lặp for để lặp qua từng phần tử i trong danh sách st1.

#Trong vòng lặp, kiểm tra xem phần tử i có tồn tại 
# trong danh sách st2 không, sử dụng câu lệnh if i in st2.

#Nếu phần tử i tồn tại trong st2, tăng biến đếm dem lên 1.

#Sau khi vòng lặp kết thúc, kiểm tra xem giá trị của 
# biến đếm dem có bằng độ dài của danh sách st1 hay không.

#Nếu dem bằng độ dài của st1, tức là tất cả các từ 
# trong st1 đều xuất hiện ít nhất một lần trong st2.
#Trường hợp này, in ra màn hình chuỗi "True".

#Ngược lại, nếu dem khác với độ dài của st1, 
# tức là có ít nhất một từ trong st1 không xuất hiện trong st2.
#Trường hợp này, in ra màn hình chuỗi "False".

#Ví dụ:
#Nếu người dùng nhập vào st1 = "apple banana mango" 
# và st2 = "mango banana apple", kết quả sẽ là "True".


st1=input().split()
st2=input().split()
dem=0
for i in st1:
    if i in st2:
        dem+=1
if dem == len(st1):
    print("True")
else:
    print("False")
    
    
#st1=input().split(): 
# Lấy đầu vào từ người dùng thông qua hàm input(). 
# Hàm split() được gọi để tách chuỗi đầu vào thành một 
# danh sách các từ và gán cho biến st1. Chuỗi đầu vào được 
# tách dựa trên khoảng trắng (mặc định).

#st2=input().split(): 
# Lấy đầu vào thứ hai từ người dùng 
# thông qua hàm input() tương tự như trên. Kết quả được 
# gán cho biến st2.

#dem=0: Khởi tạo biến đếm dem với giá trị ban đầu là 0.

#for i in st1:
#Bắt đầu vòng lặp for để lặp qua từng phần tử i trong 
# danh sách st1.
#if i in st2:: Kiểm tra xem phần tử i có tồn tại trong 
# danh sách st2 không.
#Nếu phần tử i tồn tại trong st2, tăng biến dem lên 1.

#if dem == len(st1):: 
# Kiểm tra xem giá trị của biến đếm 
# dem có bằng độ dài của danh sách st1 không. Nếu số lần 
# xuất hiện của các phần tử trong st1 trong st2 bằng 
# độ dài của st1, có nghĩa là tất cả các phần tử trong st1 
# đều xuất hiện ít nhất một lần trong st2.

#Nếu điều kiện trên đúng (dem == len(st1)), in ra màn hình 
# chuỗi "True". Ngược lại, in ra chuỗi "False". Kết quả này
# cho biết liệu tất cả các từ trong danh sách st1 có xuất
# hiện ít nhất một lần trong danh sách st2 hay không.