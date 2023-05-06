st1=input().split()
st2=input().split()
dem=0
for i in st1:
    if i in st2:
        dem+=1
if dem == len(st1):
    print("True")
else:
    print("False")