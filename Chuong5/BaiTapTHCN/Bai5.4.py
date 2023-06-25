#5.4. Nhập từ bàn phím một số nguyên n (n>0) và n số nguyên 
# lưu vào List A:
#- Hãy đảo ngược giá trị của các phần tử trong List A và
# lưu vào List B. In giá trị các phần tử trong List B sau
# khi thực hiện đảo;
#- Sắp xếp và in lên màn hình List B sau khi được sắp xếp 
# tăng dần;

#n=5
#3
#1
#4
#2
#5
#[5, 2, 4, 1, 3]
#[1, 2, 3, 4, 5]


L=[]
n=int(input("n="))
for i in range(0,n):
    x=int(input())
    L=L+[x]
L.reverse()
print(L)
L.sort()
print(L)

#Sử dụng một vòng lặp for để thực hiện việc nhập n số nguyên
# từ người dùng và thêm chúng vào danh sách L. Trong mỗi lần
# lặp, người dùng được yêu cầu nhập một số nguyên x, sau đó 
# số x được thêm vào danh sách L bằng cách sử dụng phép cộng
# danh sách (L = L + [x]).

#Sử dụng phương thức reverse() của danh sách (L.reverse()) 
# để đảo ngược thứ tự các phần tử trong danh sách L.

#In danh sách L sau khi đảo ngược lên màn hình.

#Sử dụng phương thức sort() của danh sách (L.sort()) để 
# sắp xếp các phần tử trong danh sách L theo thứ tự tăng dần.

#In danh sách L sau khi sắp xếp lên màn hình.