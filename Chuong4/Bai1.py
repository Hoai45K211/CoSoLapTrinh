def Nhap():
    n=int(input("n="))
    return n

def LaSNT(x):
    for i in range(2,x):    #x la SNT neu x khong chia het cho cac so tu 2 den x-1
        if x%i==0:          #for i in range (2,int(math.sqrt(n)+1)):
            return False    #con lai tra ve False (2)
    return True             #tra ve True neu x la SNT (1)

def inKQ(n):
    if LaSNT(n):
        print(n,"la SNT")
    else:
        print(n,"khong la SNT")

n=Nhap()
inKQ(n)