# accepts a 10 digit account number and prints it with characters 1-6 replaced with X's
# Author: Daniel Mc Donagh

AccNo = str(input("Please enter account no: "))

# modification required to deal with account number of any lenght
# It is assumed that last digits still being viewed and all else should be replaced by 6X's
# address location changed to replace every number prior to last 4 using negative index loaction

# string allows unlimited number lenght
# output concantanates 6X's to start of spliced last 4 digits from string

print ("xxxxxxx"+AccNo[-5:-1])
