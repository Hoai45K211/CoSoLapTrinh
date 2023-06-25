#Nhập vào số nguyên n (2<=n<=50), 
# in lên màn hình các số nguyên chẵn đầu tiên.
#Ví dụ: nếu nhập vào n=10 thì dãy số được in trên màn hình như sau 
# (trong dãy số, mỗi số cách nhau 1 dấu cách):
#a. Sử dụng vòng lặp while

n=int(input(""))        #nhập n
i=2             #khởi tạo từ 2
while 2<=n<=50 and i<=n:       #điều kiện
    print(i,end=" ")        #in ra i và cách 1 dấu cách
    i=i+2           #bước nhảy là 2