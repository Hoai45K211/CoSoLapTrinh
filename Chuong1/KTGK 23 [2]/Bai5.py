#tính tổng các số chẵn không vượt quá n, 
# với n được nhập vào từ bàn phím.


n=int(input())
dem=0
for i in range(1,n+1):
    if i%2==0:
        dem=dem+i
print(dem)