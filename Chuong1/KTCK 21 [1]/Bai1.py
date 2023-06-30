#Cho một danh sách và một từ, viết chương trình để chèn một 
#phần tử vào trước mỗi phần tử của danh sách 

#INPUT: nhập vào dòng thứ 1 là một dãy các từ, mỗi từ cách 
#nhau đúng 1 ký tự trắng. Dòng thứ 2 là 1 từ

#OUTPUT: in lên màn hình một danh sách mới gồm các phần tử 
#chung từ hai danh sách trên

#TEST
#INPUT
# Red Green Black
# Blue

#OUTPUT
# ['Blue', 'Red', 'Blue', 'Green', 'Blue', 'Black']


st=input().split()      #phương thức split() để tách các từ thành một danh sách
a=input()

st1=[]
for i in st:
    st1.append(a)
    st1.append(i)
    
print(st1)