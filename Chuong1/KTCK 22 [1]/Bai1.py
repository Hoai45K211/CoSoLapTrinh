#Đoạn code yêu cầu người dùng nhập vào một dãy số nguyên, 
# các số cách nhau bằng khoảng trắng.

# Sau khi nhập dãy số, nó sẽ chuyển đổi chuỗi đó thành 
# một danh sách các số nguyên bằng cách sử dụng hàm map() và split().

# Tiếp theo, danh sách các số nguyên được chuyển thành 
# một danh sách mới n2 chỉ chứa các phần tử duy nhất 
# từ danh sách ban đầu. Các phần tử trùng lặp trong danh sách n1 được loại bỏ.

# Kết quả của danh sách n2 được in ra màn hình.

#Tóm lại, đoạn code này nhận dữ liệu đầu vào từ 
# người dùng dưới dạng dãy số nguyên, loại bỏ 
# các phần tử trùng lặp và in ra các số duy nhất trong dãy đó.

#Ví dụ:
# Nếu người dùng nhập chuỗi "1 2 3 2 4 5 3", 
# đầu ra sẽ là [1, 2, 3, 4, 5].


n1=list(map(int,input().split()))
n2=list(dict.fromkeys(n1))
print(n2)


#n1=list(map(int,input().split())): 
# Đầu tiên, nó sử dụng hàm input() để nhận một chuỗi đầu 
# vào từ người dùng. Hàm input() trả về một chuỗi chứa các 
# giá trị được nhập vào từ bàn phím. Sau đó, hàm split() 
# được gọi để tách chuỗi thành một danh sách các phần tử 
# dựa trên khoảng trắng (mặc định). Hàm map() được áp dụng 
# để chuyển đổi mỗi phần tử trong danh sách thành một 
# số nguyên bằng cách sử dụng hàm int(). Kết quả là một
# danh sách các số nguyên và được gán cho biến n1.

#n2=list(dict.fromkeys(n1)): 
# Tiếp theo, danh sách n1 được truyền vào hàm dict.fromkeys()
# để tạo một từ điển với các khóa là các phần tử trong n1 
# và giá trị tương ứng là None. Sau đó, danh sách các 
# khóa từ từ điển này được chuyển đổi thành danh sách n2 
# bằng cách sử dụng hàm list(). Điều này loại bỏ các 
# phần tử trùng lặp từ danh sách n1 và giữ lại chỉ mục 
# đầu tiên của mỗi phần tử duy nhất.

#print(n2): Cuối cùng, danh sách n2 được in ra màn hình. 
# Đây là danh sách các phần tử duy nhất từ danh sách n1, 
# mà không có các phần tử trùng lặp.