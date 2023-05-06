a = list()
while True:
    val = int(input())
    if val != 0:
        a.append(val)
    else:
        a.sort()
        for i in a:
            print(i)
        break