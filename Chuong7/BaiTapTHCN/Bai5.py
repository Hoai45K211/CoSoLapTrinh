# Viết chương trình:
#- Nhập vào một chuỗi gồm các số nguyên, mỗi số cách nhau
# bởi một dấu cách; và một số nguyên X;
#- Chương trình thực hiện tìm X trong dãy số trên, in lên 
# màn hình thứ tự xuất hiện của X nếu có. Nếu không tìm thấy
# thì trả về 0;

#TEST1:
#Input: 1 30 44 12 15 24 93 100 24 52 15 34
#15
#Output: 5
#11
#TEST2:
#Input: 44 12 24 93 100 24 52
#15
#Output: 0

#Gợi ý:
#- Sử dụng hàm split() để tách mỗi số thành các phần tử của
# một List;
#- Dùng hàm int(x) để chuyển một chuỗi số sang số nguyên


n=input()
n=n.split()
X=int(input())
x=[]        #danh sách rỗng x để lưu trữ các chỉ mục (vị trí) trong danh sách n mà giá trị tại đó bằng X
for i in range(len(n)):
    if int(n[i])==X:
        x=x+[i+1]   #i+1 được thêm vào x thay vì i vì vị trí đếm bắt đầu từ 1.
if x==[]:
    print(0)
else:
    for i in x: #duyệt qua từng phần tử i trong danh sách x
        print(i)