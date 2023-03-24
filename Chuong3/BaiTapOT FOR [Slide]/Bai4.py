while True:
    a = float(input("a="))
    b = float((input("b=")))
    toantu = input("Toan tu:")
    
    if toantu == "+":
        ketqua = a + b
    elif toantu == "-":
        ketqua = a - b
    elif toantu == "*":
        ketqua = a * b
    elif toantu == "/":
        ketqua = (a / b)
    else:
        print("Toán tử không hợp lệ!")
        continue
    print(f"{a}{toantu}{b}={ketqua}")
    
    tieptuc = input("Tiep tuc:")
    if tieptuc.lower() == "t":
        break