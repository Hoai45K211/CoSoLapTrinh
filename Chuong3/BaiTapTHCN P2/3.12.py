n=input("")
char="ABCDEFGHKL"

if int(n)>=0 and int(n)<=10000:
    y=0
    while y<len(n):
        print(char[int(n[y])],end="")
        y+=1