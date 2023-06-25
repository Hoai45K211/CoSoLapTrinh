#5 Viết chương trình cho phép nhập vào một chuỗi bất kỳ, 
# đếm số chữ cái và chữ số trong câu đó và in kết quả ra màn
# hình.
#Input:
#Python Programming Class 2021
#Output:
#Chu cai: 22
#Chu so: 4


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