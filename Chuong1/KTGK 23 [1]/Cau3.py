#Tìm số nguyên tố lớn nhất nhỏ hơn hoặc bằng số nguyên n, với n là một số nguyên nhập vào từ bàn phím
#SNT chỉ chia hết cho 1 và chính nó

n=int(input())
def LaSoNguyenTo(n): 
  x=0 #biến khởi tạo
  for i in range(2,n+1): 
    if n%i==0:
      x=1   
  if x==0:  #n không chia hết cho bất kỳ số nguyên dương nào khác 1 và chính nó
    return False 
  else:     #n chia hết cho một số nguyên dương khác 1 và chính nó
    return True
i=n-1
while i>2:  #while được sử dụng để tìm số nguyên tố lớn nhất nhỏ hơn hoặc bằng n
  if LaSoNguyenTo(i)==True:    #trong mỗi vòng lặp, chương trình kiểm tra xem giá trị của i có phải là số nguyên tố bằng cách gọi hàm
    print(i) 
    break
  i=i-1     #nếu không, chương trình sẽ giảm giá trị của i đi 1 và tiếp tục vòng lặp
  
  #Ví dụ: Nếu người dùng nhập n=20, 
  #chương trình sẽ tìm số nguyên tố lớn