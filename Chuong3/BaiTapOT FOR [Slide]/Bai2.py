n=int(input("n="))
if n>=2 and n<=100:
    for i in range(2,n):
        if n%i==0:
            print(n,"khong la SNT")
            break
        else:
            print(n,"la SNT")
            

#Cach giai khac toi uu hon
n=int(input())
SNT=True
for i in range (2,n):       #range((2,math.sqrt(n)+1):
    if n%i==0:
        SNT=False
        break
if  SNT==True:
    print(n,'la SNT')
else:
    print(n,'khong la SNT')