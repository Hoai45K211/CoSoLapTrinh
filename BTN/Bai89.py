def Nhap():
    ch=str(input("Enter:"))
    return ch
def Hoa(ch):
    day=ch.capitalize()
    day=day.replace(" i "," I ")
    vtr=0
    while vtr<len(ch):
        if day[vtr]=="." or day[vtr]=="!" or day[vtr]=="?": 
            vtr=vtr+1
            while vtr<len(ch) and day[vtr]==" ": vtr=vtr+1
            if vtr<len(ch): day=day[0:vtr]+\
                                day[vtr].upper()+\
                                day[vtr+1:len(day)]
        vtr=vtr+1
    return day
ch=Nhap()
day=Hoa(ch)
print(day)
