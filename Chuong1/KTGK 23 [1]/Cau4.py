# đếm số lượng các số chẵn và chia hết cho 3 trong khoảng từ 1 đến n+1, trong đó n là một số nguyên nhập từ bàn phím.

n=int(input()) 
d=0 #d được khởi tạo bằng 0 để đếm số lượng các số chẵn và chia hết cho 3 trong khoảng từ 1 đến n+1
for i in range (1,n+2): 
  if i%2==0 and i%3==0: 
    d=d+1
print(d)

#Ví dụ: Nếu người dùng nhập n=10, 
#chương trình sẽ đếm số lượng các số chẵn và chia hết cho 3 trong khoảng từ 1 đến 11 (bao gồm 11), 
#tức là 6 và 12, và in ra giá trị 2.