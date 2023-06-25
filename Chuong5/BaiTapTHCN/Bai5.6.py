#Viết chương trình nhập vào từ bàn phím 10 số nguyên 
# và lưu vào một List A. Hãy hoán đổi giá trị của 2 phần tử
# nằm cạnh nhau (theo từng đôi) trong List.
# Và in lên màn hình List kết quả sau khi xử lý.


#5
#7
#2
#6
#3
#7
#8
#9
#1
#2
#7 5 6 2 7 3 9 8 2 1

A=[]
B=[]
for i in range(0,10):
    x=int(input())
    A.append(x)
    B.append(x)
for i in range(0,10,2):
    B[i]=A[i+1]
    B[i+1]=A[i]
for i in range(len(B)):
    print(B[i],end=" ")