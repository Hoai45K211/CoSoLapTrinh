#Ví dụ 1:
#- Nhập từ bàn phím một số nguyên n;
#- Nhập n số nguyên;
#- Lưu n và n số nguyên vào file: vd1.txt

n=int(input("n="))


f=open("vd1.txt","w")
# "w" --> mo file, neu file khong ton tai --> tao file moi, neu co thi ghi de
#Ghi so nguyen n vao file
f.write(str(n)+"\n")


#Nhap n so nguyen
st=""
for i in range(n):
    x=input()
    st=st + x + " "
   
f.write(st)
f.close()    


#_____________________________________
#Dùng hàm split() để nhận dữ liệu đầu vào từ 1 chuỗi:
st=input()      #-->5 10 15
a,b,c=st.split(" ")
a=int(a)
b=int(b)
c=int(c)


print("a=",a)
print("b=",b)
print("c=",c)
