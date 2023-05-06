#Trong bài tập này, bạn sẽ viết một hàm xác định mật khẩu
#tốt. Chúng tôi sẽ xác định mật khẩu tốt là mật khẩu có ít nhất 8 ký tự
#dài và chứa ít nhất một chữ cái viết hoa, ít nhất một chữ cái viết thường, và tại
#ít nhất một số. Hàm của bạn sẽ trả về true nếu mật khẩu được truyền cho nó dưới dạng
#tham số duy nhất của nó là tốt. Nếu không, nó sẽ trả về false. Bao gồm một chương trình chính
#đọc mật khẩu từ người dùng và báo cáo mật khẩu đó có tốt hay không. Đảm bảo
#rằng chương trình chính của bạn chỉ chạy khi giải pháp của bạn chưa được nhập vào
#một tập tin khác.


def NhapvaIn():
    pw=input("Enter a password:")
    if ktr(pw)==True:
        print("That is a good password!")
    else: print("That is not a good password!")
    return pw
def ktr(pw):
    h= False; t= False; s= False
    for i in pw:
        if i>="A" and i<="Z":
            h=True
        if i>="a" and i<="z":
            t=True
        if i>="0" and i<="9":
            s=True
    if len(pw)>=8 and h and t and s:
        return True
    else: return False
pw=NhapvaIn()
ktr(pw)