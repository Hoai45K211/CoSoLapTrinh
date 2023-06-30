#Số hoàn hảo (số hoàn thiện) là một số nguyên dương mà 
# tổng các ước nguyên dương của nó (không bao gồm ước 
# lớn nhất) bằng chính nó.

#Ví dụ:
#6=1+2+3 là một số hoàn hảo.
#Nhiệm vụ của bạn là viết chương trình kiểm tra 1 
# số nguyên nhập từ bàn phím có phải số hoàn hảo hay không!

#Dữ liệu vào
#Số nguyên n cần kiểm tra
#Giới hạn: |n| <=10^9
#Dữ liệu ra
#In ra YES nếu n là số hoàn hảo
#Và ngược lại

#Ví dụ
#Input 
#6
#Output 
#YES

n = int(input())
i = 1
s = 0
if 0 <= n <= 10**9:
	for x in range(1, n):
		if n % i == 0:
			s += i
		i += 1
	if s == n:
		print("YES")
	else:
		print('NO')
else:
	print('NO')