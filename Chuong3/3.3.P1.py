Tieuthu=int(input("Tieu thu="))
if 1<=Tieuthu<=100:
    Phaitra=Tieuthu*550
elif 101<=Tieuthu<=150:
    Phaitra=100*550+(Tieuthu-100)*750
elif 151<=Tieuthu<=200:
    Phaitra=100*550+50*750+(Tieuthu-150)*950
else:
    Phaitra=100*550+50*750+50*950+(Tieuthu-200)*1350
Thanhtien=Phaitra*1.1
print("Phai tra=",Thanhtien,sep=(""))