# Viết chương trình:
#- Nhập vào một chuỗi gồm các từ được phân tách bởi dấu phẩy;
#- Chương trình thực hiện loại bỏ các từ trùng lắp, sau đó
# sắp xếp các từ theo thứ tự bảng chữ cái, phân tách nhau 
# bởi dấu phẩy rồi in kết quả ra màn hình.

#TEST:
#Input: without,hello,bag,world,bag,hello
#Output: bag,hello,without,world

#Gợi ý:
#- Tách mỗi từ trong chuỗi thành các phần tử của một List;
#- Loại bỏ các phần tử trùng trong List;
#- Dùng hàm sort() để ắp xếp các phần tử trong List theo thứ
# tự;
#- Sử dụng hàm join() để chuyển List thành chuỗi theo yêu 
# cầu.

n=input()
n=n.split(',')
m=[]
for i in n:
    if i not in m:
        m=m+[i]
m.sort()    #sắp xếp các phần tử theo thứ tự tăng dần
print(','.join(m))