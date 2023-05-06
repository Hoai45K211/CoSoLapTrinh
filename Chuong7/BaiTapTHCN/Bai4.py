n=input()
n=n.split(',')
m=[]
for i in n:
    if i not in m:
        m=m+[i]
m.sort()
print(','.join(m))