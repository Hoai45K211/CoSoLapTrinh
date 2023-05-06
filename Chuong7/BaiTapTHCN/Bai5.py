n=input()
n=n.split()
X=int(input())
x=[]
for i in range(len(n)):
    if int(n[i])==X:
        x=x+[i+1]
if x==[]:
    print(0)
else:
    for i in x:
        print(i)