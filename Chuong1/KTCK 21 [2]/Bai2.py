#Viết chương trình để tìm các giá trị kiểu số lớn nhất và
# nhỏ nhất trong một danh sách không đồng nhất đã cho

#INPUT: nhập vào một dãy các số hoặc các từ, mỗi giá trị
#cách nhau đúng 1 ký tự trắng
#OUTPUT: in len màn hình một danh sách có 2 phần tử, là giá
#trị kiểu số lớn nhất và nhỏ nhất trong tập hợp trên

#INPUT:
# 4 Python 3 2 version 5
#OUTPUT:
# [5, 2]


st = input().split()
n = []
for i in st:
    if i.isnumeric():
        n.append(int(i))

max = max(n)
min = min(n)

st1 = [max, min]
print(st1)