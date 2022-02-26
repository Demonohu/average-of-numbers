# Assume a file containing a series of integers is named numbers.txt and exists on the 
# computer’s disk. Write a program that calculates the average of all the numbers stored in 
# the file.

def main():
    """
    This program calculates and display the average of the numbers stored in the numbers.txt file
    """
    total = 0.0       #Initialize an accumulator to 0.0. 
    count = 0         #Initialize a variable to keep count of the numbers.

    #Open the numbers.txt file.
    numbers = open('numbers.txt', 'r')

    for number in numbers:
        total += eval(number)
        count += 1

    average = total/count

    print('The average of the numbers =', average)

main()