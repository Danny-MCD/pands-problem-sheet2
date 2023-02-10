# Sums two ammounts and prints the answer
# Author: Daniel Mc Donagh

Amt1 = int(input("Enter the first amount in cents: "))
Amt2 = int(input ("Enter the second amount in cents: "))

sum = Amt1 + Amt2

total = int(sum)/100

print (f"The sum of these is €{total}") 
