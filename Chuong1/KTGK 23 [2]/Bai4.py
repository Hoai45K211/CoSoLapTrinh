#nhập một chuỗi n (số nguyên có từ 1 đến 4 chữ số), 
#sau đó tính tổng của hai chữ số cuối cùng của số nguyên tương ứng với chuỗi n

n = str(input())
if len(n)==1:
    print(0)
else:
    tong= (int(n) % 100) // 10 + (int(n) % 100) % 10
print(tong)


#Chuyển chuỗi n thành số nguyên int(n).
#Lấy phần dư của int(n) khi chia cho 100 (bằng toán tử %), để lấy được 2 chữ số cuối cùng của số nguyên tương ứng với chuỗi n.
#Lấy kết quả của bước trên và chia cho 10, sau đó lấy phần nguyên để lấy chữ số thứ hai.
#Lấy kết quả của bước trên và lấy phần dư khi chia cho 10, để lấy chữ số cuối cùng.
#Cộng hai chữ số vừa tìm được để tính tổng và lưu vào biến tong.