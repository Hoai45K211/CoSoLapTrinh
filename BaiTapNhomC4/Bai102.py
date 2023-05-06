#Nhiều sách công thức vẫn sử dụng cốc, muỗng canh và thìa cà phê để mô tả khối lượng
#của các thành phần được sử dụng khi nấu ăn hoặc nướng bánh. Trong khi công thức nấu ăn như vậy là đủ dễ dàng để
#làm theo nếu bạn có cốc và thìa đo lường thích hợp, chúng có thể khó
#tăng gấp đôi, gấp ba hoặc gấp bốn lần khi nấu bữa tối Giáng sinh cho toàn bộ thời gian kéo dài
#gia đình. Ví dụ: một công thức yêu cầu 4 muỗng canh nguyên liệu cần 16
#muỗng canh khi tăng gấp bốn lần. Tuy nhiên, 16 muỗng canh sẽ được thể hiện tốt hơn
#(và dễ đo lường hơn) là 1 cốc.

#Viết một hàm biểu thị một thể tích đế bằng cách sử dụng các đơn vị lớn nhất có thể
#có thể nhìn thấy được. Hàm sẽ lấy số lượng đơn vị làm tham số đầu tiên và đơn vị
#đo lường (cốc, muỗng canh hoặc muỗng cà phê) làm tham số thứ hai của nó. Trả về một chuỗi
#đại diện cho thước đo bằng cách sử dụng các đơn vị lớn nhất có thể làm kết quả duy nhất của hàm.
#Ví dụ: nếu chức năng được cung cấp các tham số đại diện cho 59 muỗng cà phê
#thì nó sẽ trả về chuỗi “1 cốc, 3 muỗng canh, 2 muỗng cà phê”.
#Gợi ý: Một cốc tương đương với 16 muỗng canh. Một muỗng canh tương đương với
#3 thìa cà phê.

def Nhapvdoi():
    global min
    print("Enter the volumes of ingredients:")
    cup=int(input("Cup:"))
    tablesp=int(input("Tapblespoon:"))
    teasp=int(input("Teaspoon:"))
    min=cup*48+tablesp*3+teasp
    return min
def rut(min):
    cp=min//48
    table=(min-cp*48)//3
    tea=(min-cp*48-table*3)
    return cp,table,tea
def inkq(cp,table,tea):
    if cp!=0:
        if cp==1: print("1 cup",end="")
        else: print(cp,"cups",end="")
        if min!=48: print(", ",end="")
    if table!=0:
        if table==1: print("1 tablespoon",end="")
        else: print(table,"tablespoons",end="")
        if tea!=0: print(", ",end="")
    if tea!=0:
        if tea==1: print("1 teaspoon",end="")
        else: print(tea,"teaspoons",end="")
Nhapvdoi()
cp,table,tea=rut(min)
inkq(cp,table,tea)