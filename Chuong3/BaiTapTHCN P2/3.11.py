#yêu cầu người dùng nhập các số nguyên từ bàn phím 
# cho đến khi người dùng nhập số 0. 
# Sau đó, chương trình đếm và in ra số lượng số dương và số lượng số âm đã được nhập.

soam=0      #biến đếm
soduong=0   #biến đếm
while True:
    a=int(input())
    if a==0:
        break       #nếu = 0 thì thoát
    elif a>0:       #nếu > 0 thì tăng lên đếm SD
        soduong=soduong+1
    else:           #nếu < 0 thì tăng lên đếm SÂ
        soam=soam+1
print(soduong,"so duong")
print(soam,"so am")