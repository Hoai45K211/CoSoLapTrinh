#- Nhập từ bàn phím hai số thực: a và b;
#- Nhập từ bàn phím một toán tử (+, -, *, /);
#- In lên màn hình kết quả của biểu thức tương ứng;
#- Chương trình sẽ lặp lại việc tính trên cho đến khi bấm phím T hoặc t
#thì kết thúc.

while True:
    a=float(input("a="))
    b=float(input("b="))
    tt=input("Toan tu:")
   
    if tt=="+":
        kq=a+b
    elif tt=="-":
        kq=a-b
    elif tt=="*":
        kq=a*b
    else:
        kq=a/b

    if (tt=="/") and b==0:
        print("Khong thuc hien duoc!!!")
    else:
        print(a,tt,b,"=",kq,sep="")

    lap=input("Tiep tuc: ")
    if lap=="T" or lap=="t":
        break