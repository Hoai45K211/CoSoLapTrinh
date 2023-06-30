#Đoạn code yêu cầu người dùng nhập vào một chuỗi.

#Nếu độ dài của chuỗi lớn hơn hoặc bằng 2, nó sẽ in ra 
# các ký tự đầu tiên, ký tự thứ hai, ký tự thứ hai từ cuối 
# và ký tự cuối cùng của chuỗi theo thứ tự.

#Nếu độ dài của chuỗi nhỏ hơn 2, không có hành động nào 
# được thực hiện.

#Ví dụ:
#Nếu người dùng nhập chuỗi n1 = "Hello, World!", 
# kết quả sẽ là "He!".

n1=str(input())
n2=[]
if len(n1)>=2:
    n2 = n2 + [n1[0]] + [n1[1]] + [n1[-2]] + [n1[-1]]
    for i in n2:
        print(i,end="")
else:
    None
    
#n1=str(input()): 
# Lấy đầu vào từ người dùng thông qua 
# hàm input() và chuyển đổi nó thành một chuỗi bằng cách 
# sử dụng hàm str(). Kết quả được gán cho biến n1

#n2=[]:
# Khởi tạo một danh sách rỗng n2.

#if len(n1)>=2::
# Kiểm tra xem độ dài của chuỗi n1 có lớn hơn 
# hoặc bằng 2 không. Nếu điều kiện trên đúng, tiếp tục thực 
# hiện các tác vụ bên trong khối if. Ngược lại, không làm gì 
# và qua bước kế tiếp.

#n2 = n2 + [n1[0]] + [n1[1]] + [n1[-2]] + [n1[-1]]: 
# Tạo một danh sách n2 mới bằng cách ghép các phần tử sau:
# Phần tử đầu tiên của n1 (n1[0]).
# Phần tử thứ hai của n1 (n1[1]).
# Phần tử thứ hai từ cuối của n1 (n1[-2]).
# Phần tử cuối cùng của n1 (n1[-1]).

#for i in n2: print(i,end=""):
# Duyệt qua từng phần tử i 
# trong danh sách n2 và in chúng ra màn hình, không xuống dòng. 
# Đoạn code này tạo ra một chuỗi được hiển thị liên tiếp, 
# mỗi phần tử trong n2 là một ký tự.