#Nhập vào một số nguyên dương n (n>0)
#Nhập liên tục chuỗi ký tự bất kỳ cách nhau bởi phím enter
#Tính TBC các số tự nhiên trong dãy ký tự trên, kết quả được
# làm tròn đến 2 chữ số

#INPUT
#5
#Learn
#1
#2
#Python
#3

#OUTPUT
# 2.0


n = int(input())
while n <= 0:
    break

st = []
for x in range(n):
    i = input()
    if i.isnumeric():
        st.append(int(i))

tbc = sum(st) / len(st)
print(round(tbc, 1))