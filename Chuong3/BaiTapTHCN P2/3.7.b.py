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