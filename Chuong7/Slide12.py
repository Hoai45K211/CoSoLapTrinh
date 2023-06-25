#Đoạn code này sử dụng một vòng lặp while để in từng ký tự
# trong chuỗi "banana" ra màn hình

fruit = "banana"
i=0
while i < len(fruit):
    letter=fruit[i]
    print(letter)
    i=i+1
    
#letter = fruit[i]: Gán giá trị của ký tự thứ i trong chuỗi 
# fruit cho biến letter. Điều này cho phép truy cập và lấy 
# giá trị của từng ký tự trong chuỗi.


fruit = "banana"
for char in fruit:
    print(char)
