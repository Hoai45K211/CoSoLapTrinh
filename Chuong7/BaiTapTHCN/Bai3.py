n=input()
x=0
if len(n)<6 or len(n)>17 or n.islower() or n.isupper() or n.isalnum():
        print(False)
else:
    for i in n:
        if i=='$' or i=='#' or i=='@':
                x=1
                break
    if x==1:
        print(True)
    else: print(False)