i=1                         #so hoa thi
while i<=9:    
    j=9-i                   #j la so khoang cach
    print(j*" ",end="") 
    print(((2*i)-1)*"*") 
    i=i+1        
    
#Sua de: Nhap so nguyen n
n=int(input("n="))
i=1
while i<=n:
    #In len m/h (n-i) dau cach
    print(" "*(n-i),end="")

    #In len man hinh (2*i-1) dau *
    print("*"*(2*i-1))
    i=i+1