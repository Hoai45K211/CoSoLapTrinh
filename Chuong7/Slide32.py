#Viết hàm checkstring(st1,st2,st3) kiểm tra chuỗi st1 là hợp
# lệ nếu bắt đầu bằng st2 hoặc kết thúc bằng st3. Hợp lệ thì 
# hàm trả về True, còn lại trả về False.

#TEST 1:
#st1="Python Programming" 
#st2="Py"
#st3="ming"
#--> True
#TEST 2:
#st1="Python Programming"
#st2="PY"
#st3="MING"
#--> False

def checkstring(st1, st2, st3):
    if st1.startswith(st2) or st1.endswith(st3):
        return True
    else:
        return False

# Test
st1 = "Python Programming"
st2 = "Py"
st3 = "ming"
print(checkstring(st1, st2, st3))  # Output: True

st1 = "Python Programming"
st2 = "PY"
st3 = "MING"
print(checkstring(st1, st2, st3))  # Output: False