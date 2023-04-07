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