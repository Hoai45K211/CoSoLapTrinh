#Viết chương trình thực hiện tính n!
#Biết rằng: n!=n*(n-1)!
#0!=1
#a. Sử dụng vòng lặp while
#Trong đó:
#- n được nhập vào từ bàn phím
#- Chương trình có thể lặp lại việc nhập giá trị n và tính n!, 
#cho đến khi n<0 thì dừng

while True:
    n=int(input(""))
    t=1
    i=1
    while i<=n:
        t=t*i
        i=i+1
    if n<0:
        break
    print(t)
    
    
#C2:
while True:
    n=int(input(""))
    if n<0:
        break
    giaithua=1
    i=1
    while i<=n:
        giaithua=giaithua*i
        i=i+1
    print(giaithua)