def nhap():
    n=int(input("n="))
    return n

def inkq(n):
    for i in range(2,n+1,2):
        if i % 2 == 0:
            print(i,end=" ")
    return n

while True:
    n=nhap()        #sử dụng hàm nhap() để yêu cầu người dùng nhập giá trị n từ bàn phím và lưu giá trị đó vào biến n
    inkq(n)         #hàm inkq(n) để in ra tất cả các số chẵn từ 2 đến n
    x=input("\nTiep tuc khong?")    #\n là kí tự xuống dòng
    if x=="K" or x=="k":
        break