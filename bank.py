# Sums two ammounts and prints the answer
# Author: Daniel Mc Donagh


# Program takes in an inputted value and sets it as a variable
Amt1 = int(input("Enter the first amount in cents: "))
Amt2 = int(input ("Enter the second amount in cents: "))

# basic arithmetic of summing two variables that are integers
sum = Amt1 + Amt2

# conversion of integer ammount in cents to euro
total = int(sum)/100

# formatting and printing of total 
print (f"The sum of these is €{total}") 
