#Đoạn code yêu cầu người dùng nhập một chuỗi s.
#Sau đó, chương trình tìm và trích xuất các chuỗi con 
# liên tiếp chứa các chữ

#Input: "a1b2c3d4"
# Output: "1234"
# Giải thích: Chuỗi nhập vào là "a1b2c3d4". 
# Trong chuỗi này, ta có các chuỗi con liên tiếp chứa 
# các chữ số là "1", "2", "3", "4". Chương trình sẽ 
# trích xuất các chuỗi con này và ghép lại thành 
# chuỗi mật khẩu "1234" và trả về kết quả này.

def get_password(s):
    password =''
    i = 0
    while i <len(s):
        if s[i].isdigit():
            j=i+1
            while j<len(s) and s[j].isdigit():
                j+=1
                password += str(int(s[i:j]))
                i=j
        else:
            i+=1
            return password
    s = input()
print(get_password())

#Định nghĩa hàm get_password(s): Hàm này nhận đầu vào là 
# một chuỗi s và sẽ trả về một chuỗi mật khẩu.

#Khởi tạo biến password với giá trị rỗng để lưu trữ chuỗi
# mật khẩu.

#Khởi tạo biến i với giá trị ban đầu là 0 để duyệt qua các 
# ký tự trong chuỗi s.

#Bắt đầu vòng lặp while để duyệt qua từng ký tự trong chuỗi s.

#Trong vòng lặp, kiểm tra nếu ký tự s[i] là một chữ số bằng cách 
# sử dụng phương thức isdigit().

#Nếu s[i] là một chữ số, tiến hành tìm chuỗi các chữ số liên 
# tiếp sau s[i].

#Khởi tạo biến j với giá trị i + 1.

#Bắt đầu vòng lặp while để tìm chuỗi các chữ số liên tiếp 
# sau s[i].

#Trong vòng lặp, kiểm tra nếu j chưa vượt qua độ dài chuỗi s 
# và ký tự s[j] là một chữ số.

#Nếu điều kiện thỏa mãn, tăng giá trị của j lên 1 để tiếp tục 
# tìm chuỗi chữ số.

#Sau khi tìm được chuỗi chữ số, chuyển đổi nó thành một số nguyên 
# bằng cách sử dụng int(s[i:j]), sau đó chuyển đổi số nguyên
# thành chuỗi và thêm vào biến password.

#Cập nhật giá trị của i thành j để tiếp tục duyệt các ký tự 
# tiếp theo trong chuỗi s.

#Nếu ký tự s[i] không phải là chữ số, tăng giá trị của i lên 1
# để chuyển sang ký tự kế tiếp trong chuỗi s.

#Cuối cùng, trả về giá trị của biến password là chuỗi mật khẩu.

#Trong chương trình chính, yêu cầu người dùng nhập một chuỗi s 
# từ bàn phím.

#Gọi hàm get_password(s) với đối số là chuỗi s vừa nhập và
# in kết quả ra màn hình.

