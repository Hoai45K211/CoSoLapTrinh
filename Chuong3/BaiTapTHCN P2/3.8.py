y=str(input(""))
n=int(input(""))
i=1
while i<=n and 1<=n<=20:  #lặp lại cho đến khi giá trị của biến i vượt quá giá trị của biến n hoặc giá trị của biến n không nằm trong khoảng từ 1 đến 20
    j=1
    while j<=i:      #lặp lại cho đến khi giá trị của biến j vượt quá giá trị của biến i
        print(y,end=" ",sep="")
        j=j+1
    print("")   #in ra một dòng trống để xuống dòng tiếp theo
    i=i+1
    
    
#Cach khac (tu lam)
y=str(input(""))
n=int(input(""))

for i in range (1,n+1,1):
    print(i * "* ")