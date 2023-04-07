#Nhap tu ban phim 1 so nguyen n
#In len man hinh n so nguyen to dau tien
#n=5
#2, 3, 5, 7, 11

def Nhap():
    n=int(input("n="))
    return n

def LaSNT(x):
    for i in range(2,x):    
        if x%i==0:          
            return False    
    return True

#inKQ(n)
#in len man hinh, day n so nguyen to dau tien
#dem=0
#k=1
#B1: neu k la SNT -> dem=dem+1
#B2: k=k+1
#B3: neu dem<n thi lap lai B1 / con lai thi dung

def InKQ(n):
    dem=0
    k=2
    while (dem<n):
        if LaSNT(k)==True:
            print(k, end=", ")
            dem=dem+1
        k=k+1

n=Nhap()
InKQ(n)