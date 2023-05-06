#Ví dụ 2: Phương thức writelines
#n=int(input("n="))


f=open("vd1.txt","w")
# "w" --> mo file, neu file khong ton tai --> tao file moi, neu co thi ghi de
#Ghi so nguyen n vao file
f.write(str(n)+"\n")


#Nhap n so nguyen
L=[]
for i in range(n):
    x=input()
    L.append(x + " ")
   
f.writelines(L)
f.close()
