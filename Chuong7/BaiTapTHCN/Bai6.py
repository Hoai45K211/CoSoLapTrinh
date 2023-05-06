n=input()
n=n.split(',')
m=[]
for i in n:
    if int(i,2)%3==0:
        m=m+[i]
print(','.join(m))