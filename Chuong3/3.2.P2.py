#Nhập số nguyên n (1<=n<=50) từ bàn phím. 
# In lên màn hình bảng chữ số theo cấu trúc sau.
#Ví dụ, nếu n=45, kết quả màn hình như sau:
#1 2 3 4 5 6 7 8 9 10
#11 12 13 14 15 16 17 18 19 20
#21 22 23 24 25 26 27 28 29 30
#…
#41 42 43 44 45

n=int(input("n="))
i=1                             #viet truoc
while i<=n:                     #viet truoc
    print(i,end=" ")            #de cach ra 1 dau cach
    if i%10==0:                 #neu chia het cho 10
        print()                 #thi xuong dong
    i=i+1                       #viet truoc