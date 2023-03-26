soam=0
soduong=0
while True:
    a=int(input())
    if a==0:
        break
    elif a>0:
        soduong+=1
    else:
        soam+=1
print(soduong,"so duong")
print(soam,"so am")