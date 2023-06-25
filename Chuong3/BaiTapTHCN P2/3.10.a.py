#Nhập từ bàn phím số nguyên n (n>=1), thực hiện các yêu cầu sau:
#a. In lên màn hình dãy số từ 1 đến n, 
# với điều kiện mỗi số nằm trên một dòng văn bản

n=int(input("n="))
i=1
while n>=1 and i<=n:
    print(i)
    i=i+1
    
    
#Cach FOR

n=int(input("n="))
for i in range(n):      #hàng trong ma trận, với biến i từ 0 đến n-1.
    for j in range(1,n+1):      #cột trong hàng hiện tại, với biến j từ 1 đến n
        print(j, end=" ")       #in giá trị của j, kết thúc bằng một khoảng trắng để ngăn cách các giá trị trong cùng một hàng
    print()                     #in một dòng mới