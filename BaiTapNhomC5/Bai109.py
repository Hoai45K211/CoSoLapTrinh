import math
def findDivisors(num):

    li = []
    i = 2
    divisor = math.sqrt(num)
    newDiv = num / i
    while(i <= divisor):
        if(num % i == 0):
            if(i == newDiv):
                li.append(i)
            else:
                li.append(i)
                li.append(newDiv)
        i = i + 1
    return li

num = int(input("Enter a positive number\n"))
res = findDivisors(num)
print(res)