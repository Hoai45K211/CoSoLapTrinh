#Nhập vào một dãy các số nguyên tùy ý, 
# cho đến khi bấm số 0 thì kết thúc nhập. 
# Cho biết có bao nhiêu số âm và bao nhiêu số dương 
# đã được nhập vào trong dãy số trên


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