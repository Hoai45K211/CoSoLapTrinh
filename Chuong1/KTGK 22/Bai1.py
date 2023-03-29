soluong=int(input('So luong='))
mahang=int(input('Ma hang='))
if mahang==1:
    thanhtien = soluong * 750 + (soluong * 750 * 0.1)
elif mahang==2:
    thanhtien = soluong * 500 + (soluong * 500 * 0.1)
else:
    thanhtien = soluong * 250 + (soluong * 250 * 0.1)
print('Thanh tien=',thanhtien,sep='')