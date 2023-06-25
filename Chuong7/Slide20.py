#Viết chương trình nhập vào một xâu str và một ký tự ch, 
# in lên màn hình số lượng ký tự ch xuất hiện trong xâu str 
# (không phân biệt chữ hoa và chữ thường).

#Ví dụ:
#str=Learn PYTHON Programming
#ch=n
#Number of character n is: 3

str=input("str=")       #Nhập xâu từ người dùng
ch=input("ch=")         #Nhập ký tự từ người dùng

str1 = str.lower()      #Chuyển xâu thành chữ thường
ch2 = ch.lower()        #Chuyển xâu thành chữ thường

dem=0                   #Khởi tạo biến đếm

for char in str1:       #Lặp qua từng ký tự trong xâu đã chuyển thành chữ thường
    if char == ch2:     #Nếu ký tự hiện tại bằng ký tự đã chuyển thành chữ thường
        dem=dem+1       #Tăng biến đếm lên 1
        
print("Number of character",ch,"is:",dem)  # # In số lượng ký tự xuất hiện


#Cach 2:
str1=input("str=") 
ch=input("ch=")
dem=0
for x in str1:
    if x.upper()==ch.upper():
        dem=dem+1
print("Number of character ",ch," is:",dem)

#Cach 3:
st=input("str=")
ch=input("ch=")


dem=0
for x in st.lower():
    if x==ch.lower():
        dem=dem+1
print("Number of character "+ch+" is:",dem)
