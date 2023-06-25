#In lên màn hình n dòng, 
# với mỗi dòng là một dãy số từ 1 đến n 
# (mỗi số nhau 1 dấu cách)


n=int(input("n="))  #nhập n
i=1                 #đếm dòng
while i<=n:         
    j=1             #đếm số lượng số trên dòng
    while j<=n:     
        print(j,end=" ")    # in giá trị của biến j lên màn hình mà không tạo dòng mới. Đặt end=" " để thêm một khoảng trắng giữa các số in ra   
        j=j+1
    print()
    i=i+1
    
#Cach FOR
n=int(input("n="))
for i in range (1,n+1,1):
    print("1 2 3 4 5")