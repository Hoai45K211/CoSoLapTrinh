#In lên màn hình theo cấu trúc sau:
#$$$$$$$$$
#$$$$$$$$
#$$$$$$$ 
#$$$$$$  
#$$$$$   
#$$$$
#$$$
#$$
#$

#Cach 1
i=1
while i<=9:
    j=1
    while j<= (10-i):           # In len man hinh (10-i) dau $
        print("$",end="")
        j+=1
    print()                     #Xuong dong
    i+=1
    
#Sua de: In len man hinh so n
n=int(input("n="))
i=1
while i<=n:
    j=1                         # In len man hinh (n+1-i) dau $
    while j<= (n+1-i):
        print("$",end="")
        j+=1
    print()                     #Xuong dong
    i+=1

#Cach 2
i=1                             #i bieu dien so cot
while i<=9:
    j=9                         #j bieu dien so hang
    while j>=i:
        print("$",end="")
        j=j-1
    print()                     #xuong dong
    i=i+1
    
#Cach 3
i=9
while i<=9:
    print(i*"$")
    i=i-1                       #i-=1