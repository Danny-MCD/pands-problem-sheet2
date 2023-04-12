# **pands-problem-sheet**

## ***A collection of weekly tasks for the Programming and Scripting module in Computer Science Higher Diploma in Data Analytics course***  
  

~~~

List of weekly tasks and associated programs.

- Week 1:    helloworld.py
- Week 2:    bank.py
- Week 3:    accounts.py
- Week 4:    collatz.py
- Week 5:    weekday.py
- Week 6:    squareroot.py
- Week 7:    es.py
- Week 8:    plottask.py
~~~


## Individual Description of Programmes
------------
### Weekly Tasks 1
For this week's tasks, 

Please simply introduce yourself in the Discussion forum, 
Install the required software on your machine,
Pull the sample code in my repository to your machine,
Create a GitHub account and repository for yourself (mywork), and the problem sheet (pands-problem-sheet)
Commit and push a file to the problem sheet called helloworld.py
This file should contain a python program that displays Hello World! when it is run.


### Introduction

The first program tasked to create was helloworld.py which would print out Hello World! when run.
A very simple program with only the use of the print function.

It required familarisation with GitHub as it was required to create an account in GitHub and multiple repositories within that account as set out in the tasks. Specific repositories were then to be cloned to our personal computer where we would write and save code to them via VSCode. After writing the code the program would need to be pushed back to the repository on GitHub for review at a later date.

The commands required to do this are set out below.

For cloning the repository to our PC

- git clone PASTED.URL
- git config pull.rebase false
- git pull


For pushing saved data in VSCode back to GitHub

- git add .
- git commit -m "write any comments in here"
- git push


For pulling data down to PC from GitHUb 

- git pull (when in the directory you want to update the information from)


### Calling the program
The program is called with the commands 

~~~
\\> python helloworld.py
The program prints 
    Hello World!
~~~

### Weekly Tasks 02

When Banks are storing currency figures, they store them as integers (usually in cent).This is to avoid rounding errors. 

Write a program called bank.py 

The program should:

Prompt the user and read in two money amounts (in cent)
Add the two amounts
Print out the answer in a human readable format with a euro sign and decimal point between the euro and cent of the amount 


### Introduction

The program required a number of steps to have it work as directed in the task.

The use of the input function in python to take in a value from the user. These were set to the integer class and assigned to a variable.

The simple sum function was used to add them. The total was then converted to euro by dividing by 100.

Finally the prgram would terminate and print the formatted sentence to include the variable total and display it to the user with the required euro sign in front of the total.




### Calling the program
The program is called with the commands 
~~~
\\> python bank.py
The program requests the user input an ammount in cents
    Enter the first amount in cents:

Once a number is inputted and RETURN pressed the program will print the second line
    Enter the second amount in cents:

Again once an ammount is entered the program will sum the two amounts and return the total in euro.
    The sum of these is €
    
~~~

### Weekly Task 03
Bank account numbers can be stored as 10 character strings, for security reasons some applications only display the last 4 characters (with the  other characters replaced with Xs).

Write a python program called accounts.py that reads in a 10 character account number and outputs the account number with only the last 4 digits showing (and the first 6 digits replaced with Xs).

Update to include working for a number of any lenght of characters


### Introduction

The third weekly task involved the creation of the accounts.py program. The purpose of the program was to be able to read in an account number as a string and print back out the number on the screen with the first 6 of 10 numbers replaced by X's.

Research on the maunipulation of strings was looked at and slicing using negative indexing was found to be the simplest method when working from the end of the number back. Which fitted in perfectly with the update to be able to have the program work for a bank account number of any lenght. 

The end of the string is set as index value -1 and slicing from -5:-1 will slice out the last 4 digits.
These last 4 digits were then concantanated with 6X's before being displayed as the answer. Changes to the size of the account number would have no difference on the size of the end result.

THe program will always display 6X's onto the start of the account number no matter how many digits it is copying over.

### Calling the program
The program is called with the commands 
~~~
\\> python accounts.py
The program requests the user input an account number
    Please enter account number:

    Any integer of any lenght can be inputed.

xxxxxx8976
The account number with the first 6 digits displayed as X's will be shown along with last 4 digits of the account number.
~~~

### Weekly task 04
Write a program, called collatz.py, that asks the user to input any positive integer and outputs the successive values of the following calculation.

At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one.

Have the program end if the current value is one.


### Introduction
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



### Calling the program
The program is called with the commands 
~~~
\\> python collatz.py
The program prints 
    Enter Positive Integer: 
When a positive number is entered the program will display the collatz conjecture series of numbers ending when the sequence reaches 1
The program will then terminate.

If a negative number is entered the program will show the collatz conjecture sequence of 1

If floating point number or string is entered the program will display a ValueError and terminate.

~~~
### Weekly Task 05
Write a program that outputs whether or not today is a weekday. (The program should be called weekday.py)

