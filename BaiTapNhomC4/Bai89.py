#Nhiều người viết chữ in hoa không đúng, nhất là khi gõ chữ nhỏ
#các thiết bị như điện thoại thông minh. Trong bài tập này, bạn sẽ viết một hàm viết hoa
#các ký tự thích hợp trong một chuỗi. Chữ thường “i” nên được thay thế bằng một
#chữ hoa “I” nếu nó được đặt trước và theo sau bởi khoảng trắng. Ký tự đầu tiên trong
#chuỗi cũng phải được viết hoa, cũng như ký tự không phải dấu cách đầu tiên sau dấu
#“.”, “!” hoặc "?". Ví dụ: nếu chức năng được cung cấp với chuỗi “mấy giờ
#tôi có phải ở đó không? địa chỉ là gì? thì nó sẽ trả về chuỗi “What
#thời gian tôi phải ở đó? Địa chỉ là gì?”. Bao gồm một chương trình chính đọc
#một chuỗi từ người dùng, viết hoa nó bằng hàm của bạn và hiển thị kết quả.


def Nhap():
    ch=str(input("Enter:"))
    return ch
def Hoa(ch):
    day=ch.capitalize()
    day=day.replace(" i "," I ")
    vtr=0
    while vtr<len(ch):
        if day[vtr]=="." or day[vtr]=="!" or day[vtr]=="?": 
            vtr=vtr+1
            while vtr<len(ch) and day[vtr]==" ": vtr=vtr+1
            if vtr<len(ch): day=day[0:vtr]+\
                                day[vtr].upper()+\
                                day[vtr+1:len(day)]
        vtr=vtr+1
    return day
ch=Nhap()
day=Hoa(ch)
print(day)
