#5.3. Nhập từ bàn phím một số nguyên n (n>0), 
# và n số nguyên lưu trữ vào một List.
#In lên màn hình:
#- Số lượng các số nguyên DƯƠNG
#- Trung bình cộng của các số nguyên chẵn được lưu trữ trong
#List trên.

#n=5
#6
#-2
#-1
#2
#7
#SND=3
#TBC=2.0


a=[]
x=0
SND=0
TBC=0
c=0
n=int(input("n="))
for i in range(n):
    b=int(input())
    a.append(b)
for i in range(len(a)):
    if a[i]>=0:
        SND+=1
    if a[i]%2==0:
        x=x+a[i]
        c+=1
if  c==0:
    TBC=0
else:
    TBC=x/c
print("SND=",SND,sep="")
print("TBC=",TBC,sep="")


#Tạo một danh sách rỗng a: a = [].

#Khởi tạo các biến x, SND, TBC, và c với giá trị ban đầu là 0.

#Người dùng được yêu cầu nhập vào một số nguyên n thông qua 
# hàm input("n="). Giá trị n được chuyển đổi thành kiểu dữ 
# liệu nguyên bằng cách sử dụng hàm int().

#Sử dụng một vòng lặp for để thực hiện việc nhập n số nguyên 
# từ người dùng và thêm chúng vào danh sách a. Trong mỗi lần 
# lặp, người dùng được yêu cầu nhập một số nguyên b, sau đó 
# số b được thêm vào danh sách a bằng cách sử dụng phép gắn 
# (a.append(b)).

#Sử dụng một vòng lặp for khác để duyệt qua từng phần tử 
# trong danh sách a:
#Nếu phần tử là số không âm (a[i] >= 0), biến SND được 
# tăng lên 1.
#Nếu phần tử là số chẵn (a[i] % 2 == 0), giá trị của phần 
# tử được thêm vào biến x, và biến c được tăng lên 1.

#Kiểm tra giá trị của biến c:
#Nếu c bằng 0, tức là không có số chẵn trong danh sách a, 
# giá trị của biến TBC được đặt là 0.
#Ngược lại, tức là có ít nhất một số chẵn trong danh sách a, 
# giá trị của biến TBC được tính bằng tổng của các số chẵn 
# trong danh sách a chia cho số lượng các số chẵn (x / c).

#In giá trị của biến SND và TBC ra màn hình, cách nhau bởi 
# dấu '='.