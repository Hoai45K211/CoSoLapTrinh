def NhapvaIn():
    pw=input("Enter a password:")
    if ktr(pw)==True:
        print("That is a good password!")
    else: print("That is not a good password!")
    return pw
def ktr(pw):
    h= False; t= False; s= False
    for i in pw:
        if i>="A" and i<="Z":
            h=True
        if i>="a" and i<="z":
            t=True
        if i>="0" and i<="9":
            s=True
    if len(pw)>=8 and h and t and s:
        return True
    else: return False
pw=NhapvaIn()
ktr(pw)