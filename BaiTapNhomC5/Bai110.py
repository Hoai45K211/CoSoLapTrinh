def isPerfect(num):
    '''
    Given a number it checks if it is a perfect number; if perfect return True else False
    '''
    sum=0
    for i in range(1,(num//2)+1):
        if num%i==0:
            sum=sum+i
    if sum==num:
        return True
    else:
        return False
    
def main():
    print("List of perfect numbers between 1 to 10,000 are: ")
    for num in range(1,10000):
        if isPerfect(num):
            print(num)
            
if __name__=="__main__": 
    main()