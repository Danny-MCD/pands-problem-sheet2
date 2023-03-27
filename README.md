# pands-problem-sheet

## A collection of weekly tasks for the Programming and Scripting module
## in Computer Science HDip in Data Analytics course

### List of weekly tasks and associated programs
#### Week 1:    helloworld.py
#### Week 2:    bank.py
#### Week 3:    accounts.py
#### Week 4:    collatz.py
#### Week 5:    weekday.py
#### Week 6:    squareroot.py
#### Week 7:    es.py
#### Week 8:    plottask.py

### Individual description of programmes

### Week 1
#### The inital week 1 task was not about the program helloworld.py which simply prints out Hello World
#### But was to make us familiar with the enviroment in which we would be writing and saving code.
#### Anaconda version of phython was installed in VScode and VScode was synced with a repository in GIthub to allow us push and pull information from github. To this end some of the important information learnt was to use the commands 
#### Git add .
#### git commit -m "commit message"
#### git push
#### input your passphrase
#### To pull down information from the lecture notes. I would have to be in the partiular folder in terminal and then use the command
#### Git pull 
#### Which would pull down the latest information from the git hub repository


### Week 2
#### Second weeks task was to write a program called bank.py that was to take two inputted ammounts in cents and sum these ammounts. Then finally convert to euros and print that total. Showed the use of the input function for taking in data into a program. Basic aritmatic in summing two values. Formatting and printing out of the total to the user.

### Week 3
#### The third task was the creation of accounts.py program. It was to read in a 10 digit account number and send back the same account number with the first 6 digits replaced with X's.
#### I learnt different ways to manipulate strings. To get the last 4 digits from the account number negative indexing was used to count back 4 digits from the end of the string of numbers and then splice these 4 numbers onto the 6 X's to complete the task.


Weekly task 4
Write a program, called collatz.py, that asks the user to input any positive integer and outputs the successive values of the following calculation.

At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one.

Have the program end if the current value is one.

-----------------
Introduction
The collatz conjecture is an unsolved problem from mathematics that looks to see whether repeating two simple arithmetic operations on a positive integer will eventually transform the number to 1.

For this program various methods were looked at on stackoverflow (Stackoverflow, 2018). 

The program initially calls for a positive  integer to be inputted from user to be used to create the collatz sequence.

A function collatz was initially defined with a value n which would be taken in as the positive user input value.

The task required that the arithmetic operation gets applied to the value n and result displayed in the sequence at the end.

A while loop is repeated while the value n is greater than 1. This also serves as the termination of the loop when it reaches 1.

Each time the operations are carreid out the value n is changed and added to the sequence to be printed at end.

The first arithmetic operation checks if n is odd by checking if n modulus 2 gives a remainder. True if it does and the value n is multiplied by 3 and 1 added to it.

Else the value must be even and it is divided by 2

This loop keeps repeating while n is not 1

At this point the program will print
Collatz conjecture sequence: (sequence of numbers ending in 1)
Each  value that n had throughout the program will be added into the sequence.



Calling the program
The program is called with the commands 
\\> python collatz.py
The program prints 
    Enter Positive Integer: 
When a positive number is entered the program will display the collatz conjecture series of numbers ending when the sequence reaches 1
The program will then terminate.

If a negative number is entered the program will show the collatz conjecture sequence of 1

If floating point number or string is entered the program will display a ValueError and terminate.


Weekly Task 05
Write a program that outputs whether or not today is a weekday. (The program should be called weekday.py)

(You will need to search the web to find how you work out what day it is)

An example of running this program on a Thursday is given below.

$ python weekday.py
Yes, unfortunately today is a weekday.


An example of running it on a Saturday is as follows:

$ python weekday.py
It is the weekend, yay!

----------------------
Introduction

This program would have to use the current date and be able to assess what day of the week it currently is. The datetime module was researched for this and the weekday function within it and how that is represented (Geeksforgeeks, 2017).

The datetime module was initially imported into the program and then the now() argument applied to it to create a object with the current date.

The weekday function was applied to this object to have it represent the current day of the week
with Monday = 0, Tuesday = 1 and so on until Sunday = 6

These representitive values for the weekday were used with a if else statement to print 1 statement for all weekdays up to 4 or Friday or else it would print a statement if current date showed it to be a weekend day of the week.

Calling the program
The program is called with the commands 
\\> python weekday.py

The program takes in no input but will print
"Today is a weekday" if the current date is a weekday Monday to Friday

The program will print
"Hurray, It is the weekend" , if the current date puts it on the weekend when it is run.


Weekly task 6
Write a program that takes a positive floating-point number as input and outputs an approximation of its square root.

You should create a function called <tt>sqrt</tt> that does this.

I am asking you to create your own sqrt function and not to use the built in functions x ** .5 or math.sqrt(x).

This is to demonstrate that you can research and code a process (If you really needed the square root you would use one of the above methods).

I suggest that you look at the newton method at estimating square roots.

This is a more difficult task than some of the others, but will be marked equally, so only do as much work on this as you feel comfortable.


-------------
Introduction










References




Stackoverflow (2018) Available at: https://stackoverflow.com/questions/26788266/collatz-sequence (Accessed: 20 Febuary 2023).

Geeksforgeeks (2021) Available at: https://www.geeksforgeeks.org/python-datetime-weekday-method-with-example/ (Accessed: 27 February 2023)