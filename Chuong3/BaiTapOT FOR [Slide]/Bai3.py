n=int(input("n="))
dem=0
for i in str(n):
    dem=dem+1
print(n,"co",dem,"chu so")

#Cach khac
n=int(input("n="))
so=n
if n!=0:
    dem=0
    while n>0:
        n=int(n/10)
        # print("lan",dem+1,"n=",n)
        dem+=1
else:
    dem=1
print(so,"co",dem,"chu so")
