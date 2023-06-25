#Xây dựng một hàm có đầu vào là một chuỗi bất kỳ, đầu ra là 
# 2 chuỗi, trong đó chuỗi 1 được viết thường toàn xâu, 
# chuỗi 2 được viết hoa toàn xâu.
#Input:
#Learning Python
#Output:
#learning python
#LEARNING PYTHON


def Bai74(st):
    return st.lower(), st.upper()


st="Learning Python"


st1,st2=Bai74(st)
print(st1)
print(st2)