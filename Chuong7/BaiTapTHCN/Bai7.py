#Viết chương trình:
#- Nhập vào một chuỗi ký tự chứa họ tên và email;
#- Chương trình thực hiện tách email từ chuỗi trên và in 
# kết quả lên màn hình;
#- Biết rằng dữ liệu nhập vào có email hoặc không có email.

#Ví dụ:
#Ho ten: Nguyen Van An, Email: vanan@gmail.com
#Ho ten: Le Ngoc Binh, Email:
#Ho ten: Pham Anh Ngoc, Email: anhngoc@gmail.com

#TEST1:
#Input: Ho ten: Nguyen Van An, Email: vanan@gmail.com
#Output: vanan@gmail.com
#TEST2:
#Input: Ho ten: Le Ngoc Binh, Email:
#Output

n=input()
n=n.split()
if n[-1]!='Email:': #if kiểm tra xem phần tử cuối cùng của danh sách n có giá trị khác 'Email:' hay không
    print(n[-1])    # in ra phần tử cuối cùng
else:               #chuỗi kết thúc bằng 'Email:' 
    print('')       #thì in ra một chuỗi rỗng