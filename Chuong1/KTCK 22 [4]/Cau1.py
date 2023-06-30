w=int(input())
if w<=1000: 
    h=int(input())
    if h<30000:
        mthue=str(input())
        if mthue=="A": thue=0
        elif mthue=="B": thue=0.1
        elif mthue=="C": thue=0.2
        elif mthue=="D": thue=0.29
        elif mthue=="E": thue=0.35
        else: print("Khong hop le!") 
        dgop=str(input())
        if dgop=="y": dg=10
        elif dgop=="n" : dg=0
    else: print("Khong hop le!")
else: print("Khong hop le!")
Th=w*h*thue
print(round((w*h+Th+dg),2))