#Viết chương trình để loại bỏ các ký tự không mong muốn khỏi
#một chuỗi đã cho. Biết rằng, các ký tự không mong muốn
#bao gồm #, ",!,^,%

#INPUT: nhập vào một chuỗi ký tự bất kỳ
#OUTPUT: in lên màn hình chuỗi đã được loại bỏ các ký tự 
#không mong muốn

#INPUT:
# Pyth^^on Exercis^es
#OUTPUT:
# Python Exercies

st=input()
kytu = ["#", "\"", "!", "^", "%"]

st1=""

for i in st:
    if i not in kytu:
        st1=st1+i
        
print(st1)