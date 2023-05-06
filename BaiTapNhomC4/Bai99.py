#Viết chương trình cho phép người dùng chuyển đổi một số từ cơ số này sang cơ số khác.
#Chương trình của bạn phải hỗ trợ các cơ số từ 2 đến 16 cho cả số đầu vào và
#số kết quả. Nếu người dùng chọn một cơ sở bên ngoài phạm vi này thì một cơ sở thích hợp
#thông báo lỗi sẽ được hiển thị và chương trình sẽ thoát. Chia chương trình của bạn
#thành một số chức năng, bao gồm một chức năng chuyển đổi từ một cơ sở tùy ý thành
#cơ số 10, hàm chuyển đổi từ cơ số 10 thành cơ số tùy ý và hàm chính
#chương trình đọc các cơ sở và số đầu vào từ người dùng. bạn có thể tìm thấy của bạn
#Lời giải bài 77, 78, 98 hữu ích khi hoàn thành bài tập này.


def Nhap():
    s=input("Nhap:")
    bi=int(input("He co so cua du lieu nhap:"))
    bo=int(input("He co so muon doi:"))
    if bi>16 or bo>16 or bi<2 or bo<2:
        print("Khong hop le! Vui long nhap lai")
        bi=int(input("He co so cua du lieu nhap:"))
        bo=int(input("He co so muon doi:"))
    return s,bi,bo
def baseto10(s):
    if bi==16:
        h2i=s
        kq=hex2int(h2i)
    if bi==2:
        ttt=s
        kq=two2ten(ttt)
    return kq
def ten2b(s):
    if bo==16:
        i2h=s
        kq=int2hex(i2h)
    if bo==2:
        yyy=s
        kq=ten2two(yyy)
    return kq
def giao(s):
    if bi==16 and bo==2:
        h2i=s
        gi=hex2int(h2i)
        kq=ten2two(gi)
    if bi==2 and bo==16:
        ttt=s
        gi=two2ten(ttt)
        kq=int2hex(gi)
    return kq
# bai 98
def hex2int(h2i):
    try:  i= int(h2i,16)
    except: i='Khong hop le!'
    return i
def int2hex(i2h):
    if 0<=i2h<=9: h=i2h
    elif 10<=i2h<=15:
        if i2h==10: h='A'
        if i2h==11: h='B'
        if i2h==12: h='C'
        if i2h==13: h='D'
        if i2h==14: h='E'
        if i2h==15: h='F'
    else: h='Khong hop le!'
    return h
#Bai77
def two2ten(ttt):
    d_num = 0
    m = 1
    b_len = len(str(ttt))
    for k in range(b_len):
        rem = ttt%10
        d_num = d_num + (rem * m)
        m = m * 2
        ttt = int(ttt/10)
#Bai78
def ten2two(yyy):
    st=[]
    while q!=0:
        r=q%2
        st.append(r)
        q=q//2
    a=""
    while st!=[]:
        a=a+str(st.pop())
    return a
s,bi,bo=Nhap()
def kqc(bi,bo):
    if bo==10: kqcc=baseto10(s)
    elif bi==10:kqcc=ten2b(s)
    else: kqcc=giao(s)
    print(s,"tu he co so",bi,"sang he co so",bo,"la:",kqcc)
s,bi,bo=Nhap()
kqc(bi,bo)