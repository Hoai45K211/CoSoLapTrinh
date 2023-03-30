def Nhap():
    n=int(input("n="))
    return n

def NhapVaDem(n):
    print("Nhap",n,"so nguyen:")
    dem=0
    for i in range(1,n+1):
        x=int(input())
        if x%2==0 and x!=0: 
            dem=dem+1
    return dem

def InKQ(kq):
    print("So chu so chan la:",kq)

n=Nhap()
kq=NhapVaDem(n)
InKQ(kq)
