#Viết chương trình để chuyển đổi một danh sách gồm nhiều số
#nguyên thành một số nguyên duy nhất

#INPUT: nhập vào một dãy số nguyên, mỗi số cách nhau đúng
#1 ký tự trắng
#OUTPUT: in lên màn hình một số nguyên được tạo bởi các
#phần tử trong dãy số trên

#INPUT: 
# 11 3 50
#OUTPUT:
# 11350

st=input().split()

n=int(''.join(st))  #sử dụng để nối các chuỗi số nguyên trong danh sách thành một chuỗi duy nhất. Ký tự nối là một chuỗi rỗng

print(n)