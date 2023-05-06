def nhap():
    print("Nhap 3 so nguyen:")
    a = int(input("a="))
    b = int(input("b="))
    c = int(input("c="))
    return a,b,c

def max(a,b,c):
    max=b
    if max<a:
        max=a
    if max<c:
        max=c
        return max
    
def inkq(kq):
    print("So lon nhat la:",kq)

a,b,c=nhap()
kq=max(a,b,c)
inkq(kq)