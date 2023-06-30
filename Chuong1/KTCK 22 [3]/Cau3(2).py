#nhập vào một số nguyên n và sau đó nhập n số nguyên. 
# Chương trình sẽ chia danh sách số nguyên thành hai phần,
# tính tổng của các phần tử trong mỗi phần, 
# và in ra tổng hiệu của hai tổng đó.


import math

L = []
K = []
n = int(input("Nhập số lượng số nguyên: "))
s1 = 0
s2 = 0

if n > 0:
    for h in range(1, n + 1):
        x = int(input("Nhập số nguyên thứ {}: ".format(h)))
        L.append(x)
        
    for i in range(0, len(L)):
        if float(L[i]) > 0 and float(L[i]) % 1 == 0:
            M.append(L[i])
            
    for j in range(0, len(M)):
        s += int(M[j])
        
    print("Tổng của các số nguyên là:", s)
else:
    print("Số lượng số nguyên không hợp lệ!")