#Trong một khu vực tài phán cụ thể, biển số xe cũ hơn bao gồm ba chữ cái theo sau là
#ba số. Khi tất cả các biển số theo mẫu đó đã được sử dụng,
#định dạng đã được thay đổi thành bốn số theo sau là ba chữ cái.
#Viết hàm tạo biển số xe ngẫu nhiên. chức năng của bạn nên có
#tỷ lệ xấp xỉ bằng nhau để tạo ra một chuỗi ký tự cho giấy phép cũ
#biển số hoặc biển số xe mới. Viết chương trình chính gọi hàm của bạn và
#hiển thị biển số xe được tạo ngẫu nhiên.


import random
def LPCheck(s):
    a=chr(random.randrange(65,91))
    b=chr(random.randrange(65,91))
    c=chr(random.randrange(65,91))
    e=chr(random.randrange(48,58))
    f=chr(random.randrange(48,58))
    g=chr(random.randrange(48,58))
    h=chr(random.randrange(48,58))
    if s=='old':
        lp=e+f+g+'-'+a+b+c
        print('Old license plate: %s' %lp)
    if s=='new':
        lp=e+f+g+h+'-'+a+b+c
        print('New license plate: %s' %lp)
LPCheck('new')