#Cho file input.txt:
#5
#1 2 3 4 5

#Bài toán:
#- Đọc file input.txt
#- Dòng 1: 1 số nguyên n
#- Dòng 2: lưu trữ n số nguyên
#- Đếm có bao nhiêu chữ số chẵn và ghi kết quả vào 1 file: output.txt

f=open("input.txt","r")


n=f.readline()
n=int(n)    #Chuyen chuoi sang So


st=f.readline()
f.close()


L=st.split()      #~ st.split(" ")


dem=0
for x in L:
    x=int(x)    #Chuyen sang So nguyen
    if x%2==0:
        dem+=1


# Cach 1:
# f=open("output.txt","w")
# f.write(dem)
# f.close()


# Cach 2:
with open("output.txt","w") as f:
    f.write(str(dem))
