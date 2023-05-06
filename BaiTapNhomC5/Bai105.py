def main():
    numbers_list = []
    print("Enter 0 to exit.")
    flag = False

    while not flag:
        number = int(input("Enter a number : "))
        if number != 0:
            numbers_list.append(number)
        else:
            flag = True

    if numbers_list:
        print("Below are the numbers entered by user in reverse order:")
        [print(num) for num in reversed(numbers_list)]
    
    if __name__ == '__main__':
        main()