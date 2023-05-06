#Một ngày kỳ diệu là một ngày mà ngày nhân với tháng bằng hai chữ số
#năm. Ví dụ: ngày 10 tháng 6 năm 1960 là một ngày kỳ diệu vì tháng Sáu là tháng thứ sáu và
#6 nhân 10 là 60, bằng năm có hai chữ số. Viết hàm xác định
#có hay không một ngày là một ngày kỳ diệu. Sử dụng chức năng của bạn để tạo một chương trình chính
#tìm và hiển thị tất cả các ngày kỳ diệu trong thế kỷ 20. Bạn sẽ có thể
#thấy lời giải của bạn cho Bài tập 100 hữu ích khi hoàn thành bài tập này.


def MagicDate(ngay,thang,nam):
    if ngay* thang == nam %100:
        return True
    else:
        return False
def Magic():
    for nam in range(1900,2000):
        for thang in range(1,13):
            for ngay in range(1,30):
                if MagicDate(ngay,thang,nam):
                    print("%02d/%02d/%04d la ngay ki dieu "%(ngay,thang,nam))
Magic()