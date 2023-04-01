# Đoạn code trên là yêu cầu người dùng nhập một số nguyên và 
# sau đó yêu cầu người dùng nhập một chuỗi ký tự nhiều lần tùy theo giá trị của số nguyên đó. 
# Chương trình sẽ tính tổng các số từ một đến chín ứng với các chuỗi ký tự được người dùng nhập vào. 
# Cuối cùng, chương trình sẽ in ra tổng các số đó.

n=int(input())
s=0 #biến s được khởi tạo bằng 0 để tính tổng các số tương ứng với các chuỗi ký tự được nhập vào

for i in range(1,n+1):  #vd n=3 if sẽ chạy 3 lần rồi tính tổng 3 lần
  a=str(input())
  if a== 'one':
      s=s+1
  elif a== 'two':
      s=s+2
  elif a== 'three':
      s=s+3 
  elif a=='four':
      s=s+4
  elif a=='five':
      s=s+5
  elif a== 'six':
      s=s+6 
  elif a=='seven':
      s=s+7
  elif a=='eight':
      s=s+8
  elif a=='nine':
      s=s+9 #tổng các số tương ứng với các chuỗi ký tự được nhập vào
print(s)

#Ví dụ: Nếu người dùng nhập n=3 
#và chuỗi ký tự là 'two', 'five', 'three', 
#chương trình sẽ tính tổng là 2+5+3=10 và in ra giá trị 10