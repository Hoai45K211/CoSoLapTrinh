#Viết chương trình:
#- Cho phép nhập vào một chuỗi là các số nhị phân 4 chữ số,
# phân tách bởi dấu phẩy;
#- Chương trình kiểm tra xem các số nhị phân trên có chia
# hết cho 3 không. 
#- In lên màn hình dãy số nhị phân chia hết cho 3, nếu có
# nhiều số thì mỗi số cách nhau bởi 1 dấu phẩy.

#TEST1:
#Input: 0110,0010,1001,1010
#Output: 0110,1001
#TEST2:
#Input: 0100,0010,1010,1000
#Output:

#Gợi ý: 
#- Sử dụng hàm split() để tách mỗi số thành các phần tử của một List;
#- Hàm int(x,2) cho phép chuyển số nhị phân x sang số nguyên;
#- Sử dụng hàm join() để nối các số nhị phân chia hết cho 3 thành 1 chuỗi

n=input()
n=n.split(',')
m=[]
for i in n:
    if int(i,2)%3==0:   #if kiểm tra xem giá trị của phần tử i (đã chuyển thành số nguyên nhị phân bằng int(i, 2)) chia hết cho 3 hay không (%3==0).
        m=m+[i]
print(','.join(m))  #join() để nối các phần tử trong danh sách m thành một chuỗi, với dấu phân cách là ,