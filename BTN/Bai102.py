def Nhapvdoi():
    global min
    print("Enter the volumes of ingredients:")
    cup=int(input("Cup:"))
    tablesp=int(input("Tapblespoon:"))
    teasp=int(input("Teaspoon:"))
    min=cup*48+tablesp*3+teasp
    return min
def rut(min):
    cp=min//48
    table=(min-cp*48)//3
    tea=(min-cp*48-table*3)
    return cp,table,tea
def inkq(cp,table,tea):
    if cp!=0:
        if cp==1: print("1 cup",end="")
        else: print(cp,"cups",end="")
        if min!=48: print(", ",end="")
    if table!=0:
        if table==1: print("1 tablespoon",end="")
        else: print(table,"tablespoons",end="")
        if tea!=0: print(", ",end="")
    if tea!=0:
        if tea==1: print("1 teaspoon",end="")
        else: print(tea,"teaspoons",end="")
Nhapvdoi()
cp,table,tea=rut(min)
inkq(cp,table,tea)