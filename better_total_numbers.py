# Modify the program that you wrote for total_numbers.py so it handles the following exceptions:
# •	 It should handle any IOError exceptions that are raised when the file is opened and data 
# is read from it.
# •	 It should handle any ValueError exceptions that are raised when the items that are read 
# from the file are converted to a number.

def  main():
    """
    This program is a modification of the program in total_numbers.py. This program handles IOError and ValueError.
    """
    total = 0.0       #Initialize an accumulator to 0.0. 
    count = 0         #Initialize a variable to keep count of the numbers.

    try:
    #Open the numbers.txt file.
        numbers = open('numbers.txt', 'r')
        for number in numbers:
            total += eval(number)
            count += 1

        average = total/count

        print('The average of the numbers =', average)
    except IOError:
        print('Error! File not found. Enter a valid file, ode.')
    except ValueError:
        print("Don't be stupid. Enter a valid number.")

main()