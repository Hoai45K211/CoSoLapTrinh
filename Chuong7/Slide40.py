#Phương thức rjust(n,ch), ljust(n,ch), center(n,ch)
#Viết chương trình nhập vào tên và số lượng của 4 một mặt 
# hàng bất kỳ, in lên màn hình bảng thực đơn theo mẫu sau.

#sandwiches..........       4
#apples..............      12
#cups................       4
#cookies.............    8000

mon1=input("Mon 1:")
sl1=input("So luong:")
mon2=input("Mon 2:")
sl2=input("So luong:")
mon3=input("Mon 3:")
sl3=input("So luong:")
mon4=input("Mon 4:")
sl4=input("So luong:")


print(mon1.ljust(20,"."),end="")
print(sl1.rjust(8," "))
print(mon2.ljust(20,"."),end="")
print(sl2.rjust(8," "))
print(mon3.ljust(20,"."),end="")
print(sl3.rjust(8," "))
print(mon4.ljust(20,"."),end="")
print(sl4.rjust(8," "))