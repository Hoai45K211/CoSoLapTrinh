#Cho n chuỗi ký tự, viết chương trình để in lên chuỗi dài 
#nhất và độ dài của từ đó. Kiểm tra điều kiện n>0, nếu
# n<=0 thì trả về None

#INPUT: nhập vào dòng 1 là số nguyên n, các dòng tiếp theo
# là n chuỗi ký tự
#OUTPUT: in lên màn hình từ dài nhất và độ dài của từ đó

#INPUT: 
# 3
# PHP
# Exercises
# Backend
#OUTPUT:
# Exercies
# 9

#INPUT
#0
#OUTPUT
#None 


n = int(input())

if n <= 0:
    print("None")

    for _ in range(n):
        chuoi = input()
        do_dai = len(chuoi)

        if do_dai > do_dai_max:
            chuoi_dai_nhat = chuoi
            do_dai_max = do_dai

    print(chuoi_dai_nhat)
    print(do_dai_max)