#nhập vào một số nguyên n và sau đó nhập n số nguyên. 
# Chương trình sẽ chia danh sách số nguyên thành hai phần,
# tính tổng của các phần tử trong mỗi phần, 
# và in ra tổng hiệu của hai tổng đó.


import math
L=[]
K=[]
n=int(input())
s1=0
s2=0
if n>0:
    for h in range(1,n+1):
        x=int(input())
        L.append(x)
        i=1
        while 1<=i<n:
            x=L[0:i+1]
            y=L[i:-1]
        for a in range(0,len(x)):
                s1=s1+x[a]
        for b in range(0,len(y)):
                s2=s2+x[b]
        s=s1-s2
        i=i+1
    print(s)
        