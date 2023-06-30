#Viết chương trình để tạo một danh sách mới gồm các phần tử 
#chung từ 2 danh sách cho trước.

#INPUT: nhập vào 2 dòng, mỗi dòng là một dãy các từ, mỗi từ
#cách nhau đúng 1 ký tự trắng
#OUTPUT: in lên màn hình một danh sách mới gồm các phần tử 
#chung từ 2 danh sách trên

#TEST
#INPUT: 
# Red Green White Orange
# Green Black White Pink
#OUTPUT:
# ['Green','White]

#INPUT:
# An Nam
# Binh
#OUTPUT:
# []

st1=input().split()
st2=input().split()

st3=[]
for i in (st1):
    if i in st2:
        st3.append(i)
        
print(st3)


