#Viết chương trình nhập vào 2 ký tự (chữ cái) viết thường 
# được lưu vào 2 biến kiểu char a và b. Liệt kê ra các 
# chữ cái viết hoa trong đoạn [a,b]

#Dữ liệu vào
#Hai ký tự là 2 chữ cái, cách nhau bằng 1 dấu cách
##Giới hạn:
#Chữ cái thứ nhất có thứ tự không đứng sau chữ cái thứ 2
# trong bảng chữ cái
#2 chữ cái nhập vào ở dạng viết thường
#Bảng chữ cái được nhắc tới là bảng chữ cái tiếng Anh

#Dữ liệu ra
#Các chữ cái viết hoa trong phạm vi của 2 chữ cái nhập vào,
# in ra theo thứ tự bảng chữ cái và cách nhau bằng 1 
# dấu cách (nếu có nhiều hơn 1 chữ cái thỏa mãn)

#Ví dụ
#Input 
#a c
#Output 
#A B C

a, b = [str(x) for x in input().split()]
str = "a.b.c.d.e.f.g.h.i.j.k.l.m.n.o.p.q.r.s.t.u.v.w.x.y.z"
L = str.split(".")
id1 = L.index(a)  # Lay index cua chu cai a trong bang chu cai
id2 = L.index(b)  # Lay index cua chu cai b trong bang chu cai
if id1 <= id2:  # a khong dung sau b trong bang chu cai
    A = []
    for x in range(id1, id2 + 1):  # Duyet qua bang chu cai tu index cua a den index cua b va dua vao list A
        A.append(L[x].upper())
    for y in A:
        if len(A) == 1:  # Neu chi co 1 chu cai thoa man ta khong in dau cach phia sau
            print(y)
        else:
            print(y, end=" ")