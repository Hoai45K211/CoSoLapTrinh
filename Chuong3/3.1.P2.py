#Nhập từ bàn phím một số nguyên n, 
# trong đó n>=1 và n<=50.
#Nếu n không thuộc miền trên thì yêu cầu nhập lại.

n=int(input("n="))
while 50<n or n<1:
    print("Moi nhap lai")
    n=int(input("n="))