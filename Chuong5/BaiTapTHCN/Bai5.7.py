#5.7. Viết chương trình nhập vào một số nguyên n (n>0) và 
# n số nguyên lưu vào List L. Thực hiện loại bỏ những 
# phần tử có giá trị trùng nhau và lưu tập mới vào List M. 
# In lên màn hình các phần tử trong M.

#n=5
#2
#4
#2
#5
#4
#2 4 5


L=[]
M=[]
n=int(input("n="))
for i in range(1,n+1):
    x=int(input())
    L.append(x)
for i in L:
    if i not in M:
        M.append(i)
for i in M:
    print(i,end=" ")