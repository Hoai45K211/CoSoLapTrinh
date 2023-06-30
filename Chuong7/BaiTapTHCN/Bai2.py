#Viết chương trình:
#- Cho phép nhập vào một chuỗi ký tự bất kỳ;
#- Chương trình thực hiện làm sạch chuỗi ký tự trên. 
# Biết rằng một chuỗi được gọi là “sạch” nếu: 
#o Không bắt đầu và kết thúc bằng các ký tự trắng;
#o Mỗi từ chỉ được cách nhau bằng đúng 1 ký tự trắng;
#o Chỉ được phép viết hoa chữ cái đầu tiên của chuỗi;
#o Trước các dấu câu (phẩy, chấm phẩy, hai chấm, chấm) không có ký tự trắng;
#- In nội dung chuỗi sau khi xử lý lên màn hình.

#TEST:
#Input:      Xin Chào , tôi là sInh viêN 
#Output: Xin chào, tôi là sinh viên


n=input()
n=n.strip()     #loại bỏ các khoảng trắng dư thừa ở đầu và cuối 
a=n[0].upper()+n[1:].lower()    #đổi ký tự đầu thành hoa và các ký tự sau thành in thường
a=a.split()     #chia a thành một danh sách các từ riêng biệt
n=''
for i in a:
    if i==',' or i==':' or i==';' or i=='.':
        n=n.strip()+i+' '
    else: 
        n=n+i+' '
print(n.strip())