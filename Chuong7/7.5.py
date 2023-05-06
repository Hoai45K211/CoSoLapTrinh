def Bai75(st):
    chucai=0
    so=0
    kytudacbiet=0
    for ch in st:
        if ch.isnumeric():
            so+=1
        elif ch.isalpha():
            chucai+=1
        else:
            kytudacbiet+=1
   
    print("Chu cai:",chucai)
    print("Chu so:",so)
    print("Khac:",kytudacbiet)
   
st="Python $ Programming % # & * ^ Class 2021"
Bai75(st)