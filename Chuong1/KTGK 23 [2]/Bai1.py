#Tính tổng các số nguyên từ a đến b (bao gồm a, b)

a=int(input())
b=int(input())
tong=0
for i in range (a,b+1):  #nếu a=b hoặc a>b thì sẽ luôn bằng 0
    tong=tong+i
print(tong)