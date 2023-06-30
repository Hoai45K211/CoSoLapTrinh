#Cho một danh sash L gồm các số nguyên. Viết chương trình 
#để xác định các số lẻ lưu vào danh sách L1, các số chẵn
#lưu vào danh sách L2

#INPUT: nhập vào các số nguyên là các phần tử của danh sách
#L, mỗi phần tử cách nhau đúng 1 dấu cách
#OUTPUT: in lên màn hình dòng 1 và dòng 2 là giá trị của
#các phần tử trong L1 và L2

#INPUT: 
# 1 2 3 4 5 6 7
#OUTPUT:
# [1, 3, 5, 7]
# [2, 4, 6]


L=input().split()

L1 = []
L2 = []

for i in L:
    n = int(i)
    if n % 2 == 0:
        L2.append(n)
    else:
        L1.append(n)
        
print(L1)
print(L2)