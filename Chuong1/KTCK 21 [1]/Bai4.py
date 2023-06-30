#Cho 3 chuỗi ký tự, viết chương trình đảo ngược các ký tự 
#của chuỗi và in kết quả lên màn hình.

#INPUT: nhập vào 3 dòng, mỗi dòng là 1 chuỗi ký tự
#OUTPUT: in lên màn hình các chuỗi ký tự đã được đảo ngược
#các ký tự

#INPUT
#python
#list
#exercises

#OUTPUT:
# nohtyp
# tsil
# sesicrexe

st1 = input().split()
st2 = input().split()
st3 = input().split()

st1.reverse()
st2.reverse()
st3.reverse()

print(st1)
print(st2)
print(st3)


#Cach 2
chuoi_1 = input()
chuoi_2 = input()
chuoi_3 = input()

chuoi_dao_nguoc_1 = chuoi_1[::-1]
chuoi_dao_nguoc_2 = chuoi_2[::-1]
chuoi_dao_nguoc_3 = chuoi_3[::-1]

print(chuoi_dao_nguoc_1)
print(chuoi_dao_nguoc_2)
print(chuoi_dao_nguoc_3)