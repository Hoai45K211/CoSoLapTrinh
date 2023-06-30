#người dùng nhập vào các chuỗi, lưu trữ vào danh sách L. 
# Sau đó, chương trình duyệt qua danh sách L, lọc ra 
# các số nguyên dương và tính tổng của chúng, 
# và in ra tổng đó. Quá trình nhập chuỗi và tính tổng 
# tiếp tục cho đến khi người dùng nhập chuỗi 'Q', 
# khi đó chương trình dừng lại và in ra tổng cuối cùng


L=[]    #L để lưu trữ chuỗi
M=[]    #M để lưu trữ các số nguyên dương
while True:
    n=input()
    if n=='Q':  #Nếu chuỗi nhập vào là 'Q', thì dừng vòng lặp bằng lệnh break
        break
    L.append(n) #Ngược lại, thêm chuỗi vào danh sách L
for i in range(0,len(L)):
    if float(L[i])>0 and float(L[i])%1==0:      #nếu phần tử L[i] là một số nguyên dương (lớn hơn 0 và không có phần thập phân), thì thêm vào danh sách M
        M.append(L[i])      
s=0 #Khởi tạo biến s với giá trị ban đầu là 0 để tính tổng các số nguyên dương
for j in range(0,len(M)):   #Cộng giá trị số nguyên M[j] vào biến s
    s=s+int(M[j])
print(s)