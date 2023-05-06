n=input()
h=t=s=k=0
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