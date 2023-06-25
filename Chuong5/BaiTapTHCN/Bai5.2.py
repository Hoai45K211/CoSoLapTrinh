#5.2. Viết chương trình có sử dụng hàm thực hiện các 
# yêu cầu sau:
#- Hàm Input(): nhập một số nguyên n (n>0) và n số nguyên 
# lưu trữ vào một List L;
#- Hàm Search(L): Tìm và trả về số nhỏ nhất và lớn nhất
# trong List L;
#- Hàm Output(max, min): In lên màn hình số lớn nhất max 
# và bé nhất min;
#Lưu ý: không được sử dụng hàm chuẩn max() và min()
# trong Python.

#n=5
#10
#15
#3
#2
#7
#15 2


def Input():
    L=[]
    global n    ##là biến toàn cục, nghĩa là nó có thể được truy cập và sử dụng trong bất kỳ hàm nào trong chương trình
    n=int(input("n="))
    n=int(input("n="))
    for i in range(0,n):
        x=int(input())
        L=L+[x]
    return L
def Search(L):
    max=L[0]
    for i in range(0,n):
       if max<L[i]:
           max=L[i]
    min=L[0]
    for i in range(0,n):
        if min>L[i]:
           min=L[i]
    return max,min
def Output(max,min):
    print(max,min)

L=Input()
max,min=Search(L)
Output(max,min)