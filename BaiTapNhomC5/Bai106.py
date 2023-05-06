def remove_most_extreme_values(list_of_values, n):
    """
    Function to remove the most extreme values of a list.
    It creates a new copy of the list with the n largest
    elements and the n smallest elements removed.
    Parameters:
        list_of_values (list): list of input numbers from user.
        n (int): a non-negative number.
    Returns:
        new_list (list): a list generated from the input list
                    by removing outliers.
    Procedure:
        1. Used inbuilt method 'sorted' to sort all the elements
            in the input list
        2. Sliced the sorted list from starting and ending with n
    """
    new_list = []
    try:
        new_list = sorted(list_of_values)[n:-n]
    except Exception as e:
        print ('Exception occured in remove_most_extreme_values function: ', str(e))
    return (new_list)

def main():
    try:
        list_of_values = list(map(int, input("\nEnter the numbers : ").strip().split()))
        if len(list_of_values) >= 4:
            non_negative_number_n = int(input("Enter a non-negative number: "))
            new_list_without_outliers = remove_most_extreme_values(list_of_values, non_negative_number_n)
            print ("New list without outliers: " + ", ".join(map(str, new_list_without_outliers)))
            print ("Input list with outliers: " + ", ".join(map(str, list_of_values)))
        else:
            print ("Enter more than 3 numbers.")
    except Exception as e:
        print ('Exception occured in main function: ', str(e))
if __name__ == "__main__":
    main()