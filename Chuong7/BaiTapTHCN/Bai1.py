#Viết chương trình:
#- Cho phép nhập vào một chuỗi ký tự bất kỳ;
#- Chương trình thực hiện đếm có bao nhiêu chữ cái in hoa,
# chữ cái in thường, chữ số và ký tự khác (bao gồm ký tự 
# trắng) xuất hiện trong chuỗi trên; 
#- In kết quả lên màn hình.

#TEST:
#Input: Python Programming Class @2021!
#Output:
#In hoa: 3
#In thuong: 19
#Chu so: 4
#Khac: 5



n=input()
h=t=s=k=0       #nếu có đếm phải để biến đếm = 0
for i in n:
    if i.isupper():     
        h+=1
    elif i.islower():
        t+=1
    elif i.isnumeric():
        s+=1
    else:
        k+=1
print('In hoa:',h,'\nIn thuong:',t,'\nChu so:',s,'\nKhac:',k)