n=input()
n=n.strip()
a=n[0].upper()+n[1:].lower()
a=a.split()
n=''
for i in a:
    if i==',' or i==':' or i==';' or i=='.':
        n=n.strip()+i+' '
    else: n=n+i+' '
print(n.strip())