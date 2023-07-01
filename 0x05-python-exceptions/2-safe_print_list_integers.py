#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0  # Variable to keep track of the number of integers printed
    
    for i in range(x):
        try:
            if isinstance(my_list[i], int):  # Check if the element is an integer
                print("{:d}".format(my_list[i]), end="")
                count += 1
        except IndexError:
            break  # Stop the loop if we reach the end of the list
    
    print()  # Print a new line after all integers are printed
    return count