(You will need to search the web to find how you work out what day it is)

An example of running this program on a Thursday is given below.

$ python weekday.py
Yes, unfortunately today is a weekday.


An example of running it on a Saturday is as follows:

$ python weekday.py
It is the weekend, yay!


### Introduction

This program would have to use the current date and be able to assess what day of the week it currently is. The datetime module was researched for this and the weekday function within it and how that is represented (Geeksforgeeks, 2017).

The datetime module was initially imported into the program and then the now() argument applied to it to create a object with the current date.

The weekday function was applied to this object to have it represent the current day of the week
with Monday = 0, Tuesday = 1 and so on until Sunday = 6

These representitive values for the weekday were used with a if else statement to print 1 statement for all weekdays up to 4 or Friday or else it would print a statement if current date showed it to be a weekend day of the week.

### Calling the program
The program is called with the commands 
~~~
\\> python weekday.py

The program takes in no input but will print
"Today is a weekday" if the current date is a weekday Monday to Friday

The program will print
"Hurray, It is the weekend" , if the current date puts it on the weekend when it is run.
~~~

### Weekly task 06
Write a program that takes a positive floating-point number as input and outputs an approximation of its square root.

You should create a function called <tt>sqrt</tt> that does this.

I am asking you to create your own sqrt function and not to use the built in functions x ** .5 or math.sqrt(x).

This is to demonstrate that you can research and code a process (If you really needed the square root you would use one of the above methods).

I suggest that you look at the newton method at estimating square roots.

This is a more difficult task than some of the others, but will be marked equally, so only do as much work on this as you feel comfortable.


### Introduction

The task recommended utilising the newton method for estimating square roots so this was researched initially. 

In Newton’s Method, you start with any estimate of the square root, x.
You then compute a new estimate for x using the equation x^{new}=\frac{x+\frac{n}{x}}{2}.
You then update x with the new estimate x^{new}, and repeat the process until x and x^{new} do not change (or that the difference is “close enough”). (Python Programming, 2021)

I then reserched the python program code used to implement the newton method. I started off defining a function called sqrt as called for that takes in a value n for the floating point number and a number l for the tolerance in accuracy. The formulae for newtons method of approximating square roots was then placed inside a while loop that would implemnt the mathematical operation on the floating point number and update the new value n with the new approximation each time until the values of n would be found to be within the tolerance l level defined initally. At which point the if statement would break the loop and the square root approximation would be printed as output.

### Calling the program
The program is called with the commands 
~~~
\\> python squareroot.py

The program displays the message
    Please enter a positive number: 67
    The square root of 67.0 is 8.185352771872815

The user inputted value of 67 was added in for clarity

~~~
### Weekly Task 07
Write a program that reads in a text file and outputs the number of e's it contains. Think about what is being asked here, document any assumptions you are making.

The program should take the filename from an argument on the command line. I have not shown you how to do this, you need to look it up.


### Introduction

The program es.py required the use of some new techniques
file = open(file_name, 'r')
Was used to be able to open the file and read in the contents.
The count function was used to determine the number of lower case "e" that are contained in the document.
The final part of the program required the file name to be taken from an argument on the command line. 
The command
    file_name = sys.argv[1] 
This sets the command line argument containing the txt file name to be used as the variable file_name 
For this to work the file used for testing must be located in the same directory as the python program. I have added in mobydick.txt for testing purposes.


Calling the program
The program is called with the commands 
~~~
\\> python es.py mobydick.txt
The program prints 
    The number of times the letter e is used in mobydick.txt
    58820
~~~
### Weekly Task 08
Write a program called plottask.py that displays:

a histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2, 
and a plot of the function  h(x)=x3 in the range [0, 10], 
on the one set of axes.
Some marks will be given for making the plot look nice (legend etc).


Introduction

The initial steps required the importation of the modules
matplotlib for its ability to be able to generate plots and numpy so that random numbers can be generated.
1000 numbers were then generated with a preset mean and standard deviation which were then imported into a histogram plot. The plot had its axis's labelled and legend created to better explain it.
The exponential curve of the function was then overlayed on top of the histogram.


### Calling the program
The program is called with the commands 
~~~
\\> python plottask.py
The program shows the plot
    "Histogram Distribution overlayed on Exponential Curve"

~~~

### References




Stackoverflow (2018) Available at: https://stackoverflow.com/questions/26788266/collatz-sequence (Accessed: 20 Febuary 2023).

Geeksforgeeks (2021) Available at: https://www.geeksforgeeks.org/python-datetime-weekday-method-with-example/ (Accessed: 27 February 2023)

Python Programming (2021) Available at: https://python.pages.doc.ic.ac.uk/2021/lessons/lesson04/04-applied/06-newtonhtml (Accessed: 28 March 2023)