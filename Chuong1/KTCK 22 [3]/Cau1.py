#nhập vào một số nguyên dương n, sau đó nhập n chuỗi 
# từ người dùng. Chương trình sẽ tính trung bình cộng 
# của các số trong danh sách chuỗi và in kết quả ra màn hình,
# làm tròn đến 2 chữ số thập phân.


n=int(input())
l=[]
k=[]
s=0
dem=0
if n>0:
    for i in range(1,n+1):  #thực hiện vòng lặp để nhập n chuỗi từ người dùng và thêm vào danh sách l
        m=input()
        l.append(m)
    for j in range(0,len(l)):   #kiểm tra nếu chuỗi l[j] là một số, thêm vào danh sách k
            if l[j].isnumeric():
                k.append(l[j])
    if k!=[]:   #nếu danh sách k không rỗng, thực hiện vòng lặp để tính tổng của các số trong danh sách k và đếm số lượng số
        for a in range(0,len(k)):
            dem=dem+int(k[a])
            s=s+1
        tbc=dem/s   #tính trung bình cộng tbc bằng cách chia tổng cho số lượng
    else:
        tbc=0   #Nếu danh sách k rỗng, gán giá trị trung bình cộng tbc bằng 0
    print(round(tbc,2))     #hàm round() để làm tròn giá trị tbc đến 2 chữ số thập phân
    
    
    