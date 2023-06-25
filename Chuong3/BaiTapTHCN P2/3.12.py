#Nhập một số nguyên n (0<=n<=9999) từ bàn phím. 
#In lên màn hình giá trị đã được mã hóa theo quy tắc sau:
#- Các chữ số nằm trong số nguyên n được mã hóa thành chữ cái;
#- Các chữ số được mã hóa theo quy tắc sau: 
#0 -> A
#1 -> B
#2 -> C
#3 -> D
#4 -> E
#5 -> F
#6 -> G
#7 -> H
#8 -> K
#9 -> L


n=input("")
char="ABCDEFGHKL"

if int(n)>=0 and int(n)<=10000:
    y=0
    while y<len(n):
        print(char[int(n[y])],end="")
        y+=1