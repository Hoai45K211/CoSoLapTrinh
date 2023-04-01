#thực hiện các phép toán cơ bản (+, -, *, /) trên 2 số a và b nhập từ bàn phím, 
#và so sánh kết quả với một số nguyên n nhập từ bàn phím

a=int(input())
b=int(input())
n=int(input())
if a-b==n:
    print('-')
elif a+b==n:
    print('+')
elif a*b==n:
    print('*')
elif a/b==n:
    print('/')
else:
    print('NO')