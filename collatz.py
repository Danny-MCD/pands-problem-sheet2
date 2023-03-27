# program to collatz a given number
# Author: Daniel Mc Donagh

# asks the user to input any positive integer 
# and outputs the successive values of the following calculation.
# At each step calculate the next value by taking the current value
#  and, if it is even, divide it by two, 
# but if it is odd, multiply it by three and add one.
# Have the program end if the current value is one.



#  A function called collatz is defined that will take in an integer n
def collatz(n):

    # the sequence of operations will repeat while n is greater than 1
    while n > 1:
        print(n, end=' ')

        if (n % 2):
            # n is odd if there is a remainder from n%2 and the following operation will happen
            n = 3*n + 1
        else:
            # n is even if it is not odd and so the following operation will be performed
            n = n//2
            # end='' will place a space after each sequence number instead of  putting it on a new line.
    print(1, end='')
 
 # Displays "Enter positive integer" too user and takes in a input as an integer
n = int(input('Enter positive integer: '))
print('Collatz Conjecture Sequence: ', end='')
# calling the collatz function
collatz(n)