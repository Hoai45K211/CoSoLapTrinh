#nhập vào một số nguyên n, 
#đếm số lượng số nguyên dương (>0) không vượt quá n mà chia hết cho cả 3 và 5

n = int(input(""))
dem = 0        #biến đếm
i = 1
while i <= n:
    if i % 3 == 0 and i % 5 == 0:
        dem = dem + 1
    i += 1
print(dem)




#cach FOR
n = int(input(""))
dem = 0        #biến đếm
for i in range(1,n+1):
    if i % 3 == 0 and i % 5 == 0:
        dem = dem + 1
    i=i+1
print(dem)