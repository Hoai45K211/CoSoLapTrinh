#Viết chương trình nhập từ bàn phím một số nguyên n (n>=2),
# in lên màn hình các số nguyên chẵn trong n số tự nhiên đầu tiên.
#Yêu cầu xây dựng các hàm sau:
#- Hàm nhap(),thực hiện việc nhập một số nguyên dương n;
#- Hàm inkq(n),thực hiện in lên màn hình các số nguyên chẵn trong n số tự nhiên đầu tiên;
#- Chương trình có thể lặp lại các công việc trên cho đến khi bấm phím k hoặc K thì kết
#thúc.

def nhap():
    n=int(input("n="))
    return n

def inkq(n):
    for i in range(2,n+1,2):
        if i % 2 == 0:
            print(i,end=" ")

while True:
    n=nhap()        #sử dụng hàm nhap() để yêu cầu người dùng nhập giá trị n từ bàn phím và lưu giá trị đó vào biến n
    inkq(n)         #hàm inkq(n) để in ra tất cả các số chẵn từ 2 đến n
    x=input("\nTiep tuc khong?")    #\n là kí tự xuống dòng
    if x=="K" or x=="k":
        break