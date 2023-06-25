#Viết chương trình thực hiện tính n!
#Biết rằng: n!=n*(n-1)!
#0!=1
#b. Sử dụng vòng lặp for
#Trong đó:
#- n được nhập vào từ bàn phím
#- Chương trình có thể lặp lại việc nhập giá trị n và tính n!, 
#cho đến khi n<0 thì dừng

n=int(input())
b=1    #giá trị ban đầu là 1, đây là giá trị khởi tạo của tích số giai thừa
while n>=0:    #được thực thi liên tục cho đến khi người dùng nhập giá trị n nhỏ hơn 0
    for i in range(1,n+1):
        if n==0:
            print(1)
            n=int(input())
            continue    #Nếu n bằng 0, vòng lặp for sẽ bị bỏ qua và vòng lặp while tiếp tục được thực thi. Dòng lệnh continue sẽ chuyển đến vòng lặp tiếp theo của while
        b=b*i
    print(b)
    n=int(input())
    b=1
    continue


#C2:
while True:
    n=int(input(""))
    if n<0:
        break
    giaithua=1
    for i in range(1,n+1,1):
        giaithua=giaithua*i
    print(giaithua)  