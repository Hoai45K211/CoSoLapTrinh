#Viết chương trình để xóa tất cả những ký tự trùng lặp 
# trong một chuỗi ký tự

#INPUT: nhập vào một chuỗi ký tự cách nhau bởi 1 dấu trắng
#OUTPUT: in lên màn hình chuỗi đã được loại bỏ bởi các từ
#trùng lặp

#INPUT: 
# Exercises Practice Solution Exercises
#OUTPUT:
# Exercies Practice Solution 

st = input().split()

st1 = []
for i in st:
    if i not in st1:
        st1.append(i)

st2 = ' '.join(st1)
print(st2)


