#Bài tập:
#- Nhập vào 3 xâu st1, st2, st3;
#- In lên màn hình vị trí (index) đầu tiên st2 xuất hiện trong st1;
#- Thay thế tất cả các xâu st2 bằng st3;
#- In lên màn hình xâu kết quả.
#Ví dụ:
#st1=Toi hoc python, python la NNLT manh
#st2=python
#st3=Python
#Vi tri xuat hien st2: 8
#Xau ket qua: Toi hoc Python, Python la NNLT manh

#Cach 1:
st1 = input("st1=")
st2 = input("st2=")
st3 = input("st3=")

i = st1.find(st2)  # Tìm vị trí đầu tiên của st2 trong st1
print("Vi tri xuat hien st2:",i)

st1 = st1.replace(st2, st3)  # Thay thế tất cả các xâu st2 bằng st3 trong st1
print("Xau ket qua:", st1)

#Cach 2:
st1=input('st1=')
st2=input('st2=')
st3=input('st3=')
print('Vi tri xuat hien st2:',st1.find(st2))
print('Xau ket qua:',st1.replace(st2,st3))