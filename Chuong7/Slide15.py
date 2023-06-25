#Viết chương trình:
#- Nhập vào một xâu ký tự st1;
#- Nhập vào 1 xâu st2, kiểm tra nếu st2 xuất hiện trong st1 
# thì yêu cầu nhập lại xâu khác, còn lại thì dừng.
#Ví dụ:
#Python Programming
#Python
#Pro
#thon
#abc

st1=input()
st2=input()

while st2 in st1:
    st2=input("")
    
#Cach2:
st1=input()
while True:
    st2=input()
    if st2 not in st1:
        break
