# tìm và in ra các số nguyên tố nhỏ hơn hoặc bằng 
# một số nguyên dương n được nhập từ người dùng.


n=int(input())
import math
def LaSNT():
    for r in range(2,301):
        L=[]    # danh sách rỗng L để lưu trữ các số nguyên tố
        for i in range(2, int(math.sqrt(r))+1):     #for lặp qua các số từ 2 đến căn bậc hai của r (range(2, int(math.sqrt(r)) + 1)
            if r%i==0:  #Với mỗi giá trị i, kiểm tra xem r có chia hết cho i hay không (r % i == 0).
                return 0    #Nếu r chia hết cho i, tức là r không phải là số nguyên tố, hàm LaSNT() trả về giá trị 0 và kết thúc
            else: 
                L.append(r) #Nếu r không chia hết cho bất kỳ i nào, tức là r là số nguyên tố, thêm r vào danh sách L.
    return L 
L=LaSNT()   #LaSNT() trả về danh sách L chứa các số nguyên tố.
print(L)    #print(L): In ra danh sách các số nguyên tố
M=[]    #Tạo một danh sách rỗng M để lưu trữ các số nguyên tố cần in.
dem=0   
while dem<=n:   #chạy cho đến khi dem đạt giá trị n (số nguyên dương nhập từ người dùng).
    for i in range(0,len(L),):  #for duyệt qua các phần tử trong danh sách L
        M.append(L[i])  # Với mỗi phần tử L[i], thêm nó vào danh sách M.
        dem=+1

for i in range(0,len(M)+1): #for tiếp theo duyệt qua danh sách M và in từng phần tử ra màn hình.
    print(M[i],end=" ") #danh sách các số nguyên tố nhỏ hơn hoặc bằng n được in ra trên cùng một dòng, cách nhau bởi khoảng trắng.




