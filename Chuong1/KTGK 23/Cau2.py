#để tính tổng các số lẻ từ 1 đến n, với n là một số nguyên nhập vào từ bàn phím

n=int(input())
s=0     #biến s được khởi tạo bằng 0
for i in range (1,n+1,2):
  s=s+i
print(s)

#Ví dụ: Nếu người dùng nhập n=7, 
#chương trình sẽ tính tổng các số lẻ từ 1 đến 7 
#là 1+3+5+7=16 và in ra giá trị 16


#để tính tổng các số chẵn từ 1 đến n, với n là một số nguyên nhập vào từ bàn phím

n=int(input())
s=0     #biến s được khởi tạo bằng 0
for i in range (2,n+1,2):
  s=s+i
print(s)


#Ví dụ: Nếu người dùng nhập n = 10, 
#chương trình sẽ tính tổng các số chẵn từ 1 đến 10 là 2 + 4 + 6 + 8 + 10 = 30 
#và in ra kết quả "Tổng các số chẵn từ 1 đến 10 là: 30".