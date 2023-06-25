#Viết chương trình nhập vào một số nguyên n (n>0), và n số 
# nguyên lưu trữ vào List A. In lên màn hình: tổng giá trị
# của các phần tử ở vị trí có thứ tự chẵn trong List A 
# (biết rằng phần tử thứ 1 có số chỉ mục là 0 sẽ có thứ tự 
# là 1, ...).

#n=5
#8
#10
#12
#4
#7
#Tong=14


A=[]
n=int(input("n="))
s=0
for i in range(0,n):
    x=int(input())
    A=A+[x]
for i in range(0,n):
    if i%2!=0:
        s=s+A[i]
print("Tong=",s,sep="")