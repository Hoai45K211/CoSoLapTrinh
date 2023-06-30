#Đoạn code yêu cầu người dùng nhập vào một chuỗi từ bàn phím.

#Sau đó, nó tìm các ký tự trong chuỗi đó mà xuất hiện trùng lặp.

#Nếu có ký tự xuất hiện trùng lặp, in ra ký tự đầu tiên đó.

#Nếu không có ký tự nào xuất hiện trùng lặp, in ra chuỗi "None".

#Ví dụ:
#Nếu người dùng nhập chuỗi "abbccd", kết quả sẽ là "b".


A=[]
B=[]
n=input()
for i in n:
    if i not in A:
        A+=[i]
    else:
        B+=[i]
if B!=[]:
    kq=B[0]
    print(kq)
else:
    print("None")
    
    
#A=[] và B=[]: 
# Khởi tạo hai danh sách rỗng A và B.

#n=input(): 
# Lấy đầu vào từ người dùng thông qua hàm input() 
# và gán cho biến n.

#for i in n:
# Bắt đầu vòng lặp for để lặp qua từng ký tự i trong chuỗi n.
# if i not in A:: Kiểm tra xem ký tự i có tồn tại trong 
# danh sách A không.
# Nếu ký tự i không tồn tại trong A, thêm ký tự i vào 
# danh sách A bằng cách sử dụng phép cộng danh sách (A+=[i]).
# Ngược lại, nếu ký tự i đã tồn tại trong A, thêm ký tự i 
# vào danh sách B bằng cách sử dụng phép cộng danh sách (B+=[i]).

#if B!=[]:
# Kiểm tra xem danh sách B có rỗng không.
# Nếu danh sách B không rỗng, tức là đã có ít nhất 
# một ký tự xuất hiện trùng lặp trong chuỗi n.
# Gán ký tự đầu tiên trong danh sách B cho biến kq.
# In biến kq ra màn hình.

#else: print("None")
# Nếu danh sách B rỗng, tức là không có ký tự nào 
# trong chuỗi n xuất hiện trùng lặp.
# In chuỗi "None" ra màn hình.